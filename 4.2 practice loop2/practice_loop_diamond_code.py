# Enter a floor of diamond(odd)[quit: -1]: 3
#   *  
#  *** 
#   *  
# Enter a floor of diamond(odd)[quit: -1]: 1
# *
# Enter a floor of diamond(odd)[quit: -1]: 5
#     *    
#    ***   
#   *****  
#    ***   
#     *    
# Enter a floor of diamond(odd)[quit: -1]: 7
#       *      
#      ***     
#     *****    
#    *******   
#     *****    
#      ***     
#       *      
# Enter a floor of diamond(odd)[quit: -1]: -1

num = int(input("Enter a floor of diamond(odd)[quit: -1]:"))

x = num//2
count = 0
for i in range(0,x+1):
    print(" "*(x-i),end='')
    for j in range(0,i+1):
        print("*",end='')
    print("*"*count,end="")
    count += 1
    print('')

y = num-2
for  i in range(1,x+1):
    print(" "*i,"*"*(y), sep="" )
    y -= 2
    
    

