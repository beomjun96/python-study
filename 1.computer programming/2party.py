people = input("참석자의 수를 입력하시오: ")
print("치킨의 수: ",int(people) )
print("맥주의 수: ",int(people)*2)
print("케익의 수: ",int(people)*4)


#way 1
#위와 결과가 같음 - 문자열을 정수로 바꿔주려면 다시 형태를 바꿔서 해야함
#int(people)같은 경우, 한번만 형태가 변환되고 그 다음은 안됨.
#people = int(people) 로 꼭 변환하기
""""
people = input("참석자의 수를 입력하시오: ")
int(people)
print("치킨의 수: ",people )
print("맥주의 수: ",people*2)
print("케익의 수: ",people*4)
"""
# 이렇게 하면 
# 25
# 2525
# 25252525 이렇게 문자열로 나옴

"""
people = input("참석자의 수를 입력하시오: ")
people = int(people)
print("치킨의 수: ",people )
print("맥주의 수: ",people*2)
print("케익의 수: ",people*4)
"""

#way 2
# people = int( input("참석자의 수를 입력하시오: "))


#print( people )
#print( type( people ) ) - 해당 변수의 형태(type)을 알려줌



#print("치킨의 수:", people, sep="" ) 출력된 결과 바꾸기 sep="여기 안에 쓰기"   디폴트값은 " "로 띄어쓰기 된 상태로 나타남
