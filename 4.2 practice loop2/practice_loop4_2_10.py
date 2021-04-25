'''
아래의 피라미드 모형을 출력하시오.
출력 결과에서 #은 공백(space)로 처리해도 됨.


###*###
##***##
#*****#
*******
#*****#
##***##
###*###
'''

plus = 0


for line in range(1,5):
    print("#"*(4-line) + "*"*(line+plus)+"#"*(4-line))
    plus += 1

for line in range(1,4):
    print("#"*(line) + "*"*(line+plus)+"#"*(line))
    plus += -3