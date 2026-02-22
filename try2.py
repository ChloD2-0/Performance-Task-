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


list_functions = []
scores = []
flashcards= {}
def create_cards(): 
                

                go = "start"

                while go:
                    q = input("Enter new question or type 'Q' to end: ")
                    if q.upper().strip() == "Q":
                        list_functions[0]()
                    else:
                        a = input("Enter new answer: ")
                        flashcards[q] = a
                        print("Flashcard added!\n")
def study(flashcards):
                flashcards = len(flashcards)
                cards_missed = {}
                correct = 0    
                result = 0
                for q in flashcards:
                    print(q)
                    result = input("")
                    print(flashcards[q])  
                    if input("") == flashcards[q]:
                         correct += 1
                         return result 
                else:
                      correct += -1
                      cards_missed[q] = flashcards[q]
                      cards_missed.append()
def menu(): 
    options = input("Main Menu:\n 1. Create New Flashcard\n 2. Study\n 3. View Scores\n 4. Quit\nChoose a number: ")
    while options:
        if options == "1":
            
            create_cards()
            break
        elif options == "2":
            study(flashcards)
            break

        elif options == "3":
                if scores == []:
                      print("\nScores: None\n")
                      menu()
                else:
                      print(f"Scores: {scores}")

                break
        elif options == "4":
              break
            
list_functions.insert(0,menu)
list_functions.insert(1,create_cards)
list_functions.insert(2,study)
list_functions[0]()