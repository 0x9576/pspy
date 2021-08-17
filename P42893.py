import re
import copy


def solution(word, pages):
    url_index = {}
    answer = []
    score = {}
    ref = {}
    word = word.lower()
    find_url = re.compile('<meta property="og:url" content="https://(.*)"/>')
    find_body = re.compile('<body>(.*)</body>', re.DOTALL)
    find_href = re.compile('<a href(\S*)</a>')
    find_link = re.compile('https://(.*)"')
    find_alpha = re.compile('([a-zA-Z]*)[^a-zA-Z]')
    word = word.lower()
    idx = 0

    for page in pages:
        url = find_url.search(page).group(1)
        url_index[url] = idx
        body = find_body.search(page).group(1)
        href_list = find_href.findall(body)
        link_list = []
        for href in href_list:
            link = find_link.search(href).group(1)
            link_list.append(link)
        body = body.lower()
        alpha_list = find_alpha.findall(body)
        score[url] = alpha_list.count(word)
        ref[url] = link_list
        idx += 1

    match_score = copy.deepcopy(score)

    for key in score:
        sc = score[key]
        lin_list = ref[key]
        for lin in lin_list:
            if lin in ref:
                match_score[lin] += score[key] / len(ref[key])
        answer.append(sc)

    ans_link = sorted(match_score.items(), key=lambda x: x[1], reverse=True)[0][0]
    return url_index[ans_link]