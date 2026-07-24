import random
from question import q, questions
from show_grade import show_grade

def play_round(question_list):
    wrong = []
    score = 0

    for question, answer in question_list:
        if q(question, answer):
            score += 1
        else:
            wrong.append((question, answer))

    return score, wrong


def test():
    answered_correctly = []   # 지금까지 맞춘 문제 누적
    wrong = []                 # 직전 라운드에서 틀린 문제

    while True:
        pool = []
        for item in questions:
            if item not in answered_correctly and item not in wrong:
                pool.append(item)

        if wrong and pool:
            # 틀린 문제도 있고, 아직 안 나온 새 문제도 있는 경우 → 선택
            choice = input('\n틀린 문제를 재도전하시겠습니까, 새 문제를 푸시겠습니까? (w=틀린문제 / n=새문제): ')
            if choice.strip().lower() == 'w':
                round_questions = wrong
            else:
                round_questions = random.sample(pool, min(3, len(pool)))
        elif wrong:
            # 새로 낼 문제가 없으면 틀린 문제로 자동 진행
            print('\n남은 새 문제가 없어 틀린 문제를 재도전합니다.\n')
            round_questions = wrong
        else:
            # 틀린 문제가 없으면 새 문제로 진행 (다 풀었으면 전체에서 다시)
            if len(pool) < 3:
                print('\n모든 문제를 다 풀어서 전체 문제 중에서 다시 출제합니다.\n')
                pool = questions
            print('\n새 문제 3개를 출제합니다.\n')
            round_questions = random.sample(pool, 3)

        round_score, wrong = play_round(round_questions)
        round_count = len(round_questions)

        correct_this_round = []
        for item in round_questions:
            if item not in wrong:
                correct_this_round.append(item)
        answered_correctly.extend(correct_this_round)

        show_grade(round_score, round_count)

        retry = input('\n다시 풀어보시겠습니까? (y/n): ')
        if retry.strip().lower() != 'y':
            break

    print('\n게임을 종료합니다.')