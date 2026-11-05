#include <bits/stdc++.h>
using namespace std;

// Semantica provisional: se elige un camino minimo S-T y se puede recorrer
// gratuitamente un subcamino contiguo, en el sentido S hacia T, una vez.
// Se requiere la caja negra oficial para confirmar las reglas del pase.

using i64 = long long;
const i64 INF = LLONG_MAX;

class FastInput {
    static constexpr size_t B = 1 << 16;
    char buf[B]; size_t at = 0, len = 0;
public:
    i64 next() {
        int c;
        do {
            if (at == len) { len = fread(buf, 1, B, stdin); at = 0; if (!len) return -1; }
            c = buf[at++];
        } while (c <= ' ');
        i64 x = 0;
        do {
            x = x * 10 + c - '0';
            if (at == len) { len = fread(buf, 1, B, stdin); at = 0; if (!len) break; }
            c = buf[at++];
        } while (c >= '0' && c <= '9');
        return x;
    }
};

struct Edge { int to, next; i64 w; };

int main() {
    FastInput in;
    int n = (int)in.next(); if (n < 0) return 0;
    int m = (int)in.next();
    int S = (int)in.next(), T = (int)in.next();
    int U = (int)in.next(), V = (int)in.next();
    vector<int> head(n + 1, -1);
    vector<Edge> edges; edges.reserve(2ull * m);
    auto addEdge = [&](int a, int b, i64 w) {
        edges.push_back({b, head[a], w}); head[a] = (int)edges.size() - 1;
    };
    for (int i = 0; i < m; ++i) {
        int a = (int)in.next(), b = (int)in.next(); i64 w = in.next();
        addEdge(a, b, w); addEdge(b, a, w);
    }
    auto dijkstra = [&](int src, vector<int>* popOrder = nullptr) {
        vector<i64> dist(n + 1, INF);
        priority_queue<pair<i64,int>, vector<pair<i64,int>>, greater<pair<i64,int>>> pq;
        dist[src] = 0; pq.push({0, src});
        while (!pq.empty()) {
            auto [d, a] = pq.top(); pq.pop();
            if (d != dist[a]) continue;
            if (popOrder) popOrder->push_back(a);
            for (int e = head[a]; e != -1; e = edges[e].next) {
                int b = edges[e].to; i64 w = edges[e].w;
                if (d > LLONG_MAX - w) continue;
                i64 nd = d + w;
                if (nd < dist[b]) { dist[b] = nd; pq.push({nd, b}); }
            }
        }
        return dist;
    };

    vector<int> order; order.reserve(n);
    vector<i64> ds = dijkstra(S, &order);
    vector<i64> du = dijkstra(U);
    i64 answer = du[V];
    if (ds[T] != INF) {
        vector<i64> dt = dijkstra(T);
        vector<i64> dv = dijkstra(V);
        vector<i64> best(n + 1, INF);
        for (int a : order) {
            if (dt[a] == INF || ds[a] > ds[T] - dt[a]) continue;
            if (du[a] < best[a]) best[a] = du[a];
            if (best[a] != INF && dv[a] != INF && best[a] <= LLONG_MAX - dv[a])
                answer = min(answer, best[a] + dv[a]);
            for (int e = head[a]; e != -1; e = edges[e].next) {
                int b = edges[e].to; i64 w = edges[e].w;
                if (ds[b] == INF || dt[b] == INF || ds[a] > LLONG_MAX - w) continue;
                if (ds[a] + w != ds[b] || ds[b] > ds[T] - dt[b]) continue;
                if (best[a] < best[b]) best[b] = best[a];
            }
        }
    }
    if (answer == INF) puts("-1"); else printf("%lld\n", answer);
}
