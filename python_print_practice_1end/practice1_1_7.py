land, port = map(int, input("직사각형의 가로,세로 길이를 입력해주세요:").split())

width = land+5
length = port*2
area = width*length

print("width =", width)
print("length =", length)
print("area =", area)