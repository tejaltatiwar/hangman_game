import random

stages=['''   
       _______
     |/      |
     |      (_)
     |       
     |       
     |     
     |
     |___
     ''',
    '''  
           _______
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
     |___
''','''
       _______
     |/      |
     |      (_)
     |      \|
     |       |
     |      
     |
     |___
''','''
       _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
     |___
''',
        '''
        _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
     |___
''','''     
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
     |___
''']

decending_stages= stages[::-1]
# print(decending_stages)

lives=6

word_list=["ardvark","baboon","camel"]
chosen_word=random.choice(word_list)
print(f"Choosen word is {chosen_word} .")

display=[]
for l in chosen_word:
    display.append("_")
print(display)

end_of_game=False
while not end_of_game:
    guess = input("Guess a letter:")
    guess = guess.lower()

    for position in range(len(chosen_word)):
        l = chosen_word[position]
        if l == guess:
            display[position] = l
    print(display)

    if guess not in chosen_word:
        lives-=1
        if lives == 0:
            end_of_game=True
            print("You lose!")
        print(decending_stages[lives])
