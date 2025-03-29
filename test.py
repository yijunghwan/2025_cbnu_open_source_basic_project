import math

# 틱택토 보드 초기화
board = [' ' for _ in range(9)]

# 보드 출력 함수
def print_board():
    for row in [board[i:i + 3] for i in range(0, 9, 3)]:
        print('| ' + ' | '.join(row) + ' |')

# 승리 조건 확인 함수
def check_winner():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # 가로
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # 세로
        [0, 4, 8], [2, 4, 6]             # 대각선
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]
    return None

# Minimax 알고리즘
def minimax(is_maximizing):
    winner = check_winner()
    if winner == 'X':
        return -1
    elif winner == 'O':
        return 1
    elif ' ' not in board:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(best_score, score)
        return best_score

# AI의 최적 움직임 결정
def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

# 게임 시작
def play_game():
    print("틱택토: 당신은 X, AI는 O입니다.")
    print_board()

    while True:
        # 사용자 입력
        try:
            user_move = int(input("당신의 움직임 (0-8): "))
            if board[user_move] != ' ':
                print("이미 채워진 자리입니다. 다시 선택해주세요.")
                continue
            board[user_move] = 'X'
        except (ValueError, IndexError):
            print("유효하지 않은 입력입니다. 0에서 8 사이의 숫자를 입력해주세요.")
            continue

        print_board()

        # 승리 확인
        if check_winner() == 'X':
            print("축하합니다! 당신이 승리했습니다!")
            break
        if ' ' not in board:
            print("무승부입니다!")
            break

        # AI 움직임
        print("AI의 차례입니다...")
        ai_move()
        print_board()

        # 승리 확인
        if check_winner() == 'O':
            print("AI가 승리했습니다!")
            break
        if ' ' not in board:
            print("무승부입니다!")
            break

# 게임 실행
play_game()