l = [num*2 for num in range(1, 5)]
names = ['Alex', 'Carol', 'Fisher', 'Fang yuan', 'Peace']
import random
student_score  = {student:random.randint(1, 100) for student in names}
print (student_score.items())
#first method of 
pass_student = {item:student_score[item] for item in student_score if student_score[item]>=60}
#seconf method
pass_student_sm = {student:score for (student, score) in student_score.items() if score >= 60}

import pandas as pd
student_dict = {
    'name': ['Alex', 'Carol', 'Fisher', 'Fang yuan', 'Peace'],
    'score':[random.randint(1,100) for item in names]
}
print(student_dict)
alpha_comp = pd.read_csv('nato_phonetic_alphabet.csv')
alpha_dict = {row.letter:row.code for (index, row) in alpha_comp.iterrows()}
print(alpha_comp.iterrows)

def tryy():
    word = input("enter a word:\n").upper()
    try:
        output_list = [alpha_dict[letter] for letter in word]
    except KeyError:
        print('only letter')
        tryy()
    else:
        print(output_list)
tryy()