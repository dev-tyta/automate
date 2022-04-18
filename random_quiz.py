import shelve
import pyperclip
import random

# shelfData = shelve.open("mydata")
# musicians = ["Khalid", "Wizkid", "James Arthur", "Lewis Capaldi", "Jacob Banks"]

# shelfData["musicians"] = musicians
# shelfData.close()


for quizNum in range(35):
    quiz_file = open(fr"capital_quiz{quizNum + 1}.txt", "w")
    ans_key = open(fr"capital_quizans{quizNum + 1}.txt", "w")

    quiz_file.write("Name:\n\nDate:\n\nPeriod:\n\n")
    quiz_file.write((" " * 20) + f"State Capitals Quiz(Form{quizNum + 1})")
    quiz_file.write("\n\n")

    states = list(capitals.keys())
    random.shuffle(states)