Score = 0
print("welcome to quiz game")
print("you will be asked 5 questions")
print("enter your name")
User_name =input("Name:")

print("Hello",User_name,"!")
print("Let's start the quiz")   

print("first question")
print("1. What is the capital of India?")
ans=input("a) Delhi\nb) Mumbai\nc) Kolkata\nd) Chennai\n Answer:")

if ans == "a":
    print("Correct answer")
    Score += 1
else:
    print("Wrong answer")
    
print("score is",Score)
print("second question")
print("2. Who is the president of inida?")
ans=input("a) Ram Nath Kovind\nb) Droupadi Murmu\nc) A P J Abdul Kalam\nd) Zakir Husain\n Answer:")

if ans == "b":
    print("Correct answer")
    Score += 1  
else:
    print("Wrong answer")   

print("score is",Score)
print("third question")
print("3. What is the currency of India?")
ans=input("a) Dollar\nb) Euro\nc) Rupee\nd) Pound\n Answer:")

if ans == "c":
    print("Correct answer")
    Score += 1
else:
    print("Wrong answer")

print("score is",Score)
print("fourth question")

print("4. Who is the prime minister of India?")
ans=input("a) Narendra Modi\nb) Manmohan Singh\nc) Atal Bihari Vajpayee\nd) Rajiv Gandhi\n Answer:")

if ans == "a":
    print("Correct answer")
    Score += 1
else:
    print("Wrong answer")

print("score is",Score)
print("fifth question")
print("5. What is the national animal of India?")
ans=input("a) Lion\nb) Tiger\nc) Elephant\nd) Peacock\n Answer:")

if ans == "b":
    print("Correct answer")
    Score += 1
else:
    print("Wrong answer")
print("score is",Score)
print("Your final score is",Score)