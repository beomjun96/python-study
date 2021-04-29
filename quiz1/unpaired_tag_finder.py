# 아래와 같은 입력에 대한 출력을 제공하는 프로그램을 작성하시오.
# 문제. 4 unpaired tag finder아래와같은입력에대한출력을제공하는프로그램을작성하시오.

# 예시 1)Input: "<div><div><b></b></div></p>"
# Output: div
# 예시 2)Input: "<div>abc</div><p><em><i>test test test</b></em></p>"
# Output: i

input_string = input("태그 입력:")
tag_dic = {}

while ">" in input_string:
    for word in input_string:
        if word == ">":
            num = input_string.find(word)           # > 위치 찾기
            tag_dic[input_string[1:num]] = 1
            for word in tag_dic:
                if word == 1 :
                    tag_dic[word] = 1 
                else:
                    tag_dic[word] += 1
            input_string = input_string[num+1:]
            

        

print(tag_dic)


# input_string = input("태그 입력:")
# tag_list = []
# count = 1

# while ">" in input_string:
#     for word in input_string:
#         if word == ">":
#             num = input_string.find(word)
#             tag_list.append([input_string[1:num],count])
#             for i in tag_list:
#                 if tag_list[i][0][0:num+1] == input_string[1:num] :
#                     count += 1
                    
#             input_string = input_string[num+1:]

# print(tag_list)


