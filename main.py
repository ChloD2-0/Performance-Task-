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

flashcards= {}
scores = []
def menu(): 
    while True:
        options = input("Main Menu:\n 1. Create New Flashcard\n 2. Study\n 3. View Scores\n 4. Quit\nChoose a number: ")
        if options == "1":
            print("")
            create_cards()
        elif options == "2":
            print("")
            study(flashcards)

        elif options =="3":
             if not scores:
                  print("")
                  print("Scores: None")
                  print("")
             else:
                print(f"Scores: {scores}")
             
        elif options == "4":
            print("")
            print("See you next time!👋")
            break
        
        else:
              print("Please choose 1, 2, 3, or 4")
        
def create_cards(): 
    while True:
        q = input("Enter new question or type 'Q' to end: ")
        if q.upper() == "Q":
            print("")
            break
        else:
            a = input("Enter new answer: ")
            flashcards[q] = a
            print("New flashcard created!\n")
            
    

def study(flashcards):
                flashcards = len(flashcards)
                cards_missed = {}
                correct = 0
                for i in flashcards:
                    print(i)
                    input("")
                    print(flashcards[i])  
                correct = input("Did you get it right?🤔 (y/n): ")
                if correct == "y":
                     right += 1
                else:
                     cards_missed[i] = flashcards[i]
                     print(f"You got {correct} out of {flashcards} correct!")
                     scores.append(correct)

            
menu()


# def want_another():
#             answer = input("Do you want to see the menu again (y/n): ")
#             if answer == "y":
#                 menu()

# want_another()
                                     
