# A program creates a window on your screen using Tkinter.

import tkinter as tk

# Main window
root = tk.Tk()


index = 0
score = 0


questions = [

    "What is the capital of England?",
    "What is the tallest mountain?",
    "What is the longest river?",
    "What is the largest ocean?",
    "What is the smallest planet?",
    "What is the only even prime number?",
    
    ]

answers = [

    ["Poland", "London", "Amsterdam", "Paris"],
    ["Everest", "Kinabalu", "Aconcagua", "McKinley"],
    ["Amazon", "Nile", "Colorado", "Dragon"],
    ["Atlantic", "Pacific", "Indian", "Arctic"],
    ["Saturn", "Jupiter", "Mars", "Mercury"],
    ["9", "44", "0" ,"2"]

    ]

correct_answers = [

    "London",
    "Everest",
    "Nile",
    "Pacific",
    "Mercury",
    "2",
    
    ]


#def refresh(index):
    #index+=1
    #question = tk.Label( text = questions[index])
    #question.pack()
    #answer_choices = answers[index]
####

def delete():
    for widget in root.winfo_children():
        widget.destroy()


def check_answer(answer, questions, index, score):
    if answer == correct_answers[index]:
        score +=1
    index+=1
    delete()
    check(index, questions, answers, score)



def check(index, questions, answers, score):

    question = tk.Label(text = questions[index])
    question.pack()
    answer_choices = answers[index]

    score = tk.Label(text = score)
    score.pack()

    for j in answer_choices:
        potential_answers = tk.Button( text = j, command = lambda answer = j: check_answer(answer, questions, index, score))
        potential_answers.pack()


check(index, questions, answers, score)


root.mainloop()

