# 충북대학교 2학년 2022041022 이정환
#
# 2025년 3월 30일
#
#- 성적관리프로그램
#
# 조건: 5명의 학생의 세개의 교과목 (영어, C-언어, 파이썬)에 대하여 
#
#         키보드로부터 학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 입력받아 총점, 평균, 학점, 등수를 계산하는 프로그램 작성
#
#       - 입력 함수, 총점/평균 계산 함수,  학점계산 함수, 등수계산 함수, 출력 함수 
#
#       - 삽입 함수, 삭제 함수, 탐색함수(학번, 이름), 정렬(총점)함수, 80점이상 학생 수 카운트 함수

import os
import time
import sys

def main():
    menu(menu_start())

def menu(all):
    set = True
    while set:
        print("현재 학생 수:",all.num)
        set = input_and_test(input("""
                            0:종료
                            1:학생 정보 수정
                            2:학생 정보 출력
                            """),3)
        if 0 == set:
            print("정상종료")
            return 0
        elif 1 == set:
            all.student_in(all)
        elif 2 == set:
            all.student_print(all)
        else:
             print("비정상 종료 코드 1")
             return 1
    print("비정상 종료 코드 2")
    return 2


def menu_start():
    set = True
    student_num = 1
    subject_name = ["수학"]#["영어","C_언어","Python"]
    while set:
        os.system('cls')
        print("초기 학생정보를 입력하시요")
        print("현재 설정값")
        print("초기입력 학생수 : ",student_num)
        print("초기 입력 과목 : ",subject_name)
        set = input_and_test(input("""
                            0:종료
                            1:초기 학생 정보 입력
                            2:초기 입력학생 수 수정(기본값: 5)
                            3:기본 입력 과목 수정 (기본값: 영어 c언어 python 3개)
                            """),3)
        if 0 == set:
             print("정상종료")
             exit()
        elif 1 == set:
            all = student_linked_list(subject_name)
            for i in range(student_num-1):
                all.in_append()
            return all
        elif 2 == set:
            print("0은 뒤로가기")
            num = input_and_test(input("초기 입력 학생수를 적으시오 : "),sys.maxsize)
            if (num == 0):
                continue
            student_num = num
        elif 3 == set:
            print("0은 뒤로가기")
            num = input_and_test(input("원하는 과목수를 적으시오 : "),sys.maxsize)
            if (num == 0):
                continue
            subject_num = num
            new_subject_name=list()
            for i in range (subject_num):
                print(i+1,"번째 과목이름")
                new_subject_name.append(input())
            subject_name =new_subject_name
        else:
             print("비정상 종료 코드 1")
             return 1
    print("비정상 종료 코드 2")
    return 2
     


#학생 객체 클래스
class student:

    #매개 변수 subject_num : 과목수 subject_name : 과목명
    def __init__(self,subject_name):#과목수 과목 이름을 받아 객체 생성시 기본정보(학점, 이름, 점수)를 입력받으며 총점/평균/평점(추가 함수 이용) 계산 및 저장
        self.next = None
        self.subject_name = subject_name
        self.student_number = input_and_test(input("학번 : "),sys.maxsize)
        self.name = input ("이름 : ")
        self.score= list()
        self.total_score = 0
        for i in subject_name:#과목 수 만큼 점수 입력
            print(i,":",end=" ")
            self.score.append (input_and_test(input(),100))
            self.total_score += self.score[-1]
        self.averge_score = int(round(self.total_score/len(self.subject_name))) # 평균 계산  (round 함수로 평균의 소수점은 반올림처리)
        self.averge_grade = grade_couting(self.averge_score)
    
    #매개 변수 s_h: 헤드 노드 h:순위 측정 대상 노드
    def rank(self,ranked): #자기 자신과 헤더 노드를 받아 순위를 메기는 메서드
        self.ranked = ranked


    def grapic(self): #정보를 출력하는 메서드
        print("""
------------------------------------------------------
학번:{} 이름:{}""".format(self.student_number,self.name))
        for i in self.subject_name:
            print(i,":",end='')
            for ii in range(len(self.subject_name)):
                print(self.score[ii])
        print("""총점:{}
평균:{}
학점:{}
등수:{}
------------------------------------------------------
""".format(self.total_score,self.averge_score,self.averge_grade,self.ranked))


#학생 객체 링크드 리스트
class student_linked_list:

    #매개변수 subject_num : 과목수 subject_name : 과목명
    def __init__(self,subject_name):#첫 학생 객체 생성(헤드 노드)
        print("1 번째 학생 입력")
        self.head = student(subject_name)# 학생 객체 생성
        self.num = 1
        self.subject_name = subject_name


    def student_in(self,linked_list):
        print_student = self.head
        set = True
        while set:
            print("현재 총 학생 수:",self.num,"\n\n")
            set = input_and_test(input("""
                                0:입력 종료
                                1:학생추가
                                2:특정 학생 삽입(그 이후 학생은 번호가 1씩 밀림니다!)
                                3:특정 학생 삭제
                                4:입력 과목 변경
                                """),4)
            if 0 == set:
                print("출력 메뉴 정상 종료")
                return 0
            elif 1 == set:
                linked_list.in_append()
            elif 2 == set:
                print("취소는 0")
                linked_list.in_push(input_and_test(input("삽입 번호를 말하세요(그 이후 학생은 번호가 1씩 밀림니다!)"),self.num))
            elif 3 == set:
                print("취소는 0")
                linked_list.in_pop(input_and_test(input("정보를 삭제할 학생의 번호를 말하세요"),self.num))
            elif 4 == set:
                print("취소는 0")
                linked_list.in_subject_change(input_and_test(input("원하는 과목수를 적으시오 : "),sys.maxsize))
            else:
                print("비정상 출력 메뉴 종료 코드3")
                return 3
        print("비정상 출력 메뉴 종료 코드4")
        return 4


    #매개변수 subject_num : 과목수 subject_name : 과목명
    def in_append(self):#추가 학생 객체 생성 메서드
        last_student = self.head# 헤드 노드 부터 시작
        while 1:#마지막 학생객체로 넘어가기 위한 반복문
            if last_student.next == None:#마지막 학생인지 확인
                break
            last_student = last_student.next# 아니라면 다음 객체로 넘어가기
        print(self.num+1,"번째 학생의 정보를 입력하세요!(가장 뒷번호로 설정)")
        last_student.next = student(self.subject_name)#마지막 학생객체에서 추가 객체 생성
        self.num += 1
        print(self.num,"번째 학생의 정보가 추가되었습니다")


    #매개변수 s_num:삭제할 학생번호
    def in_pop(self,s_num):#학생 번호를 입력받아 입력받은 학생 정보 삭제  !!!입력시 노드 오버 문제주의
        temp=self.head
        pop_node = None
        if s_num == 0:
             return 0
        if s_num == 1:
            self.head=self.head.next
        else:
            for i in range(s_num-2):
                temp = temp.next
            del_pop = temp.next
            temp = temp.next.next
            del pop_node
        self.num -= 1
        print(s_num,"번째 학생의 정보는 삭제되었습니다!")


        #매개변수 s_num:삽입 학생번호
    

    #매개변수 s_num:삽입될 학생 정보의 위치
    def in_push(self,s_num):#학생 번호를 입력받아 입력받은 학생 정보 삽입 !!!입력시 노드 오버 문제주의
        temp=self.head
        if s_num == 0:
             return 0
        print("삽입할 학생의 정보를 입력하세요")
        push_node = student(self.subject_name)
        if s_num == 1:
            push_node.next = self.head
            self.head =push_node
        else:
            for i in range(s_num-2):
                temp = temp.next
            push_node.next = temp.next
            temp.next=push_node
        self.num += 1
        print(s_num,"번째 학생의 정보가 삽입 되었습니다!(뒤 학생의 번호는 전부 밀렸습니다!)")



    def in_subject_change(self,subject_num):
        if subject_num == 0:
            return 0
        new_subject_name=list()
        for i in range (subject_num):
            print(i+1,"번째 과목이름")
            new_subject_name.append(input())
        self.subject_name = new_subject_name




    def all_stundent_rank_counting(self):#모든 학생 순위 메기는 메서드 
        rank_couting_student = self.head
        temp_s = self.head#임시 노드 생성 (헤더노드부터 시작)
        while 1:
            r = 1#최소 1순위 이니 기본값을 1로 설정
            while 1:
                if (rank_couting_student.total_score < temp_s.total_score):#순위를 측정할 노드에 임시 헤더를 비교
                    r+=1
                if temp_s.next == None:# 임시 노드가 마지막 인지 확인 마지막일경우 반복문 탈출
                        break
                else:
                    temp_s=temp_s.next#아니라면 임시 노드를 다음 노드으로 넘어가기
            rank_couting_student.rank(r)#학생 객체의 순위 계산 메서드
            if (rank_couting_student.next!=None):
                rank_couting_student = rank_couting_student.next
            else :
                break
        return 0


    def student_print(self,linked_list):
        print_student = self.head
        set = True
        linked_list.all_stundent_rank_counting()
        while set:
            print("현재 총 학생 수:",self.num,"\n\n")
            set = input_and_test(input("""
                                0:출력 종료
                                1:특정 학생 정보 출력
                                2:모든 학생 정보 출력
                                3:학생 이름 검색
                                4:학생 학번 검색
                                5:학생 평균 80점 이상 학생수 검색 
                                """),5)
            if 0 == set:
                print("출력 메뉴 정상 종료")
                return 0
            elif 1 == set:
                print("뒤로가기는 0")
                i = input_and_test(input("정보를 원하는 학생 번호를 말하시오.(학생번호는 1번부터 시작합니다)"),self.num)
                if i == 0:
                    continue
                linked_list.print_num(i)
            elif 2 == set:
                linked_list.print_all()
            elif 3 == set:
                print("뒤로가기는 0")
                linked_list.print_find_name(input("찾을 학생의 이름을 입력하세요:"),linked_list)
            elif 4 == set:
                linked_list.print_find_number(input_and_test(input("찾을 학생의 학번을 입력하세요:"),sys.maxsize),linked_list)
            elif 5 == set:
                linked_list.print_counting_b()
            else:
                print("비정상 출력 메뉴 종료 코드3")
                return 3
        print("비정상 출력 메뉴 종료 코드4")
        return 4



    def print_num(self,num):# 특정 번호의 학생정보 출력 !!!입력시 노드 오버 문제주의
        temp = self.head
        for i in range(num-1):
            temp = temp.next
        print(num,"번째 학생 정보",end='')
        temp.grapic()


    def print_all(self):
        last_student = self.head# 헤드 노드 부터 시작
        s_num = 1
        while 1:#마지막 노드로 넘어가기 위한 반복문
            print(s_num,"번째 학생 정보",end='')
            last_student.grapic()
            if last_student.next == None:#마지막 노드인지 확인
                break
            s_num +=1
            last_student = last_student.next# 아니라면 다음 노드로 넘어가기


    def print_counting_b(self):
        last_student = self.head# 헤드 노드 부터 시작
        i = 0
        while 1:#마지막 학생객체로 넘어가기 위한 반복문
            if last_student.averge_score >= 80:
                 i+=1
            if last_student.next == None:#마지막 학생인지 확인
                print(i,"만큼의 학생의 점수가 80점(B학점)이상입니다.")
                break
            last_student = last_student.next# 아니라면 다음 객체로 넘어가기  

       
    def print_find_number(self,number,linked_list):
        last_student = self.head# 헤드 노드 부터 시작
        num = 1
        while 1:#마지막 학생객체로 넘어가기 위한 반복문
            if last_student.student_number == number:
                print(num,"번째 학생이 이 학번을 가지고 있습니다. 정보를 출력하시겠습니까?")
                i = input_and_test(input("""
                                         아니요 : 0
                                         예 : 1
                                         """),1)
                if i:
                    linked_list.print_num(num)
            if last_student.next == None:#마지막 학생인지 확인
                print("더 이상 학생이 없습니다!")
                break
            num += 1
            last_student = last_student.next# 아니라면 다음 객체로 넘어가기


    def print_find_name(self,name,linked_list):
        last_student = self.head# 헤드 노드 부터 시작
        num = 1
        while 1:#마지막 학생객체로 넘어가기 위한 반복문
            if last_student.name == name:
                print(num,"번째 학생이 이 이름을 가지고 있습니다. 정보를 출력하시겠습니까?")
                i = input_and_test(input("""
                                         아니요 : 0
                                         예 : 1
                                         """),1)
                if i:
                    linked_list.print_num(num)
            if last_student.next == None:#마지막 학생인지 확인
                print("더 이상 학생이 없습니다!")
                break
            num += 1
            last_student = last_student.next# 아니라면 다음 객체로 넘어가기



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

main()