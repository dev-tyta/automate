import url
import pyperclip
import random

capitals = url.capitals

for quizNum in range(35):
    quiz_file = open(fr"C:\Users\Testys\Documents\GitHub\automate\capital\capital_quiz{quizNum + 1}.txt", "w")
    ans_key = open(fr"C:\Users\Testys\Documents\GitHub\automate\capital\capital_quizans{quizNum + 1}.txt", "w")

    quiz_file.write("Name:\n\nDate:\n\nPeriod:\n\n")
    quiz_file.write((" " * 20) + f"State Capitals Quiz(Form{quizNum + 1})")
    quiz_file.write("\n\n")

    states = list(capitals.keys())
    random.shuffle(states)
