#include <bits/stdc++.h>
using namespace std;

// Semantica provisional: longitud fisica; ceros ignorados para la mediana;
// un tramo sin lecturas no cuenta; para cardinalidad par se usa mediana superior.
// La caja negra oficial es necesaria para confirmar estas convenciones.

class FastInput {
    static constexpr size_t B = 1 << 16;
    char buf[B]; size_t at = 0, len = 0;
public:
    int next() {
        int c;
        do {
            if (at == len) { len = fread(buf, 1, B, stdin); at = 0; if (!len) return -1; }
            c = buf[at++];
        } while (c <= ' ');
        int x = 0;
        do {
            x = x * 10 + c - '0';
            if (at == len) { len = fread(buf, 1, B, stdin); at = 0; if (!len) break; }
            c = buf[at++];
        } while (c >= '0' && c <= '9');
        return x;
    }
};

string decimal(__int128 x) {
    if (!x) return "0";
    string s;
    while (x) { s.push_back(char('0' + x % 10)); x /= 10; }
    reverse(s.begin(), s.end());
    return s;
}

int main() {
    FastInput in;
    int n = in.next(); if (n < 0) return 0;
    int L = in.next(), R = in.next(), M = in.next();
    vector<int> pref(n + 1);
    vector<int> freq(2 * n + 1);
    vector<long long> indexSum(2 * n + 1);
    const int offset = n;
    long long qualified = 0, qualifiedIndexSum = 0;
    long long count = 0;
    __int128 lengthSum = 0;
    int lastNonzero = 0;
    for (int j = 1; j <= n; ++j) {
        int a = in.next();
        if (a) lastNonzero = j;
        int delta = a == 0 ? 0 : (a >= M ? 1 : -1);
        pref[j] = pref[j - 1] + delta;
        int oldThreshold = pref[j - 1];

        int remove = j - R - 1;
        if (remove >= 0) {
            int bucket = pref[remove] + offset;
            --freq[bucket]; indexSum[bucket] -= remove;
            if (pref[remove] <= oldThreshold) {
                --qualified; qualifiedIndexSum -= remove;
            }
        }
        int add = j - L;
        if (add >= 0) {
            int bucket = pref[add] + offset;
            ++freq[bucket]; indexSum[bucket] += add;
            if (pref[add] <= oldThreshold) {
                ++qualified; qualifiedIndexSum += add;
            }
        }
        if (delta == 1) {
            int bucket = pref[j] + offset;
            qualified += freq[bucket]; qualifiedIndexSum += indexSum[bucket];
        } else if (delta == -1) {
            int bucket = oldThreshold + offset;
            qualified -= freq[bucket]; qualifiedIndexSum -= indexSum[bucket];
        }

        long long valid = qualified;
        __int128 validLength = (__int128)j * qualified - qualifiedIndexSum;
        // Solo los tramos enteramente formados por ceros tienen suma transformada 0
        // pero carecen de mediana.
        int firstZeroStart = max(j - R, lastNonzero);
        int lastStart = j - L;
        if (firstZeroStart <= lastStart) {
            long long zeroCount = (long long)lastStart - firstZeroStart + 1;
            long long zeroIndexSum = (long long)(firstZeroStart + lastStart) * zeroCount / 2;
            valid -= zeroCount;
            validLength -= (__int128)j * zeroCount - zeroIndexSum;
        }
        count += valid;
        lengthSum += validLength;
    }
    printf("%lld %s\n", count, decimal(lengthSum).c_str());
}
