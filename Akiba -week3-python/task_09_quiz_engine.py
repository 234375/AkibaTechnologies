questions = [
    {
        "question": "What is the capital city of Ethiopia?",
        "options": ["A", "B", "C", "D"],
        "choices": ["Jimma", "Addis Ababa", "Hawassa", "Bahir Dar"],
        "answer": "B"
    },

    {
        "question": "Which language is used for web development?",
        "options": ["A", "B", "C", "D"],
        "choices": ["Python", "HTML", "C++", "Java"],
        "answer": "B"
    },

    {
        "question": "What does CPU stand for?",
        "options": ["A", "B", "C", "D"],
        "choices": [
            "Central Processing Unit",
            "Computer Personal Unit",
            "Central Program Utility",
            "Control Processing User"
        ],
        "answer": "A"
    },

    {
        "question": "Which one is a Python data type?",
        "options": ["A", "B", "C", "D"],
        "choices": ["integer", "browser", "keyboard", "monitor"],
        "answer": "A"
    },

    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A", "B", "C", "D"],
        "choices": ["//", "#", "/*", "<!--"],
        "answer": "B"
    }
]


def display_question(question_data):
    print("\n" + question_data["question"])
    for i in range(len(question_data["options"])):
        print(
            question_data["options"][i] + ". " +
            question_data["choices"][i]
        )

def validate_answer(answer, valid_options):
    answer = answer.upper()
    if answer in valid_options:
        return True
    else:
        return False

def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return True
    else:
        return False

def update_score(score, is_correct):
    if is_correct:
        score += 1
    return score

def display_results(score, total_questions):
    incorrect = total_questions - score
    percentage = (score / total_questions) * 100
    print("\n========== QUIZ RESULTS ==========")
    print("Total Questions:", total_questions)
    print("Correct Answers:", score)
    print("Incorrect Answers:", incorrect)
    print("Final Score:", score, "/", total_questions)
    print("Percentage:", percentage, "%")
    if percentage >= 90:
        category = "Excellent"
    elif percentage >= 80:
        category = "Very Good"
    elif percentage >= 70:
        category = "Good"
    elif percentage >= 50:
        category = "Pass"
    else:
        category = "Needs Improvement"
    print("Category:", category)


def run_quiz():
    score = 0
    for question_data in questions:
        display_question(question_data)
        while True:
            user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
            valid = validate_answer(
                user_answer,
                question_data["options"]
            )
            if valid:
                break
            print("Invalid option! Please try again.")
        correct = check_answer(
            user_answer,
            question_data["answer"]
        )
        if correct:
            print("Correct answer!")
        else:
            print("Wrong answer!")
        score = update_score(score, correct)
    display_results(score, len(questions))

while True:
    run_quiz()
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thank you for playing!")
        break