# 충북대학교 2학년 2022041022 이정환
#
# 2025년 3월 23일
#
#5명의 학생의 세개의 교과목 (영어, C-언어, 파이썬)에 대하여  키보드로부터 입력받아 총점, 평균, 학점, 등수를 계산하는 프로그램
#
# - 입력 함수, 총점/평균 계산 함수,  학점계산 함수, 등수계산 함수, 출력 함수로 나누어 구현



import sys#정수 입력 최대값을 구하기위해 사용 34번째줄 코드 확인


#메인 함수
def main():
    STUDENT_NUM = 5#학생수
    SUBJECT_NUM = 3#과목수
    SUBJECT_NAME=("영어","C-언어","python")#과목명
    if(STUDENT_NUM>0):#헤더 노드 생성
        student_head = student_linked_list(SUBJECT_NUM,SUBJECT_NAME)
    input_information(STUDENT_NUM,SUBJECT_NUM,SUBJECT_NAME,student_head)#추가 노드 생성
    student_head.all_stundent_rank_counting()#전 노드(학생 객체) 순위 계산
    student_head.all_print_stundent_information()#전 노드 (학생 객체) 정보 출력




#학생 객체 클래스
class student:

    #매개 변수 subject_num : 과목수 subject_name : 과목명
    def __init__(self,subject_num,subject_name):#과목수 과목 이름을 받아 객체 생성시 기본정보(학점, 이름, 점수)를 입력받으며 총점/평균/평점(추가 함수 이용) 계산 및 저장
        self.next = None
        self.student_number = input_and_test(input("학번 : "),sys.maxsize)
        self.name = input ("이름 : ")
        self.score= list()
        self.total_score = 0
        for i in range(subject_num):#과목 수 만큼 점수 입력
            print(subject_name[i],":",end=" ")
            self.score.append (input_and_test(input(),100))
            self.total_score += self.score[i]
        self.averge_score = int(round(self.total_score/3)) # 평균 계산  (round 함수로 평균의 소수점은 반올림처리)
        self.averge_grade = grade_couting(self.averge_score)
        print("\n")
    
    #매개 변수 s_h: 헤드 노드 h:순위 측정 대상 노드
    def rank(self,s_h,h): #자기 자신과 헤더 노드를 받아 순위를 메기는 메서드
        self.ranked = rank_couting(s_h,h)#순위 측정 함수


    def grapic(self): #정보를 출력하는 메서드
        print("""
============================================================================================================================

{:<20}{:<15}{:>10}        {:<10}{:<10}{:<10}{:<10}{:<10}{} 

============================================================================================================================

{:<20}{:<15}{:>10}        {:<10}{:<10}{:<10}{:<10}{:<10}{} 
              

""".format("학번","이름","영어","c-언어","python","총점","평균","학점","등수",self.student_number,self.name,self.score[0],self.score[1],self.score[2],self.total_score,self.averge_score,self.averge_grade,self.ranked))



#학생 객체 링크드 리스트
class student_linked_list:

    #매개변수 subject_num : 과목수 subject_name : 과목명
    def __init__(self,subject_num,subject_name):#첫 학생 객체 생성(헤드 노드)
        self.head = student(subject_num,subject_name)# 학생 객체 생성

    #매개변수 subject_num : 과목수 subject_name : 과목명
    def new_student_append(self,subject_num,subject_name):#추가 학생 객체 생성 메서드
        last_student = self.head# 헤드 노드 부터 시작
        
        while 1:#마지막 학생객체로 넘어가기 위한 반복문
            if last_student.next == None:#마지막 학생인지 확인
                break
            last_student = last_student.next# 아니라면 다음 객체로 넘어가기

        last_student.next = student(subject_num,subject_name)#마지막 학생객체에서 추가 객체 생성


    def all_stundent_rank_counting(self):#모든 학생 순위 메기는 메서드
        rank_couting_student = self.head
        while 1:
            rank_couting_student.rank(self.head,rank_couting_student)#학생 객체의 순위 계산 메서드
            if (rank_couting_student.next!=None):
                rank_couting_student = rank_couting_student.next
            else :
                break
        return 0


    def all_print_stundent_information(self):#모든 학생 객체에서 정보를 출력하는 메서드
        print_student = self.head
        while 1:
            print_student.grapic()
            if (print_student.next!=None):
                print_student = print_student.next
            else :
                break
        return 0





#학생수 과목수 과목이름을 받아 원하는 학생수 만큼 추가하는 함수
#입력 함수
#매개변수 student_num : 학생수 subject_num : 과목수 subject_name : 과목명 s : 헤더 노드
def input_information(student_num,subject_num,subject_name,s):
    for i in range(student_num-1):#위에서 헤더노드는 이미 생성했기에 -1 
         s.new_student_append(subject_num,subject_name)
    return 0




#헤드 노드와 순위를 측정할 노드를 받아 순위를 리턴하는 함수
#매개변수 s_h:헤더 노드 s:순위를 측정할 노드
def rank_couting(s_h,s):

    temp_s = s_h #임시 노드 생성 (헤더노드부터 시작)
    r = 1#최소 1순위 이니 기본값을 1로 설정
    while 1:
        if (s.total_score < temp_s.total_score):#순위를 측정할 노드에 임시 헤더를 비교
            r+=1
        if temp_s.next == None:# 임시 노드가 마지막 인지 확인 마지막일경우 반복문 탈출
                break
        else:
                temp_s=temp_s.next#아니라면 임시 노드를 다음 노드으로 넘어가기
    return r




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