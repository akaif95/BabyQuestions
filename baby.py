from random import choice

questions = ["Why is the earth round?: ", "Why is the sun so bright?: ", "Why is the sky blue?: "]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("why?: ").strip().lower()
    
    
print("Oh.....Okay.")
