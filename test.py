import random
from questions import questions
from result import result
from play_round import play_round

# 퀴즈 진행 메인함수
def test():

    # 맞춘 문제와 틀린 문제 저장
    answered_correctly = []
    wrong = []

    while True:

    # 아직 풀지 않은 문제 목록 생성
        pool = []
        for item in questions:
            if item not in answered_correctly and item not in wrong:
                pool.append(item)

    # 틀린 문제와 새로운 문제가 모두 남아있는 경우
        if wrong and pool:
            while True:
                choice = input('\n틀린 문제를 재도전하시겠습니까, 새 문제를 푸시겠습니까? (w=틀린문제 / n=새문제): ')
                # 틀린 문제만 출제
                if choice.strip().lower() == 'w':
                    round_questions = wrong
                    break
                # 새로운 문제 출제
                elif choice.strip().lower() == 'n':
                    round_questions = random.sample(pool, min(3, len(pool)))
                    break
                else:
                    print('w 또는 n을 입력해주세요.')

    # 새 문제 없고, 틀린 문제만 있는 경우
        elif wrong:
            print('\n남은 새 문제가 없어 틀린 문제를 재도전합니다.\n')
            round_questions = wrong

    # 새 문제가 3개 미만이면 전체 문제 다시 사용
        else:
            if len(pool) < 3:
                print('\n모든 문제를 다 풀어서 전체 문제 중에서 다시 출제합니다.\n')
                pool = questions
            print('\n새 문제 3개를 출제합니다.\n')
            round_questions = random.sample(pool, 3)

    # 한 라운드 진행 후 점수와 틀린 문제 확인
        round_score, wrong = play_round(round_questions)
        round_count = len(round_questions)

    # 이번 라운드에서 맞춘 문제 저장
        correct_this_round = []
        for item in round_questions:
            if item not in wrong:
                correct_this_round.append(item)
        answered_correctly.extend(correct_this_round)

    # 이번 라운드 결과 출력
        result(round_score, round_count)

    # 게임 계속 진행할지 묻는 함수
        def ask_retry():
            while True:
                retry = input('\n다시 풀어보시겠습니까? (y/n): ')
                retry = retry.strip().lower()

                if retry == 'y' or retry == 'n':
                    return retry
                else:
                    print('y 또는 n을 입력해주세요.')

    # 게임 재시작 여부 확인
        retry = ask_retry()
        if retry != 'y':
            print('\n게임을 종료합니다.')
            break

