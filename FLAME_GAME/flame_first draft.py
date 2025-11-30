#FLAME GAME
name_1=input("Enter ur charming name: ").capitalize()
name_2=input("Enter ur lovely's partner name here: ").capitalize()

ind1=name_1.find(" ")
user_name1=name_1[:ind1]

ind2=name_2.find(" ")
user_name2=name_2[:ind2]



# SEt for user 1
len_1_name=len(user_name1)

if(len_1_name==3):
    a=user_name1[0]
    b=user_name1[1]
    c=user_name1[2]
    l1={a,b,c}
    

elif(len_1_name==4):
    a=user_name1[0]
    b=user_name1[1]
    c=user_name1[2]
    d=user_name1[3]
    l1={a,b,c,d}
    

elif(len_1_name==5):
    a=user_name1[0]
    b=user_name1[1]
    c=user_name1[2]
    d=user_name1[3]
    e=user_name1[4]
    l1={a,b,c,d,e}
    

elif(len_1_name==6):
    a=user_name1[0]
    b=user_name1[1]
    c=user_name1[2]
    d=user_name1[3]
    e=user_name1[4]
    f=user_name1[5]
    l1={a,b,c,d,e,f}
    


elif(len_1_name==7):
    a=user_name1[0]
    b=user_name1[1]
    c=user_name1[2]
    d=user_name1[3]
    e=user_name1[4]
    f=user_name1[5]
    g=user_name1[6]
    l1={a,b,c,d,e,f,g}
    

elif(len_1_name==8):
    a=user_name1[0]
    b=user_name1[1]
    c=user_name1[2]
    d=user_name1[3]
    e=user_name1[4]
    f=user_name1[5]
    g=user_name1[6]
    h=user_name1[7]
    l1={a,b,c,d,e,f,g,h}
    
    
else:
    print("Its ok")


# Set for USER 2
len_2_name=len(user_name2)

if(len_2_name==3):
    a=user_name2[0]
    b=user_name2[1]
    c=user_name2[2]
    l2={a,b,c}
    

elif(len_2_name==4):
    a=user_name2[0]
    b=user_name2[1]
    c=user_name2[2]
    d=user_name2[3]
    l2={a,b,c,d}
    

elif(len_2_name==5):
    a=user_name2[0]
    b=user_name2[1]
    c=user_name2[2]
    d=user_name2[3]
    e=user_name2[4]
    l2={a,b,c,d,e}
    

elif(len_2_name==6):
    a=user_name2[0]
    b=user_name2[1]
    c=user_name2[2]
    d=user_name2[3]
    e=user_name2[4]
    f=user_name2[5]
    l2={a,b,c,d,e,f}
    


elif(len_2_name==7):
    a=user_name2[0]
    b=user_name2[1]
    c=user_name2[2]
    d=user_name2[3]
    e=user_name2[4]
    f=user_name2[5]
    g=user_name2[6]
    l2={a,b,c,d,e,f,g}
    

elif(len_2_name==8):
    a=user_name2[0]
    b=user_name2[1]
    c=user_name2[2]
    d=user_name2[3]
    e=user_name2[4]
    f=user_name2[5]
    g=user_name2[6]
    h=user_name2[7]
    l2={a,b,c,d,e,f,g,h}
    
    
else:
    print("Its ok")

set_user_1=l1
set_user_2=l2

union=set_user_1.union(set_user_2)
intersect=set_user_1.intersection(set_user_2)
print(union)
print(intersect)