import re

def check(id):
    if '..' in id: return False
    pattern = '^[a-z0-9_-][a-z0-9_.-]+[a-z0-9_-]$'

    if re.search(pattern, id) == None:
        return False

    if not (len(id) <= 15 and len(id) >= 2): return False
    return True


def solution(new_id):
    if check(new_id): return new_id

    answer = new_id.lower()
    answer = re.sub('[^a-z0-9_.-]', '', answer)

    while '..' in answer:
        answer = answer.replace('..', '.')

    if answer:
        if len(answer) == 1 and answer[0] == '.':
            answer = ''
        else:
            if answer[0] == '.':
                answer = answer[1:]
            if answer[-1] == '.':
                answer = answer[:-1]

    if not answer: answer = 'a'

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    if len(answer) <= 2:
        while len(answer) <= 2:
            answer = answer + answer[-1]

    return answer