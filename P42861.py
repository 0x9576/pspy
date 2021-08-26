def solution(n, costs):
    costs.sort(key=lambda x: x[2], reverse=True)
    parent = [i for i in range(0, n)]
    print(costs)

    def find(a):
        if a != parent[a]:
            parent[a] = parent[a]
        return parent[a]

    def union(p, c):
        p = find(p)
        c = find(c)
        parent[c] = p
    answer = 0
    edge = 0
    while edge < n:
        u, v, wt = costs.pop()
        if find(u) != find(v):
            union(u, v)
            answer += wt
            edge += 1
    return answer