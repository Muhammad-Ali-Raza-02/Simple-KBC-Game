# Simple KBC-style quiz (Beginner Version)

questions = [
    ["What is the capital of Pakistan?",
     ["1. Karachi", "2. Lahore", "3. Islamabad", "4. Peshawar"], 3],

    ["Which planet is known as the Red Planet?",
     ["1. Earth", "2. Mars", "3. Jupiter", "4. Venus"], 2],

    ["Who invented the light bulb?",
     ["1. Edison", "2. Newton", "3. Einstein", "4. Tesla"], 1],

    ["Which is the largest ocean in the world?",
     ["1. Atlantic", "2. Indian", "3. Pacific", "4. Arctic"], 3],

    ["Which gas do plants absorb from the atmosphere?",
     ["1. Oxygen", "2. Nitrogen", "3. Carbon Dioxide", "4. Hydrogen"], 3],

    ["Who wrote 'Pakistan ka matlab kya' slogan?",
     ["1. Allama Iqbal", "2. Liaquat Ali Khan", "3. Chaudhry Rehmat Ali", "4. Maulana Zafar Ali Khan"], 4],

    ["Which is the fastest land animal?",
     ["1. Tiger", "2. Lion", "3. Cheetah", "4. Horse"], 3],

    ["What is H2O commonly known as?",
     ["1. Oxygen", "2. Water", "3. Hydrogen", "4. Helium"], 2],

    ["Who is called the Father of Computers?",
     ["1. Charles Babbage", "2. Bill Gates", "3. Alan Turing", "4. Steve Jobs"], 1],

    ["Which is the smallest continent?",
     ["1. Europe", "2. Australia", "3. Antarctica", "4. Africa"], 2],
]

score = 0  # start with zero

for q in questions:
    print("\n" + q[0])  # show question
    for option in q[1]:  # show options
        print(option)

    answer = input("Enter your option number (1-4): ")

    if answer == str(q[2]):  # correct
        print("Correct!\n")
        score = score + 1
    else:  # wrong answer
        correct_option = q[1][q[2] - 1]
        print("Wrong answer!")
        print("Correct answer is:", correct_option)
        print("Better luck next time!")
        break  # end the game

# after loop ends
if score == len(questions):  # all questions correct
    print("\nCongratulations! You have won! 🎉")
else:
    print("\nYour final score is:", score)
