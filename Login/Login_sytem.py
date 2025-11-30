# Login system

full_name=input("Type Your full name: ").capitalize()

#Email id verfication
email_id=input("Type your Email id: ")
email_pw=input("Enter Your Password: ")
confirm_pw=input("Confirm Your password: ")


#VERIFICATIOn via while loop
while email_pw!=confirm_pw:
    print("Your pw is wrong,pls try again")
    email_pw=input("Enter your password: ")
    confirm_pw=input("Confirm your pw again:")
else:
     print("Your pw is verified: ")

# VERIFICATION Via for loop
for i in email_id:
    if(email_pw!=confirm_pw ):
     print("Your pw is wrong, try again")
     email_pw=input("Enter your password: ")
     confirm_pw=input("Confirm ur pw again: ")
else:
    print("Your email id is verified")


# age and gender
age=int(input("Enter your age: "))
sex=input("Whats your gender: ").capitalize()

#making username
gap=full_name.find(" ")
user_name=full_name[:gap]

#Storing user info
user_info={
    "name":user_name,
    "email_id":email_id,
    "age":age,
    "gender":sex,
    "pw_id":email_pw
}
#Asking for user info
info_query=input("Do you want ur info saved with us :").capitalize()


#Checking male or female
if(sex=="Male"):
  print(f"Good Morning Mr {user_name}")
else:
    print(f"Good Morning Mrs {user_name}")

#TIMEPASS COMMANDS
if(age>=18):
    print("You are a big boii\nU can drink")
else:
    print('You are minor')
    print("U cant drink")

#Requesting user info

if("Yes" in info_query):
    print(f"Here is your info {user_info}")
else:
    print("Ok we wont show user info")




    