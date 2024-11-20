
import random


registration_email = []
registration_password = []

def Registration():
    while True:
        email = input("Please enter your email:\n").casefold()
        if email in registration_email:
            print("This email is already registered.")
            while True:
                choice = input("Enter '1' to try again or '2' to log in:\n")
                if choice == '1':
                    break
                elif choice == '2':
                    return
                else:
                    print("Please enter a valid input.")
        else:
            password = input("Please enter your password:\n")
            registration_email.append(email)
            registration_password.append(password)
            print("You have registered successfully.")
            return


def Login(email):
    while True:
        password = input("Please enter the password for the registered email:\n")
        index = registration_email.index(email)
        if registration_password[index] != password:
            print("Wrong password. Please try again.")
        else:
            print("Login successful!")
            return


def Generate_Question():
    questions = {
        "What is the primary function of a Database Management System (DBMS)?": [
            "A) To provide a user interface for data entry",
            "B) To manage and store data in a structured format",
            "C) To provide a programming language for software development",
            "D) To provide a network protocol for data communication",
            "B"
        ],
        "What is the difference between a relation and a table in a relational database?": [
            "A) A relation is a set of tuples, while a table is a set of rows",
            "B) A relation is a set of rows, while a table is a set of columns",
            "C) A relation is a set of columns, while a table is a set of rows",
            "D) A relation is a set of rows, while a table is a set of tuples",
            "A"
        ],
        "What is the purpose of the PRIMARY KEY constraint in a relational database?": [
            "A) To uniquely identify each row in a table",
            "B) To specify the order of rows in a table",
            "C) To specify the data type of a column",
            "D) To specify the default value of a column",
            "A"
        ],
        "What is the difference between an INNER JOIN and an OUTER JOIN in a relational database?": [
            "A) An INNER JOIN returns only matching rows, while an OUTER JOIN returns all rows",
            "B) An INNER JOIN returns all rows, while an OUTER JOIN returns only matching rows",
            "C) An INNER JOIN returns only non-matching rows, while an OUTER JOIN returns all rows",
            "D) An INNER JOIN returns all rows, while an OUTER JOIN returns only non-matching rows",
            "A"
        ],
        "What is the purpose of the INDEX data structure in a relational database?": [
            "A) To improve data security",
            "B) To improve data integrity",
            "C) To improve query performance",
            "D) To improve data storage efficiency",
            "C"
        ]
        answers = {"What is the maximum possible length of an identifier?":'none of these',
               "What is a correct syntax to output 'Hello World' in Python?":'print("Hello World")',
               "Which of the following is the correct extension of the Python file?":".py",
               "What will be the value of the following Python expression? 4+3%5 ":7,
               "Which keyword is used for function in Python language?":"def",
               "Which of the following character is used to give single-line comments in Python?":"#",
               "What will be the output of the following Python code? print(True) if 0.1 + 0.2 == 0.3 else print(False)":"False",
               "Which of the following is used to define a block of code in Python language?":"indentation",
               "What will be the output of the following Python code snippet if x=1?  x<<2 ":4,
               "What will be the output of the following Python function? min(max(False,-3,-4), 2,7)":"False",
               "Which of the following is not a core data type in Python programming?":"Class",
               "What will be the output of the following Python function? len(['hello',2, 4, 6]) ":4,
               "Which one of the following is not a keyword in Python language?":"eval",
               "Who developed Python Programming Language?":"Guido van Rossum",
               "Which type of Programming does Python support?":"both",
               "Which of the following is the use of id() function in python?":"Id returns the identity of the object",
               "Which of the following is a Python tuple?":"(1, 2, 3)",
               "Which of the following is used to represent list in python":"[]",
               "Which of the following is the correct syntax for type casting ":"datatype(variable)"
               }

    }

    
    selected_questions = random.sample(list(questions.items()), 5)
    correct_answers = 0

    for idx, (question, options) in enumerate(selected_questions, start=1):
        print(f"\nQuestion {idx}: {question}")
        for i, option in enumerate(options[:-1], start=1):
            print(f"\t{i}. {option}")
        
        # Get user input for the answer
        while True:
            try:
                answer = int(input(f"Select your answer for Question {idx} (1-4): "))
                if 1 <= answer <= 4:
                    break
                else:
                    print("Please select a valid option (1-4).")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")

        # Check if the answer is correct
        if options[answer - 1][0] == options[-1]:
            correct_answers += 1
        else:
            print(f"Incorrect. The correct answer is: {options[-1]}")

    print(f"\nYou answered {correct_answers} out of 5 questions correctly.")


if __name__ == "__main__":
    while True:
        print("\nEnter '1' for registration or '2' for login:")
        choice = input()
        if choice == '1':
            Registration()
        elif choice == '2':
            while True:
                email = input("Please enter your registered email:\n").casefold()
                if email in registration_email:
                    Login(email)
                    break
                else:
                    print("Account not found.")
                    retry = input("Press '1' to register or '2' to try logging in again:\n")
                    if retry == '1':
                        Registration()
                        break
                    elif retry != '2':
                        print("Invalid input. Please try again.")

            Generate_Question()
            while True:
                retry_quiz = input("Do you want to generate another quiz? Press 'y' for Yes or 'n' for No: ").lower()
                if retry_quiz == 'y':
                    Generate_Question()
                elif retry_quiz == 'n':
                    print("Thank you for participating!")
                    exit()
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
        else:
            print("Please enter a valid option.")


