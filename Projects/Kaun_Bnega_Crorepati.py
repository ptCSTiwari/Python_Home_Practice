questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Plumber", "Actor", "Astronaut", 3],
    ["What is the capital of France?", "Berlin", "Paris", "Rome", "London", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["What is the largest mammal?", "Shark", "Blue Whale", "Elephant", "Giraffe", 2],
    ["Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Charles Dickens", "Homer", 1],
    ["What is the square root of 64?", "8", "10", "6", "12", 1],
    ["Which country is known as the Land of the Rising Sun?", "India", "South Korea", "Japan", "China", 3],
    ["Who painted the Mona Lisa?", "Claude Monet", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", 3],
    ["What is the fastest land animal?", "Horse", "Lion", "Cheetah", "Elephant", 3],
    ["Which ocean is the largest?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2],
    ["What is the smallest country in the world?", "San Marino", "Vatican City", "Monaco", "Liechtenstein", 2],
    ["Who owns jersey no 18 in cricket?", "Rohit Sharma", "Jasprit Bumrah", "Virat Kohli", "Hardik Pandya", 3],
    ["Which format is the longest in cricket?", "T10", "Test Cricket", "ODI", "Super Over", 2],
    ["How many continents are there on Earth?", "7", "5", "6", "8", 1],
    ["Who is India's Prime Minister?", "Atal Bihari Vajpayee", "Bhagat Singh", "Dr. APJ Abdul Kalam", "Narendra Modi", 4],
    ["Which planet is known as the 'Morning Star'?", "Venus", "Mars", "Jupiter", "Saturn", 1]
]

prizes = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000,640000, 1250000, 2500000, 5000000,10000000, 70000000]

safe_level1 = 4
safe_level2 = 9
safe_level3 = 14

i = 0
total_winnings = 0
safe_amount = 0

for question in questions:
    print(f"\nQuestion {i + 1}: {question[i]}")
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")
    try:
        ans = int(input("Enter your answer (1 for a, 2 for b, 3 for c, 4 for d): "))
    except ValueError:
        print("Invalid input! Only 1 to 4 are allowed.")
        break

    if ans == question[5]:
        print("✅ Correct Answer!")
        print(f"You won ₹{prizes[i]}")
        total_winnings += prizes[i]

        if i == safe_level1:
            safe_amount = 10000
        elif i == safe_level2:
            safe_amount = 320000
        elif i == safe_level3:
            safe_amount = 10000000

        print(f"Total winnings so far: ₹{total_winnings}\n")
    else:
        print(f"❌ Incorrect! The correct answer was option {question[5]}")
        print(f"You are going home with ₹{safe_amount}")
        break

    i += 1

if i == len(questions):
    print(f"\n🎉 Congratulations! You've won the jackpot of ₹{total_winnings}")
