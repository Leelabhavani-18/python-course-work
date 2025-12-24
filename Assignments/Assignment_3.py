def python_quiz():

    questions = [

        # Data Types
        ["What is the data type of 10.5?",
         ["int", "float", "double", "str"], "b"],

        ["Which data type is immutable?",
         ["list", "set", "tuple", "dict"], "c"],

        ["Which of the following is a valid list?",
         ["{1,2,3}", "(1,2,3)", "[1,2,3]", "1,2,3"], "c"],

        # Operators
        ["Which operator is used for modulo?",
         ["%", "//", "**", "@"], "a"],

        ["What is the result of 2 + 3 * 2?",
         ["10", "12", "8", "7"], "d"],

        # Strings
        ["What is the output of 'Python'.upper()?",
         ["PYTHON", "python", "Python", "error"], "a"],

        ["Which function finds length of a string?",
         ["count()", "length()", "len()", "size()"], "c"],

        # Lists
        ["Which method adds an item to a list?",
         ["add()", "insert()", "append()", "push()"], "c"],

        ["What is the index of first element in a list?",
         ["0", "1", "-1", "None"], "a"],

        # Tuples
        ["Tuples are:",
         ["Mutable", "Changeable", "Immutable", "Dynamic"], "c"],

        # Dictionaries
        ["Dictionary stores data in the form of:",
         ["key-value pairs", "index-value", "rows", "sets"], "a"],

        ["Which method returns all dictionary keys?",
         ["keys()", "get()", "items()", "values()"], "a"],

        # Functions
        ["Which keyword is used to return a value?",
         ["send", "return", "yield", "give"], "b"],

        ["Which keyword defines a function?",
         ["fun", "function", "def", "create"], "c"],

        # Loops
        ["Which loop runs until a condition becomes false?",
         ["for", "repeat", "while", "loop"], "c"],

        ["Which statement skips the current iteration?",
         ["break", "stop", "continue", "exit"], "c"],

        # Conditionals
        ["Which keyword is used in else-if?",
         ["elseif", "elif", "else if", "elif()"], "b"],

        ["Which of these is a relational operator?",
         ["=", "==", "+", "*"], "b"],

        # Type Conversions
        ["Which function converts integer to string?",
         ["int()", "str()", "float()", "char()"], "b"],

        ["What is the output of int(4.9)?",
         ["5", "4", "4.0", "error"], "b"]
    ]

    score = 0
    print("Python Quiz Started\n")

    for i, q in enumerate(questions, start=1):
        print(f"Question {i}: {q[0]}")
        print("a)", q[1][0])
        print("b)", q[1][1])
        print("c)", q[1][2])
        print("d)", q[1][3])

        answer = input("Choose (a/b/c/d): ").lower()

        if answer == q[2]:
            print("Correct\n")
            score += 1
        else:
            print("Wrong\n")

    print("Quiz Finished")
    print("Your Score:", score, "/ 20")


python_quiz()
