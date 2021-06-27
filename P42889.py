def solution(N, stages):
    answer = []
    num = [0] * 502
    d = [0] * 502
    fail = [0.0] * 502
    tfail = []
    for s in stages:
        for i in range (1,s+1):
            num[i] +=1
        d[s] += 1
    for i in range(0, N + 1):
        if num[i] == 0:
            fail[i] = 0
            continue
        fail[i] = d[i]/num[i]
    for i in range (1,N+1):
        tfail.append((fail[i],i))
    tfail.sort(key= lambda x : -x[0])
    for t in tfail:
        answer.append(t[1])
    return answer