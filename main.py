# A program creates a window on your screen using Tkinter.

import tkinter as tk

# Main window
root = tk.Tk()

index = 0
score = 0

score_list = []

questions = [
    "What is the capital of England?",
    "What is the tallest mountain?",
    "What is the longest river?",
    "What is the largest ocean?",
    "What is the smallest planet?",
    "What is the only even prime number?",
    "How many days are in a year?",
    "Which country shares a border with France?",
    "What do bees make?",
    ]

answers = [
    ["Poland", "London", "Amsterdam", "Paris"],
    ["Everest", "Kinabalu", "Aconcagua", "McKinley"],
    ["Amazon", "Nile", "Colorado", "Dragon"],
    ["Atlantic", "Pacific", "Indian", "Arctic"],
    ["Saturn", "Jupiter", "Mars", "Mercury"],
    ["9", "44", "0", "2"],
    ["24", "3000", "200", "365"],
    ["England", "Ukraine", "Lesotho", "Spain"],
    ["Milk", "Juice", "Honey", "Soda"],
    ]

correct_answers = [
    "London",
    "Everest",
    "Nile",
    "Pacific",
    "Mercury",
    "2",
    "365",
    "Spain",
    "Honey"
    ]

def delete():
    for widget in root.winfo_children():
        widget.destroy()

def check_answer(answer, questions, index, score):
    if answer == correct_answers[index]:
        score += 1
    index += 1
    delete()
    if index < len(questions):
        display(index, questions, answers, score)
    else:
        end_screen(answer, questions, index, score)

def display(index, questions, answers, score):
    question = tk.Label(text = questions[index], font=("Arial", 17, "bold"))
    question.pack(padx=20,pady=20)
    answer_choices = answers[index]
    score_display = tk.Label(text = "Score: "+str(score), font=("Arial", 12))
    score_display.pack()
    for j in answer_choices:
        potential_answers = tk.Button( text = j, command = lambda answer = j: check_answer(answer, questions, index, score))
        potential_answers.pack(padx=10,pady=10)

def end_screen(answer, questions, index, score):
    if score < len(questions):
        message = tk.Label(text = "Game over. Would you like to play again?")
    else:
        message = tk.Label(text = "Game over. You got all of them right!")
    message.pack()

    final_score = tk.Label(text = str(score) + '/'+str(len(questions)))
    final_score.pack()

    score_list.append(score)
    high_score = tk.Label(text="Highest score: "+str(max(score_list))+'/'+str(len(questions)))
    high_score.pack()
    index = 0
    score = 0

    restart = tk.Button( text = "Restart?", command = lambda: (delete(), display(index, questions, answers, score)),bg="Green", fg="white", font=("Arial", 12, "bold"))
    restart.pack(padx=10,pady=10)
    
#Main
display(index, questions, answers, score)
root.mainloop()
