questions = [
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. HTML", "C. Java", "D. C++"],
        "answer": "B"
    },
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Pune", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. int", "B. string", "C. float", "D. bool"],
        "answer": "D"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. /*", "D. --"],
        "answer": "B"
    }
]

score = 0

print("===== PYTHON QUIZ GAME =====")

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    answer = input("Enter your answer: ").upper()

    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\n===== QUIZ RESULT =====")
print("Your Score:", score, "/", len(questions))

if score == 5:
    print("Excellent!")
elif score >= 3:
    print("Good Job!")
else:
    print("Keep Practicing!")