from collections import deque

def solution(cacheSize, cities):
    cities.lower()
    answer = 0
    cache = deque()
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        if city not in cache:
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(city)
            answer += 5
        else:
            del cache[cache.index(city)]
            cache.append(city)
            answer += 1
    return answer