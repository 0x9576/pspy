import sys


def solution(n, s, a, b, fares):
    inf = sys.maxsize
    answer = inf
    dist = [[inf]*(n+1) for _ in range(n+1)]
    for fa in fares:
        dist[fa[0]][fa[1]] = fa[2]
        dist[fa[1]][fa[0]] = fa[2]
    for i in range(n+1):
        dist[i][i] = 0

    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

    for i in range(n+1):  # 같이 가는 곳이 i까지 라면
        answer = min(answer, dist[s][i] + dist[i][a] + dist[i][b])
    return answer