# 2020 kakao coding test
# 문자열 압축

s = input("문자열 입력(1000자 이하):")
slice_list = []

if len(s)<= 2:
    print(s)

else:
    for slice_num in range(0,len(s)):
        slice_list.append(s[slice_num])

print(slice_list)