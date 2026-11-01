def check_length(password, min_length=8):
    if len(password) >= min_length:
        return True
    else:
        return False

def check_uppercase(password):
    for character in password:
        if character.isupper():
            return True
    return False

def check_lowercase(password):
    for character in password:
        if character.islower():
            return True
    return False

def check_digits(password):
    for character in password:
        if character.isdigit():
            return True
    return False


def check_special(password):
    for character in password:
        if not character.isalnum(): #.isalnum() means is alphabetic or numeric.It checks whether a character is An uppercase letter,A lowercase letter,A digit.
            return True
    return False

def analyze_password(password):
    report = {
        "Minimum Length": check_length(password),
        "Uppercase Letters": check_uppercase(password),
        "Lowercase Letters": check_lowercase(password),
        "Digits": check_digits(password),
        "Special Characters": check_special(password)
    }
    passed = 0
    failed = 0
    missing_requirements = []
    for requirement, result in report.items():
        if result == True:
            passed += 1
        else:
            failed += 1
            missing_requirements.append(requirement)
    return {
        "report": report,
        "passed": passed,
        "failed": failed,
        "missing": missing_requirements
    }

def display_report(password):
    result = analyze_password(password)
    print("\nPassword Analysis")
    print("--------------------")
    for requirement, status in result["report"].items():
        if status == True:
            print(requirement, ": PASS")
        else:
            print(requirement, ": FAIL")
    print("\nPassed:", result["passed"])
    print("Failed:", result["failed"])
    if result["failed"] == 0:
        print("Password meets all requirements!")
    else:
        print("Missing requirements:")
        for requirement in result["missing"]:
            print("-", requirement)

passwords = [
    "Hello123!",
    "hello123!",
    "HELLO123!",
    "Hi1!"
]
for password in passwords:
    print("\nTesting:", password)
    display_report(password)