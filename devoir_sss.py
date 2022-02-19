# # вывести одно неповторяющееся число из списка
# nums=list(input("nums: "))
# for x in nums:
#     a=nums.count(x)
#     if a==1:
#         print(x)
# word="letter"
# for x in word:
#     b=word.count(x)
#     if b==1:
#         print(x)
# # из массива чисел вывести индекс тех, чья сумма= константе
# a=9
# nums=list(map(int, input("list:").split()))
# print(nums)

# for x in nums:
#     for y in nums:
#         sum_1=x+y
#         if sum_1==a:
#             print(nums.index(x))
# #вывести true если число палиндром
# polindrom = int(input("num:"))
# a=[int(x) for x in str(polindrom)]
# print(a)
# b=list(reversed(a))
# print(b)

# if a==b:
#     print("yes")
# else:
#     print("no")
# #вывести общий префикс
# b=list()
# words=list(map(str,input("words:").split()))
# for x in words:
#     a=list(x)
#     b.append(a)
# i=0
# j=0
# result=list()
# while b[i][j]==b[i+1][j]==b[i+2][j]:
#     result.append(b[i][j])
#     j+=1
# if b[i][j]!=b[i+1][j]!=b[i+2][j]:
#     print("no")
# print("".join(result))
# #скобки должны закрываться
# st=list(input("str:"))
# i=0
# if st[i]=="(":
#     if st[i+1]==")":
#         print("true")
#     else:
#         print("false")
#     i+=1
# if st[i]=="[":
#     if st[i+1]=="]":
#         print("true")
#     else:
#         print("false")
#     i+=1
# if st[i]=="{":
#     if st[i+1]=="}":
#         print("true")
#     else:
#         print("false")
#     i+=1
# удалить повторяющиеся элементы списка
b = [0,0,1,1,1,2,2,3,3,4]
print(b)
i = 0
for x in b:
    while i < len(b)-1:

        if b[i] == b[i+1]:
            b[i] = b[-1]
        i += 1
        
b.sort()
i=len(b)-1
while b[i]==b[i-1]:
    b[i]="_"
    i=i-1
print(b)
