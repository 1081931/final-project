# A program creates a window on your screen using Tkinter.

import tkinter as tk

index = 0

questions = [

    "What is the capital of England?",
    "What is the tallest mountain?",
    "What is the longest river?",
    "What is the largest ocean?",
    "What is the smallest planet?",
    "What is the only even prime number?",
    :
    ]

answers = [

    ["Poland", "London", "Amsterdam", "Paris"],
    ["Everest", "Kinabalu", "Aconcagua", "McKinley"]
    ["Amazon", "Nile", "Colorado", "Dragon"]
    ["Atlantic", "Pacific", "Indian", "Arctic"]
    ["Saturn", "Jupiter", "Mars", "Mercury]
    ["9", "44", "0" ,"2"]
    [
    ]

correct_answers = [

    "London",
    "Everest",
    "Nile",
    "Pacific",
    "Mercury",
    "2",
    
    ]

def check_answer(answer, index):
    if answer == correct_answers[index]:
        yes = tk.Label(text = "yes")
        yes.pack()
    else:
        no = tk.Label(text = "no")
        no.pack()


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


