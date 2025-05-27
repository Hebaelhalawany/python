################11111111111111111################
# str= input("Enter a string: ")
# a= ['a','o','e','i','u']
# c=0
# for i in str:
#     if i in a:
#         c+=1
# print(c)

##############22222222222222###############
# a = []
# for num in range(5):
#     num = int(input("Enter a number: "))
#     a.append(num)
# a.sort()
# print(a)
# a.reverse()
# print(a)

# ###########333333333333########
# str= input("Enter a string: ")
# print(str.count('iti'))

# ############4444444444###########
# str= input("Enter a string: ")
# a= ['a','o','e','i','u']
# str1=[]
# for i in str:
#     if i not in a:
#         str1.append(i)
# print(str1)
# print(''.join(str1))

# #############555555##################
# str= input("Enter a string: ")
# print(str.index('i'))

# ###########66666##############

num = int(input("Enter a number: "))
all = []
for i in range(1,num+1):
    r = [i * j for j in range(1, i + 1)]
    for j in range(1, i + 1):
        r= [i * j]
    all.append(r)

print(all)
