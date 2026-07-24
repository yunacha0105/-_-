# 결과 출력 함수

def result(score, total):
    print(f'\n총 {total}문제 중 {score}문제 맞췄습니다.')

    if score == total:
        grade = 'A'
        message = '최고에요! '
    elif score >= total - 1:
        grade = 'B'
        message = '좋아요! '
    elif score >= 1:
        grade = 'C'
        message = '오,, '
    else:
        grade = 'F'
        message = '분발하세요! '

    print(f'{message}당신은 {grade} 등급입니다.')