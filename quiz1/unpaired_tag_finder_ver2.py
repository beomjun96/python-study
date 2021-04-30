# 아래와 같은 입력에 대한 출력을 제공하는 프로그램을 작성하시오.
# 문제. 4 unpaired tag finder아래와같은입력에대한출력을제공하는프로그램을작성하시오.

# 예시 1)Input: "<div><div><b></b></div></p>"
# Output: div
# 예시 2)Input: "<div>abc</div><p><em><i>test test test</b></em></p>"
# Output: i



input_string = input("태그 입력:")
tag_list = []
tag_str = ""

for x in input_string:
    tag_str = tag_str + x
    if "<" not in tag_str:
        tag_str = ""

    if "<" and ">" in tag_str:
        num = len(tag_str)
        tag_str = tag_str[1:num-1]
        if "/" in tag_str:
            tag_str = tag_str.replace("/","")
            if tag_str not in tag_list:
                tag_list.append("/"+tag_str)
            else:
                tag_list.remove(tag_str)


        else:
            tag_list.append(tag_str)
        tag_str = ""

    
    

print("unpaired tag",tag_list)


############################################ 추가로 /p 태그나 /b 태그 안넣고 싶으면 list작성 후 조건문 돌리기