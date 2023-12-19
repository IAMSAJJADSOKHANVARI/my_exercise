string="hello how are you i'm fine thank you and you?!"
c=(input("enter your character : "))
count=[]
for i in string:
    if i == c:
        count.append(i)
    
print(len(count))