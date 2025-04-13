# 충북대학교 2학년 2022041022 이정환
#
# 2025년 3월 15일
#
#5명의 학생의 세개의 교과목 (영어, C-언어, 파이썬)에 대하여  키보드로부터 입력받아 총점, 평균, 학점, 등수를 계산하는 프로그램
#



# 학생 클래스
class student:
    def __init__(self,student_number,name,e_score,c_score,py_score,num):# 이름, 영어점수, c언어점수, pyton점수 학생번호를 받아 추가로 총점 평균 학점 계산하여 저장 
        self.num = num
        self.student_number = student_number
        self.name = name
        self.e_score = e_score
        self.c_score = c_score
        self.py_score = py_score
        self.total_score = self.e_score + self.c_score +self.py_score
        self.averge_score = int(round(self.total_score/3)) #round로 평균의 소수점은 반올림처리
        self.e_grade = grade_couting(e_score)#학점 확인
        self.c_grade = grade_couting(c_score)
        self.py_grade = grade_couting(py_score)
        
    def rank(self,ranked): #랭크를 저장하는 메소드
        self.ranked = ranked

    def grapic(self):#학생의 정보를 출력하는 메소드
        print("""
                    {}번 학생  이름 : {}
              
                                --  영어  --  c언어  --  pyton -- 
                    점수            {:<10} {:<10} {}
                    학점            {:<10} {:<10} {} 
              
              

                    총점 : {:<9}평균 : {:<9}등수 : {}"""\
              .format(self.num,self.name,self.e_score,self.c_score,self.py_score,self.e_grade,self.c_grade,self.py_grade,self.total_score,self.averge_score,self.ranked))




#학생수를 입력받아 이를 리턴하는 함수
def input_student(num):
    all_student = list()
    for i in range(num): #학생수만큼 입력받음
        print("\n",i+1,"번째 학생의 정보를 입력하시오.")
        all_student.append(student(score_input_and_test(input("학번 : "),),input("이름 : "),score_input_and_test(input("영어 점수는? : "),100),score_input_and_test(input("c언어 점수는? : "),100),score_input_and_test(input("pyton점수는? : "),100),i+1))
    return all_student





#점수와 학생수를 받아 순위를 리턴하는 함수
def rank_couting(s,num):

    for i in range(num):                                               
        temp=(s[i].total_score)
        r = 1#최소 1순위 이니 기본값을 1로 설정정
        for j in range(num):
            if temp < (s[j].total_score):
                r+=1
        s[i].rank(r)

    return s





#점수를 주면 학점을 리턴하는 함수
def grade_couting(s):
    if s>90:
            grade="A"
    elif s>80:
            grade="B"
    elif s>70:
            grade="c"
    elif s>60:
            grade="d"
    else:
            grade="F"
    return grade





#값과 값의 범위를 받아 확인 및 값을 다시 받는 함수
def score_input_and_test(s,num):
    while 1:
        #unsigedint 확인
        if(s.isdecimal()):
            s=int(s)
            #범위 확인
            if((s>=0)and(s<=num)):
                 break
            else:
                 print("오류! 입력된 숫자가 너무 많습니다 적정숫자: 0~",num," 다시 입력하시오.")    
        else:
            print("오류! 입력이 usiged int 자료형만 가능합니다. 다시 입력하시오.")
        s = input()
    return s



#메인
def main():
    import time
    S_NUM = 5 #학생 숫자
    stundent_information=input_student(S_NUM)# 학생 정보 입력
    stundent_information=rank_couting(stundent_information,S_NUM)#학생 순위 평가
    print("\n\n\n모든 정보가 기입되었습니다.\n\n\n")
    time.sleep(1)
    while(1): #정보 출력
        print("정보를 원하는 학생 번호를 말하시오. (1~{}) 종료는 0입니다.".format(S_NUM))
        i = score_input_and_test(input(),S_NUM)
        if(i==0):
            exit()
        else:
            stundent_information[int(i)-1].grapic()

main()