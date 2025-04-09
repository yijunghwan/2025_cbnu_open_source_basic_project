# 충북대학교 2학년 2022041022 이정환
#
# 2025년 3월 28일
#
# 틱텍톡 게임(컴퓨터와 사람)
#
# 


import math#ai 최적화 용도의 라이브러리
import os#cmd창 출력시 'cls'명령어 사용
import time#sleap함수 사용
import sys#버퍼 psuh 

LEN=3       #한변의 크기
WIN_LEN=3   #승리까지의 연속된 돌 수
board = [ ' ' for i in range(LEN*LEN) ] #1차원 리스트로 된 게임판

#메인함수
def main():
    print("안녕하세요 틱택토 게임입니다! 좌표는 제1사분면 기준입니다.(x가로축)(y세로축)")#간단 룰 설명
    set = input_and_test(input("난이도를 고르시오(easy 0 nomal 1 hard 2)"),2)#난이도 변수입력 (난이도변수 *2차례간 hard_ai함수 이후 esay_ai함수)
    start = input_and_test(input("선 후공을 고르시오(선공은 0 후공은 1)"),1)#선 후공 선택 변수 입력
    set *= 2#난이도변수 *2
    if (start):#선공시 ai 먼저
        ai_turn(set)
    turn = 0
    while True:
        grapic()#화면 출력
        human_turn()#사람 차례 함수
        print("현재 AI의 턴 입니다",end='')
        for i in range(4):#중간 구분용 그래픽(총 1.5초)
            time.sleep(0.5)
            print(".",end='')#\n이 없어 버퍼에 쌓임
            sys.stdout.flush()#버퍼 push
        print("")#줄 바꿈 출력
        ai_turn(set)
        set -=1#난이도 조정
       


#오류확인 함수
def input_and_test(s,num):#입력값,범위 를 입력받아 확인하는 함수
    while 1:
        if(s.isdecimal()):#unsigedint 확인
            s=int(s)
            if((s>=0)and(s<=num)):#범위 확인
                 break
            else:
                 print("오류! 입력된 숫자가 너무 많습니다 적정숫자: 0~",num," 다시 입력하시오.")    
        else:
            print("오류! 입력이 usiged int 자료형만 가능합니다. 다시 입력하시오.")
        s = input()
    return s


#사람 차례의 돌을 두는 함수
def human_turn():#
    while True:
        x = input_and_test(input("다음 수의 X좌표를 입력하시오: "),LEN-1)#x좌표 입력
        y = input_and_test(input("다음 수의 y좌표를 입력하시오: "),LEN-1)#y좌표 입력
        if board [c(x,y)] != ' ':   #기존 돌 여부 확인 있다면 contiune
            print("이미 돌이 있습니다! 다시 해주세요!")
            continue
        board [c(x,y)] = 'X'
        break
    # 승리 확인
    grapic()
    if check(c(x,y)) == 'X':
        print("축하합니다! 당신이 승리했습니다!")
        exit()
    if ' ' not in board:
        print("무승부입니다!")
        exit()

#좌표 걔산함수
def c(x,y):# 2차원을 1차원으로 바꿔주는 함수
        len = LEN
        
        return int(x) + int(y)*len

#좌표 확인 함수
def map_out(x,y):#board함수의 범위를 넘은 인덱스 값인지 확인
    len = LEN
    if (len-1) < x or x < 0:
        return True
    if (len-1) < y or y < 0:
        return True
    return False

#출력함수
def grapic():
    os.system('cls')
    for i in range(LEN):
        for ii in range(LEN):
            print(' |',board[c(ii,LEN-(i+1))],end='')
        print('| ')

#승리 확인함수
def check(position):#직전에 입력한 돌위치 중심으로 빙고 파악
        len=LEN#한 변의 길이
        x = position % len#직전에 입력한 돌위치를2차원 좌표로 변경 x값(가로)
        y = int(position / len)#직전에 입력한 돌위치를2차원 좌표로 변경 y값(세로)
        win_len =WIN_LEN

        #→← 승리 확인
        win_conut = 1
        for i in range (1,win_len):
            if map_out(x+i,y) or (board[c(x,y)] != board[c(x+i,y)]):#→확인
                for ii in range(1,win_len):
                    if map_out(x-ii,y) or (board[c(x,y)] != board[c(x-ii,y)]):#←확인
                        break#두방향 전부 연속되지 않았다면 탈출
                    win_conut +=1#연속된 돌이 있다면 +1
                break       
            win_conut +=1#연속된 돌이 있다면 +1
        if win_conut>=win_len:#연속된 돌 수 확인
            return board[position]#승리한 돌 리턴

        #↑↓ 승리 확인
        win_conut = 1
        for i in range (1,win_len):
            if map_out(x,y+i) or (board[c(x,y)] != board[c(x,y+i)]):
                for ii in range(1,win_len):
                    if map_out(x,y-ii) or (board[c(x,y)] != board[c(x,y-ii)]):
                        break
                    win_conut +=1
                break        
            win_conut +=1
        if win_conut>=win_len:
            return board[position]

        #↗↙ 승리 확인
        win_conut = 1
        for i in range (1,win_len):
            if map_out(x+i,y+i) or (board[c(x,y)] != board[c(x+i,y+i)]):
                for ii in range(1,win_len):
                    if map_out(x-ii,y-ii) or (board[c(x,y)] != board[c(x-ii,y-ii)]):
                        break
                    win_conut +=1
                break        
            win_conut +=1
        if win_conut>=win_len:
            return board[position]
        
        #↖↘ 승리 확인
        win_conut = 1
        for i in range (1,win_len):
            if map_out(x-i,y+i) or (board[c(x,y)] != board[c(x-i,y+i)]):
                for ii in range(1,win_len):
                    if map_out(x+ii,y-ii) or (board[c(x,y)] != board[c(x+ii,y-ii)]):
                        break
                    win_conut +=1
                break        
            win_conut +=1
        if win_conut>=win_len:
            return board[position]
        return 0

#저 수준 ai 함수
def ai_easy(i):#수를 입력받아 가중치를 리턴
    len = LEN
    winner = check(i)
    if winner == 'O':#이기는 수 라면 가중치 3
        return 3
    elif i == c((LEN/2),(LEN/2)):#정 가운데는 가중치 2
        return 2
    elif i == 0 or i == c(len-1,len-1) or i == c(0,len-1) or i == c(len-1,0) :#모서리는 가중치 1
        return 1
    else:#나머지는 가중치 0
        return 0

    


#아래 두 함수(minimax,ai_turn)는 생성형 AI를 사용하여 만들었으며 일부 수정함
# Minimax 알고리즘
def minimax(is_maximizing,ii):
    winner = check(ii)
    if winner == 'X':
        return -1
    elif winner == 'O':
        return 1
    elif ' ' not in board:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(LEN*LEN):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False,i)
                board[i] = ' '
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(LEN*LEN):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True,i)
                board[i] = ' '
                best_score = min(best_score, score)
        return best_score

# AI의 최적 움직임 결정
def ai_turn(level):
    best_score = -math.inf
    move = None
    if level > 0:#추가 구문 (ai 수준 구분)
        for i in range(LEN*LEN):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False,i)
                board[i] = ' '
                if score > best_score:
                    best_score = score
                    move = i
    else:#추가 구문
        best_score = 0
        for i in range(LEN*LEN):
            if board[i] == ' ':
                board[i] = 'O'
                score = ai_easy(i)#쉬운 ai logic
                board[i] = ' '
                if score > best_score: 
                    best_score = score
                    move = i

    board[move] = 'O'
    # 승리 확인
    if check(move) == 'O':
        grapic()
        print("AI가 승리했습니다!")
        exit()
    if ' ' not in board:
        grapic()
        print("무승부입니다!")
        exit() 


main()
