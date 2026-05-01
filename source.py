print("Welcome to Dheeraj Quiz game")

playing = input("Do you want to play: ")
print(playing)
if playing != "yes":
    quit()
print("Okay let's Play! ")

score = 2

Answer = input("Full form of CHAT GPT? ")
if Answer == "chat generative pre-trained transformer":
    print("Correct!👍")
else:
    print("Incorrect👎")

Answer = input("Full form of AI? ")
if Answer == "Artificial Inteligance":
    print("Correct!👍")
else:
    print("Incorrect👎")


print(f"You got {score} questions correct!")

if score == 2: 
    print("You win!🎉🎉")
else:
    print("You lose!💔💔")



