# Multiplication quiz

import pyinputplus as pyip
import random
import time

num_of_questions = 20
corr_ans = 0
for quest_num in range(num_of_questions):
    num1 = random.randint(0, 15)
    num2 = random.randint(0,18)

    prompt = f"{quest_num}: {num1} * {num2} = "
    try:
        pyip.inputStr(prompt, allowRegexes= [f'{num1 * num2}' ],
                      blockRegexes= [(".*", "Incorrect!")],
                      timeout=10, limit=3)
    except pyip.TimeoutException:
        print("Time Up!")
    except pyip.RetryLimitException:
        print("Out of Tries")
    else:
        print("Correct!")
        corr_ans += 1
    time.sleep(1)
print(f"Score: {corr_ans} / {num_of_questions} ")
