def show_grade(score, total):
    print(f'\n총 {total}문제 중 {score}문제 맞췄습니다.')

    if score == total:
        grade = 'A'
    elif score >= total - 1:
        grade = 'B'
    elif score >= 1:
        grade = 'C'
    else:
        grade = 'F'

    print(f'등급: {grade}')