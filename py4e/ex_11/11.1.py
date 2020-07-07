#test.txt파일에 있는 모든 숫자의 합 구하기
import re
fh = open("test.txt")
sum =0
for line in fh:
    numbers = re.findall('[0-9]+',line)
    for num in numbers:
        sum = sum + int(num)

print(sum)
