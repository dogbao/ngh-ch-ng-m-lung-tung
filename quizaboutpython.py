def run_quiz():
    questions = [
        {
            "question": "What is the correct file extension for Python files?",
            "options": ["A. .pt", "B. .py", "C. .pyt", "D. .pw"],
            "answer": "B"
        },
        {
            "question": "Which keyword is used to create a function in Python?",
            "options": ["A. function", "B. create", "C. def", "D. fn"],
            "answer": "C"
        },
        {
            "question": "How do you insert comments in Python code?",
            "options": ["A. //", "B. <!--", "C. /*", "D. #"],
            "answer": "D"
        }
    ]

    score = 0

    print("--- Welcome to the Python Quiz ---\n")

    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for option in q['options']:
            print(option)
        
        user_answer = input("Your answer (A, B, C, or D): ").strip().upper()
        
        if user_answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")

    print(f"Quiz finished! You scored {score}/{len(questions)}.")

run_quiz()
