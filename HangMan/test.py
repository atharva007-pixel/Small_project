# word=["pain","paris","alpine","plane","apple","grape","grapefruit"]


# def game():
#         print("Welcome to the guess game")
#         import random
#         chosen_word=random.choice(word)
        
#         lintial_w=chosen_word[0]
#         llast_w=chosen_word[-1]

#         print(f'''Your first word is of {len(chosen_word)} letters
#               Starting with {lintial_w} and Ending with {llast_w}''')


#         letrs=[]

#         for letters in chosen_word:
#             letrs.append(letters)
        
#         letrs.remove(llast_w)
#         letrs.remove(lintial_w)
#         # print(letrs)
        
#         while True:
#             guess=input("Whats your guess man: ")
#             if guess in letrs:
#                 print("You guessed right")
#                 letrs.remove(guess)
#                 print(f"Now only {len(letrs)} letters are left")
#                 print("_"*len(letrs))
#             else:
#                 print('You guessed wrong')
#         # print(f"The word starts with {lintial_w}")


                    
# game()

s=4
word="Atharva"
# list=[" _ "*len(word)]  
update_l=len(word[1:-1])
# print(word[1:-1])




blanks=(" _ "*update_l)
blanks2=(" _ "*(update_l-1))
filled=[word[0],blanks,word[-1]]

filled.pop(1)
filled.append(blanks2)

print(filled)

# print(filled)

# # list.append(word)
# hash=" _ "
# total_h=hash*update_l





# list=[word[0],total_h,word[-1]]
# print(list)                                           

# g=input("Guess: ")

# hash.replace(" _ "," _ "*len(g))
# n_list=[word[0],total_h,word[-1]]
# n_list.append(g)
# print(n_list)

# for letters in word:

