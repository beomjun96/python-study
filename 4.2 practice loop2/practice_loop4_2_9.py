# 문제 9.
# 아래의 결과를 보이도록 프로그램을 작성하시오.

#    *
#   ***
#  *****
# *******


plus = 0

for line in range(1,5):
    print(" "*(4-line) + "*"*(line+plus))
    plus += 1
