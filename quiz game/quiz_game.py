print("Welcome to quiz game!")

answer = input("Do you want to play game? ")

score = 0

if answer.lower() != "yes":
    quit()

first_answer = input("What does the CPU stand for?")

if first_answer.lower() == "central processing unit":
    print("Correct")
    score += 1

else:
    print("Incorrect")

second_answer = input("What does the GPU stand for?")

if second_answer.lower() == "graphics processing unit":
    print("Correct")
    score += 1

else:
    print("Incorrect")


third_answer = input("What does the RAM stand for?")

if third_answer.lower() == "random access memory":
    score += 1
    print("Correct")
else:
    print("Incorrect")

print("There were in total 3 questions.")
print('you have correctly answered {} questions'.format(score))
