# flashcards = [ 
#     {Term = input("Enter term: ")},
#     {Meaning = input("Meaning:  ")},
#     {Level = input("Difficulty level: ")},
# ]
# flashcard.cards

# def flashcard(x, y): 
#     question = input("Create new flashcard?🤔 (y/n)")
#     if question == "y":
#         x = input("Enter term: ")
#         y = input("Enter definition: ")


# flashcard(x,y)
# flashcards = 
#     {
#         "Term":,
#             "Meaning":,
#                 "Level" :
#                 }

#                 def create_card():
#                     input("Create new flashcard?🤔 (y/n)")
#                         if == "y":
#                                 input("Enter term: ")
#                                         input("Meaning:  ")
#                                                 input("Difficulty level: ")

#                                                 create_card()   
# --------------------- Try 1 ^
# list_functions = []
# def menu(): 
#     options = input("Main Menu:\n 1. Create New Flashcard\n 2. Study\n 3. Delete Flashcard\nChoose a number: ")
#     while options:
#         if options == "1":
#             def create_cards(): 
#                 # print("Before studying, create some new flashcards.")
#                 flashcards= {}

#                 go = "start"

#                 while go:
#                     q = input("Enter new question or type 'Q' to end: ")
#                     if q.upper() == "Q":
#                         break
#                         print("")
#                         menu()
#                     else:
#                         a = input("Enter new answer: ")
#                         flashcards[q] = a
#                         print("Flashcard added!\n")
#             create_cards()
#             break
#         elif options == "2":
#             def study(dictionary):
#                 flashcards = dictionary 
#                 length = len(flashcards)
#                 cards_missed = {}
#                 correct = 0
#                 for i in flashcards:
#                     print(i)
#                     input("")
#                     print(flashcards[i])  
#                 correct = input("Did you get it right?🤔 (y/n): ")
#                 if correct == "y":
#                      right += 1
#                 else:
#                      cards_missed[i] = flashcards[i]
#             study(create_cards())
#             break

#         elif options == "3":
#             return options
#             # answer = input("Do you want to see the menu again (y/n): ")
#             # if answer == "y":
#             #     list_functions[0]
        
# menu()
#---------------------- Try 2 ^

flashcards = {}
scores = []
def menu(): 
    while True:
        options = input("Main Menu:\n 1. Create New Flashcard\n 2. Study\n 3. View Scores\n 4. Quit\nChoose a number: ")
        if options.strip() == "1":
            print("")
            create_cards()
        elif options.strip() == "2":
            print("")
            study(flashcards)

        elif options.strip() =="3":
            print(f"Scores: {scores}")
        
        elif options.strip() == "4":
            print("")
            print("See you next time!")
            break
        else: 
            print("")
            print("Please choose 1, 2, 3, or 4") 
            print("")
def create_cards(): 
    while True:
        q = input("Enter new question or type 'Q' to end: ")
        if q.upper().strip() == "Q":
            print("")
            break
        else:
            a = input("Enter new answer: ")
            flashcards[q] = a
            print("New flashcard created!\n")
def study(flashcards):
    if not flashcards:
        print("No flashcards created")
        print("")
        return
    cards_missed = {}
    correct = 0
    for questions in flashcards:
        print(f"Question: {questions}")
        input("Answer: ")
        print(f"Correct answer: {flashcards[questions]}")  
        result = input("Did you get it right? (y/n): ")
        print("")
        if result == "y":
            correct += 1
        else:
            cards_missed[questions] = flashcards[questions]
        num_of_flashcards = len(flashcards)
        grade = (correct / num_of_flashcards) * 100
    print(f"You got {correct} out of {len(flashcards)} correct!")
    print(f"You scored a {grade}%\n")
    scores.append(grade)

menu()


# def want_another():
#             answer = input("Do you want to see the menu again (y/n): ")
#             if answer == "y":
#                 menu()

# want_another()
                                     
