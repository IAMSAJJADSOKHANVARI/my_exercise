
# target = int (input ("please Enter your target: "))
# aray=[]
# index=[0,0]
# n= len(aray)
# for i in range (5):
#     vorodi= int (input("enter your add array: "))
#     aray.append(vorodi)
#     print(aray)
# for j in range (n):
#     for k in range (j+1,n):
#         if aray[k] == (target - aray[j]):
#             index[0],index[1]= j , k
#             print (index)
# print(index)
####
target = int(input("Please enter your target: "))
aray = []
index = [0, 0]

for i in range(5):
    vorodi = int(input("Enter your array element: "))
    aray.append(vorodi)
    print(aray)

n = len(aray)
for j in range(n):
    for k in range(j+1, n):
        if aray[k] + aray[j] == target:
            index[0], index[1] = j, k
            print(index)

print(index)