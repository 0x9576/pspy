def solution(phone_book):
    answer = True
    phone_book.sort(key=len,reverse = True)
    dic = {}
    for pb in phone_book:
        st = ""
        for ch in pb:
            st += ch
            if st in dic and len(st) == len(pb):
                answer = False
            if st not in dic:
                dic[st] = 1
    return answer