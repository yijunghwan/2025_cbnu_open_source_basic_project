
import sys
import os
import time
#메인 함수
def main():
    student_num = 5#학생수
    set = True
    check = False
    while set:
        os.system('cls')
        print("현재 학생 수:",student_num)
        print("학생 정보입력 여부 : ",check)
        set = input_and_test(input("""
                            0:종료
                            1:학생정보 입력
                            2:학생 정보 출력
                            3:학생 수 조정(기본값: 5명)
                            4:학생 정보 수정
                            4:과목 조정 (기본값: 영어 c언어 python 3개)
                            """),4)
        os.system('cls')
        if 0 == set:
             print("정상종료")
             return 0
        elif 1 == set:
              student_all = list (student(i) for i in range(student_num))
              rank_couting(student_all,student_num)
              check = True
        elif 2 == set :
            if check == False:
                print("아직 학생 정보가 입력되지 않았습니다!")
                time.sleep(2)
                continue
              
            student_output(student_all,student_num)
        elif 3 == set:
              student_num = input_and_test(input("학생수를 적으시오 : "),sys.maxsize)
        elif 4 == set:
              subject_num = input_and_test(input("원하는 과목수를 적으시오 : "),sys.maxsize)
              subject_name=list()
              for i in range (subject_num):
                subject_name.append(input(i,"번째 과목이름 : "))
        else:
             print("비정상 종료 코드 1")
             return 1
    print("비정상 종료 코드 2")
    return 2




#학생 객체 클래스
class student:

    #매개 변수 subject_num : 과목수 subject_name : 과목명
    def __init__(self,num,subject_name = ("영어","C-언어","python")):#과목수 과목 이름을 받아 객체 생성시 기본정보(학점, 이름, 점수)를 입력받으며 총점/평균/평점(추가 함수 이용) 계산 및 저장\
        self.student_number = input_and_test(input("학번 : "),sys.maxsize)
        self.name = input ("이름 : ")
        self.score= list()
        self.total_score = 0
        for i in subject_name:#과목 수 만큼 점수 입력
            print(i,":",end=" ")
            self.score.append (input_and_test(input(),100))
            self.total_score += self.score[-1]
        self.averge_score = int(round(self.total_score/3)) # 평균 계산  (round 함수로 평균의 소수점은 반올림처리)
        self.averge_grade = grade_couting(self.averge_score)

    def rank(self,ranked): #랭크를 저장하는 메소드
        self.ranked = ranked

    def grapic(self): #정보를 출력하는 메서드
        print("""이름 {}""")



#값과 값의 범위를 받아 값이 정수인지 조건에 부합하는지 확인후 부합할 때까지 값을 다시 받는 함수
#오류 방지 함수
#매개변수 s:입력할 값 num : 값의 범위 
def input_and_test(s,num):
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




#점수를 주면 학점을 리턴하는 함수
#학점 평가 함수
#매개 변수 s : 평가 할 점수
def grade_couting(s):
    if s>95:
            grade="A+"
    elif s>90:
            grade="A"
    elif s>85:
            grade="B+"
    elif s>80:
            grade="B"
    elif s>75:
            grade="C+"
    elif s>70:
            grade="C"
    elif s>65:
            grade="D+"
    elif s>60:
            grade="D"
    else:
            grade="F"
    return grade


def rank_couting(s,num):

    for i in range(num):                                               
        temp=(s[i].total_score)
        r = 1#최소 1순위 이니 기본값을 1로 설정정
        for j in range(num):
            if temp < (s[j].total_score):
                r+=1
        s[i].rank(r)

    return s

def student_output(s,num):
    set = True
    os.system('cls')
    while set:
        print("현재 총 학생 수:",num,"\n\n")
        set = input_and_test(input("""
                            0:출력 종료
                            1:특정 학생 정보 출력
                            2:모든 학생 정보 출력
                            """),2)
        os.system('cls')
        if 0 == set:
             print("출력 메뉴 정상 종료")
             return 0
        elif 1 == set:
            i = input_and_test(input("정보를 원하는 학생 번호를 말하시오.(학생번호는 0번부터 시작합니다)"),num - 1)
            s[i].grapic()
        elif 2 == set:
            for i in range(num):
                 s[i].grapic()
        else:
            print("비정상 출력 메뉴 종료 코드3")
            return 3
    print("비정상 출력 메뉴 종료 코드4")
    return 4

             
     

main()