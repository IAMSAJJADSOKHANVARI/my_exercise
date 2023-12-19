string=input("enter your string :  ")
space=string.rstrip()  #because i use rstrip ,remove the space right 

s=string.rfind(" ")  #find first right space 
print(space[s+1:])