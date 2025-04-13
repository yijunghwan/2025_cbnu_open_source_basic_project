
import random

# 텍스트 파일 생성
with open("input_file_format.txt", "w") as file:
    i=10000000
    ii=10000000
    file.write(f"{i} {ii}\n")
    for _ in range(i+ii):  # 10,000줄 생성
        num1 = random.randint(1, 10000000)  # 첫 번째 숫자 범위
        num2 = random.randint(1, 10000000)  # 두 번째 숫자 범위
        file.write(f"{num1} {num2}\n")

