
questions = ["What is the capital of India?",
            "Select North Eastern State from the following options:"]
options = [
            ["New Delhi", "Mumbai", "Jaipur", "Chennai"],
            ["West Bengal", "Assam", "Himachal", "Maharashtra"]
            ]
answers = ["New Delhi", "Assam"]

# Take input from user
for i in range(len(questions)):
    print(questions[i])
    for k in range(len(options)):
        print(options[i][k])
    answer=input("Answer: ")
    if str.lower(answer)==str.lower(answers[i]): # string matching
        print("correct!")
    else:
        print("not correct")
