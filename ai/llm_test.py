from brain import generate_ideas, generate_stack

while True:
    user_question = input("\rType your response here: ") + "\n"
    if user_question == "quit\n":
        break
    answer = generate_ideas(user_question)
    print(answer)