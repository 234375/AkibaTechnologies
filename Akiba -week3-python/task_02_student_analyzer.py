student_list = [
    {"name": "Sara", "score": 85},
    {"name": "Ahmed", "score": 42},
    {"name": "Musa", "score": 93},
    {"name": "Hana", "score": 67}
]

#check the validity of the score
def validate_score(student_score):
    if isinstance(student_score, bool):
        return False #isinstance is built in function that checks if it is in particular type. if score is boolean , reject it.
    if not isinstance(student_score, (int, float)):
        return False #if the score is not int or float reject it.
    if student_score < 0 or student_score > 100:
        return False
    return True 
    
    
def calculate_grade(student_score):
    if not validate_score(student_score):
        return "Invalid Score"
    if student_score >= 90:
        return "A"
    elif student_score >= 80:
        return "B"
    elif student_score >= 70:
        return "C"
    elif student_score >= 60:
        return "D"
    else:
        return "F"

def calculate_average(student_list):
    total_score = 0
    number_of_students = 0
    for one_student in student_list:
        student_score = one_student["score"]
        if validate_score(student_score):
            total_score += student_score
            number_of_students += 1
    if number_of_students == 0:
        return 0
    class_average = total_score / number_of_students
    return class_average


def find_highest_lowest(student_list):
    highest_student = None
    lowest_student = None
    for one_student in student_list:
        student_score = one_student["score"]
        if validate_score(student_score):
            if highest_student is None:
                highest_student = one_student
                lowest_student = one_student
            else:
                if student_score > highest_student["score"]:
                    highest_student = one_student
                if student_score < lowest_student["score"]:
                    lowest_student = one_student
    return highest_student, lowest_student


def count_passed_failed(student_list):
    passed_students = 0
    failed_students = 0
    for one_student in student_list:
        student_score = one_student["score"]
        if validate_score(student_score):
            if student_score >= 50:
                passed_students = passed_students + 1
            else:
                failed_students = failed_students + 1
    return passed_students, failed_students


def find_above_average(student_list):
    class_average = calculate_average(student_list)
    above_average_students = []
    for one_student in student_list:
        student_score = one_student["score"]
        if validate_score(student_score):
            if student_score > class_average:
                above_average_students.append(one_student)
    return above_average_students


def generate_report(student_list):
    if len(student_list) == 0:
        print("No students available.")
        return
    class_average = calculate_average(student_list)
    highest_student, lowest_student = find_highest_lowest(student_list)
    passed_students, failed_students = count_passed_failed(student_list)
    above_average_students = find_above_average(student_list)
    
    print("========== CLASS REPORT ==========")

    print(f"Total Students: {len(student_list)}")

    print("\n----- STUDENT RESULTS -----")

    for one_student in student_list:

        student_name = one_student["name"]
        student_score = one_student["score"]

        if validate_score(student_score):

            student_grade = calculate_grade(student_score)

            if student_score >= 50:
                student_status = "Passed"
            else:
                student_status = "Failed"

            print(
                f"Name: {student_name} | "
                f"Score: {student_score} | "
                f"Grade: {student_grade} | "
                f"Status: {student_status}"
            )

        else:
            print(f"Name: {student_name} | Invalid Score")


    print(f"\nAverage Score: {class_average:.2f}")

    if highest_student is not None:
        print(
            f"Highest Score: {highest_student['name']} - "
            f"{highest_student['score']}"
        )

    if lowest_student is not None:
        print(
            f"Lowest Score: {lowest_student['name']} - "
            f"{lowest_student['score']}"
        )

    print(f"Passed Students: {passed_students}")
    print(f"Failed Students: {failed_students}")

    print("\n----- STUDENTS ABOVE AVERAGE -----")

    for one_student in above_average_students:
        print(f"{one_student['name']} - {one_student['score']}")

generate_report(student_list)