quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "paris"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "berlin"
    },
    "question3": {
        "question": "What is the capital of UK?",
        "answer": "london"
    },
    "question4": {
        "question": "What is the capital of Spain?",
        "answer": "madrid"
    },
    "question5": {
        "question": "What is the capital of Portugal?",
        "answer": "lisbon"
    },
    "question6": {
        "question": "What is the capital of switzerland?",
        "answer": "bern"
    },
    "question7": {
        "question": "What is the capital of Austria?",
        "answer": "vienna"
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("answer? ")

    if answer.lower() == value['answer'].lower():
        print("correct!")
        score += 1
        print(f"your score is {score}")
    else:
        print("wrong!")
        print(f"The answer is {value['answer']}")

print(f"You got {score} out of  {len(quiz)} questions.")
print(f"Your percentage is {(score/len(quiz))*100:.2f}%.")