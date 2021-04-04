from collections import defaultdict
import re


def solution(word, pages):
    base_score = defaultdict(lambda: 0)
    incoming = defaultdict(list)
    external_score = defaultdict(lambda: 0)

    index = defaultdict()

    meta_regex = r'<meta[^>]*content="https://([\S]*)"/>'
    atag_regex = r'<a href="https://([\S]*)">'


    for i, page in enumerate(pages):
        self_link = re.search(meta_regex, page).group(1)
        for w in re.findall(r'[a-zA-Z]+',page.lower()):
            if word.lower() == w:
                base_score[self_link]+=1
        index[self_link] = i

        ref_links = re.findall(atag_regex, page)
        print(ref_links)
        for ref_link in ref_links:
            incoming[ref_link].append(self_link)
        external_score[self_link] = len(ref_links)

    big = 0
    answer = 0
    for link, i in index.items():
        link_score = 0
        for income in incoming[link]:
            link_score += (base_score[income] / external_score[income])
        total = base_score[link] + link_score
        if total > big:
            answer = i
            big = total


    return answer
a=["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://b.c./rerfdb\" test=\"dfgsfdqom\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
word='Muzi'
print(solution(word,a))