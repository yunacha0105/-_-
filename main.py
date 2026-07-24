from test import test

attendance = input('''리눅스 시험을 시작합니다.
참가하시겠습니까? y / n : ''')
while True:
    if attendance == 'y':
        test()
        break
    elif attendance == 'n':
        print('시험을 종료합니다.')
        break
    else:
        print('잘못입력하셨습니다')
        attendance = input('참가하시겠습니까? y / n : ')