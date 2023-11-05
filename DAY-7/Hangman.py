import random
word_list=["ardvark","baboon","camel"]
choosen_word=random.choice(word_list)
display=[]
for _ in range(len(choosen_word)):
  display+="_"
print(display) 
end_ff_game=False
while not end_ff_game:
 gues=input("Guess a Letter").lower()

 for position  in range(len(choosen_word)):
  letter=choosen_word[position]
  if letter==gues:
    display[position]=letter

 print(display)
 if '_' not in display:
  end_ff_game=True
 print("You Win")
    # print(display)
    # if letter==gues:
    #     print("right")
    # else:
    #     print("wrong")   a
