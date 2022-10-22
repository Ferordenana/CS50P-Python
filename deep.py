universe_question = input("What's the answer to the great question?: ")

universe_question = universe_question.lower().strip()
if universe_question == "forty-two" or universe_question == "forty two":
    print("Yes")
elif universe_question == "42":
    print("yes")
else:
    print("No")