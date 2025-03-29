# 충북대학교 2학년 2022041022 이정환
#
# 2025년 3월 23일
#
# 틱텍톡 게임(컴퓨터와 사람)
#
# - 입력 함수, 총점/평균 계산 함수,  학점계산 함수, 등수계산 함수, 출력 함수로 나누어 구현

import math
import os
import time
import sys

LEN = 3
play = titato(LEN)
while(1):
    print("현재 당신의 턴 입니다",end='')
    print("")
    play.grapic()
    play.human_turn(play)
    play.grapic()
    #play.ai_turn()
    print("현재 AI의 턴 입니다",end='')
    for i in range(3):
        time.sleep(0.5)
        print(".",end='')
        sys.stdout.flush()
    print("")

def c(x,y,len):
        if len < x or x < 0:
            return False
        if len < y or y < 0:
            return False
        return (x + y*len)

class titato :
    def __init__(self,LEN):
        self.map = [ ' ' for i in range(LEN*LEN) ]
        self.len = LEN
        self.win_len =LEN

    def ai_turn(self):#이 메소드를 부분은 Copilot을 사용함
        best_score = -math.inf
        move = None
        for i in range(9):
            if self.map[i] == ' ':
                self.map[i] = 'O'
                score = minimax(False)
                self.map[i] = ' '
                if score > best_score:
                    best_score = score
                    move = i
        self.map[move] = 'O'
        if(titato.check[move]):
            print("AI의 승리 입니다!")
            exit()

    def human_turn(self,map):
        i = int(input("원하는 위치를 말하시오"))
        self.map[i]='X'
        if (map.check(i)):
            print("당신의 승리 입니다!")
            exit()
        

    def check(self,position):
        print("0")
        x = position % len
        print("0")
        y = position / len
        print("0")
        len = self.len
        print("0")
        win_len =self.win_len
        print("1")
        #→← 승리 확인
        win_count = 1
        for i in range (1,win_len):
            if c(x+i,y,len) or (self.map(c(x,y)) != self.map(c(x+i,y))):
                for ii in range(1,win_len):
                    if c(x-ii,y,len) or (self.map(c(x,y)) != self.map(c(x-ii,y))):
                        break
                    win_conut +=1
                break        
            win_conut +=1
        if win_conut>=win_len:
            return 1
        print("2")
        #↑↓ 승리 확인
        win_count = 1
        for i in range (1,win_len):
            if c(x,y+i,len) or (self.map(c(x,y)) != self.map(c(x,y+i))):
                for ii in range(1,win_len):
                    if c(x,y-ii,len) or (self.map(c(x,y)) != self.map(c(x,y-ii))):
                        break
                    win_conut +=1
                break        
            win_conut +=1
        if win_conut>=win_len:
            return 1
        print("3")
        #↗↙ 승리 확인
        win_count = 1
        for i in range (1,win_len):
            if c(x+i,y+i,len) or (self.map(c(x,y)) != self.map(c(x+i,y+i))):
                for ii in range(1,win_len):
                    if c(x-ii,y-ii,len) or (self.map(c(x,y)) != self.map(c(x-ii,y-ii))):
                        break
                    win_conut +=1
                break        
            win_conut +=1
        if win_conut>=win_len:
            return 1
        print("4")
        #↖↘ 승리 확인
        win_count = 1
        for i in range (1,win_len):
            if c(x-i,y+i,len) or (self.map(c(x,y)) != self.map(c(x-i,y+i))):
                for ii in range(1,win_len):
                    if c(x+ii,y-ii,len) or (self.map(c(x,y)) != self.map(c(x+ii,y-ii))):
                        break
                    win_conut +=1
                break        
            win_conut +=1
        if win_conut>=win_len:
            return 1
        print("5")
        return 0

    def grapic(self):
        os.system('cls')

        for i in range(self.len):
            for ii in range(self.len):
                print(' | ',self.map[c(ii,i,self.len)],end=' ')
            print('| ')

    # Minimax 알고리즘
def minimax(is_maximizing):#이 메소드를 함수는 Copilot을 사용함
    """
    winner = check_winer()
    if winner == 'X':
        return -1
    elif winner == 'O':
        return 1
    elif ' ' not in play.map:
        return 0
"""
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if play.map[i] == ' ':
                play.map[i] = 'O'
                score = minimax(False)
                play.map[i] = ' '
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if play.map[i] == ' ':
                play.map[i] = 'X'
                score = minimax(True)
                play.map[i] = ' '
                best_score = min(best_score, score)
        return best_score


main()
