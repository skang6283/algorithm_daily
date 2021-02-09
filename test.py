import re
answer = input()
answer=answer.lower()
answer = re.sub('[^a-z0-9_.-]', '', answer)

print(answer)

