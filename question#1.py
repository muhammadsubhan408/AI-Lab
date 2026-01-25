name = input("enter your name : ")
age = int(input ("enter your age : "))  #check this line it is imp
city = input("enter your city : ")

user_info = {"name" : name , "age" : age , "city" : city }

for key,val in user_info.items():
    print({key} ,{val})

if user_info["age"] > 17 :
    print( "congrats the person , " , user_info["name"] , "is eligible to vote !!")
else :
    print("apology :( " , user_info["name"] , "is not eligible to vote sadly")