from questions import q

# 한 라운드 끝난 후 점수랑 틀린 문제 반환하는 함수
def play_round(question_list):
    wrong = []
    score = 0

    for question, answer in question_list:

# 정답이면 점수 증가
        if q(question, answer):
            score += 1

# 오답이면 재도전 위해 저장
        else:
            wrong.append((question, answer))

    return score, wrong