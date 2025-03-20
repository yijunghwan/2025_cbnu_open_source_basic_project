import sys

def main():
    STUDENT_NUM = 5
    SUBJECTS_NUM = 3
    SUBJECTS_NAME=["영어","수학","ㅁㅁㅁ"]
    s=a(SUBJECTS_NUM,SUBJECTS_NAME)
    return 0


class a:
    def __init__(self,subject_num,subject_name):
        self.next = None
        #self.student_number = input_and_test(input("학번 : "),sys.maxsize)
        #self.name = input ("이름 : ")
        self.score= list()
        self.total_score = 0
        for i in range(subject_num):
            print(subject_name[i]," : ")
            self.score.append (input_and_test(input(),100))
            self.total_score += self.score[i] 
        self.averge_score = int(round(self.total_score/3)) #round로 평균의 소수점은 반올림처리
        print(self.total_score)
        #self.averge_grade = grade_couting(self.averge_grade)
        
class student:
    def __init__(self,subjects_num,subject_name):#학생 객체 기본정보
        self.next = None
        self.student_number = input_and_test(input("학번 : "),sys.maxsize)
        self.name = input ("이름 : ")
        self.score= list()
        self.total_score = 0
        for i in subject_name:
            print(subject_name[i]," : ")
            self.score.append (input_and_test(input(),100))
        #    self.total_score += self.score[i] 
        #self.averge_score = int(round(self.total_score/3)) #round로 평균의 소수점은 반올림처리
        #self.averge_grade = grade_couting(self.averge_grade)
    
    #def rank(self,s_h,h): #자기 자신과 링크드리스트의 헤더를 받아 순위를 메기는 메서드
        #self.ranked = rank_couting(s_h,h)

    #def grapic(self):
        #print("1")

#값과 값의 범위를 받아 확인 및 값을 다시 받는 함수
def input_and_test(s,num):
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

main()