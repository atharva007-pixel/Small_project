import os



print("What name would like to give to your pics")
new_name=input("Enter here: ")
# ss_path="C:\\Users\\PC\\Pictures\\Screenshots"
ss_path=os.path.join(os.path.expanduser("~"),"Documents",)

i=1
for pics in os.listdir(ss_path):
    name,ext=os.path.splitext(pics)  #Name part takes nd ext takes extension
    # print(ext)
    if pics.endswith(".png") or pics.endswith(".jpg"):
        
        old_n=os.path.join(ss_path,pics)
        new_n=os.path.join(ss_path,f"{new_name}{i}{ext}")
        i+=1
        os.rename(old_n,new_n)
        print(f"Your pics name has been changed {pics} to {new_name}{i}{ext}")
        



# import os

# ss_path = os.path.join(os.path.expanduser("~"), "Documents")

# i = 1
# for pics in os.listdir(ss_path):
#     if pics.lower().endswith((".png", ".jpg")):
#         old_path = os.path.join(ss_path, pics)
        
#         # keep the original extension
#         _, ext = os.path.splitext(pics)
        
#         new_name = f"SS_{i}{ext}"
#         new_path = os.path.join(ss_path, new_name)

#         os.rename(old_path, new_path)
#         print(f"{pics} → {new_name}")

#         i += 1
















