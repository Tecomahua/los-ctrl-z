#include <cstdint>
#include <cstdio>
#include <cstring>

namespace {
constexpr uint32_t USERS = 2000000;
// 20 bytes/user, 40,000,000 bytes total. Arrays avoid struct padding.
uint32_t events[USERS];
uint32_t previous[USERS]; // (timestamp << 2) | action; fits in 32 bits.
uint32_t gaps[USERS];
int64_t gapSum[USERS];

class Input {
    static constexpr size_t CAPACITY = 1 << 20;
    unsigned char buffer[CAPACITY];
    size_t pos = 0, size = 0;

    int get() {
        if (pos == size) {
            size = std::fread(buffer, 1, CAPACITY, stdin);
            pos = 0;
            if (!size) return EOF;
        }
        return buffer[pos++];
    }

public:
    // Consume the whole physical line, even if it is invalid or too long.
    // Strip one residual CR; native Windows text input already translates CRLF.
    bool line(char* out, size_t capacity, int& length) {
        size_t used = 0;
        bool overflow = false, any = false;
        int c;
        while ((c = get()) != EOF && c != '\n') {
            any = true;
            if (used + 1 < capacity) out[used++] = static_cast<char>(c);
            else overflow = true;
        }
        if (c == EOF && !any) return false;
        if (used && out[used - 1] == '\r') --used;
        out[used] = '\0';
        length = overflow ? -1 : static_cast<int>(used);
        return true;
    }
};

Input input;

bool number(const char*& p, const char* end, uint64_t& value) {
    value = 0;
    unsigned digits = 0;
    while (p < end && *p >= '0' && *p <= '9') {
        if (++digits > 12) return false;
        value = value * 10 + static_cast<unsigned>(*p++ - '0');
    }
    return digits != 0;
}

bool parse(const char* line, int length, uint32_t& t, uint32_t& u,
           uint32_t& action) {
    if (length < 0) return false;
    const char* p = line;
    const char* end = line + length;
    uint64_t time, user;
    if (!number(p, end, time) || p == end || *p++ != ' ') return false;
    if (!number(p, end, user) || p == end || *p++ != ' ') return false;
    if (time > 1000000000 || user >= USERS) return false;
    const size_t n = static_cast<size_t>(end - p);
    if (n == 4 && std::memcmp(p, "READ", 4) == 0) action = 0;
    else if (n == 5 && std::memcmp(p, "WRITE", 5) == 0) action = 1;
    else if (n == 5 && std::memcmp(p, "LOGIN", 5) == 0) action = 2;
    else if (n == 6 && std::memcmp(p, "LOGOUT", 6) == 0) action = 3;
    else return false;
    t = static_cast<uint32_t>(time);
    u = static_cast<uint32_t>(user);
    return true;
}
} // namespace

int main() {
    char line[128];
    int length;
    long long t1, t2, threshold, n;
    if (!input.line(line, sizeof line, length) || length < 0 ||
        std::sscanf(line, "%lld %lld %lld", &t1, &t2, &threshold) != 3)
        return 0;
    if (!input.line(line, sizeof line, length) || length < 0 ||
        std::sscanf(line, "%lld", &n) != 1 || n < 0 || n > 5000000)
        return 0;

    for (long long i = 0; i < n; ++i) {
        if (!input.line(line, sizeof line, length)) break;
        uint32_t t, u, action;
        if (!parse(line, length, t, u, action) || t < t1 || t > t2) continue;
        const uint32_t key = (t << 2) | action;
        if (events[u]) {
            if (previous[u] == key) continue;
            const int64_t delta = static_cast<int64_t>(t) - (previous[u] >> 2);
            if (delta <= threshold) {
                gapSum[u] += delta;
                ++gaps[u];
            }
        }
        previous[u] = key; // A cut still establishes the next predecessor.
        ++events[u];
    }

    uint32_t top[5];
    unsigned used = 0;
    // Ascending traversal preserves the lower-user tie break.
    for (uint32_t u = 0; u < USERS; ++u) {
        if (!events[u]) continue;
        unsigned at = 0;
        while (at < used && events[top[at]] >= events[u]) ++at;
        if (at == 5) continue;
        if (used < 5) ++used;
        for (unsigned j = used - 1; j > at; --j) top[j] = top[j - 1];
        top[at] = u;
    }
    if (!used) std::puts("SIN DATOS");
    for (unsigned i = 0; i < used; ++i) {
        const uint32_t u = top[i];
        if (!gaps[u]) {
            std::printf("%u %u NA\n", u, events[u]);
        } else {
            // Exact nearest rounding, ties away from zero. On ordered input
            // gapSum is nonnegative; signed handling also covers reverse probes.
            const int64_t sum = gapSum[u];
            const uint64_t magnitude = static_cast<uint64_t>(sum < 0 ? -sum : sum);
            const uint64_t milli = (magnitude * 1000 + gaps[u] / 2) / gaps[u];
            std::printf("%u %u %s%llu.%03llu\n", u, events[u],
                        sum < 0 && milli ? "-" : "",
                        static_cast<unsigned long long>(milli / 1000),
                        static_cast<unsigned long long>(milli % 1000));
        }
    }
    return 0;
}
