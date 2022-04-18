import url
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

    for quest_num in range(50):
        cor_ans = capitals[states[quest_num]]
        wrong_ans = list(capitals.values())
        del wrong_ans[wrong_ans.index(cor_ans)]
        wrong_ans = random.sample(wrong_ans, 3)
        ans_opt = wrong_ans + [cor_ans]

        quiz_file.write(f"{quest_num + 1}. What is the capital of {states[quest_num]}")
        for i in range(4):
            quiz_file.write(f"      {'ABCD'[i]}. {ans_opt[1]}\n")
        quiz_file.write("\n")

        ans_key.write(f"{quest_num + 1}. {'ABCD'[ans_opt.index(cor_ans)]}")
quiz_file.close()
ans_key.close()
