import random
from question import q, questions

selected = random.sample(questions, 3)

score = 0
for question, answer in selected:
    if q(question, answer):
        score += 1

print(f'\n총 {len(selected)}문제 중 {score}문제 맞췄습니다.')


if score == len(selected):
    grade = 'A'
elif score >= len(selected) - 1:
    grade = 'B'
elif score >= 1:
    grade = 'C'
else:
    grade = 'F'

print(f'등급: {grade}')