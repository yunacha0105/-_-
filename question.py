def q(question, answer):
    print(question)

    user_input = input('답: ')

    if user_input.strip().casefold() == answer.casefold():
        print('정답입니다!')
        return True
    else:
        print(f"오답입니다. 정답은 {answer}입니다.")
        return False


questions = [
    ('이전에 입력했던 명령어 목록을 확인할 때 사용하는 명령어는?', 'history'),
    ('현재 접속해있는 사용자가 누구인지 알아내는 명령어는?', 'whoami'),
    ('새로운 사용자 계정을 추가할 때 사용하는 명령어는?', 'adduser'),
    ('사용자의 비밀번호를 설정/변경할 때 사용하는 명령어는?', 'passwd'),
    ('파일이나 디렉토리의 권한을 변경할 때 사용하는 명령어는?', 'chmod'),
    ('상위 폴더로 가기 위해 입력해야하는 명령어는?', 'cd ..'),
    ('파일의 수정일자를 업데이트하고, 없으면 만들기도 하는 명령어는?', 'touch'),
    ('디렉토리를 만드는 명령어는?', 'mkdir'),
    ('vi를 통해 파일을 열어 수정한 뒤 저장하지 않고 나가려면 입력해야하는 명령어는?', ':q!'),
]