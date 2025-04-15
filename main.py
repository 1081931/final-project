# A program creates a window on your screen using Tkinter.

import tkinter as tk

index = 0

questions = [

    "what is the capital of england?",

    ]

answers = [

    ["Poland", "London", "Amsterdam", "Paris"],

    ]

correct_answers = [

    ["London"],

    ]

def check_answer(j, index):
    if j == correct_answers[index]:
        yes = tk.Label(text = "eh")
        yes.pack()


def refresh(index, answers):
    
    question = tk.Label( text = questions[index])
    question.pack()
    answer_choices = answers[index]

    for j in answer_choices:
        potential_answers = tk.Button( text = j, command = lambda answer = j: check_answer(answer, index))
        potential_answers.pack()



refresh(index, answers)


def my_button(index):

    index+=1
    refresh(index)

    print("kunsh typed that")



# Main window
root = tk.Tk()
root.wm_geometry("300x200")

root.mainloop()
