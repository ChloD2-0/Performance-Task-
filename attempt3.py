# Final ---------------------- v
# list_functions = []
scores = []
flashcards = {}
def create_cards(): 
      while True:
                    q = input("\nEnter new question or type 'Q' to end: ")
                    if q.upper().strip() == "Q":
                        print("")
                        menu()
                        break
                    else:
                        a = input("Enter new answer: ")
                        flashcards[q] = a
                        print("Flashcard added!\n")
def study(flashcards):
                # flashcards = len(flashcards)
                # cards_missed = {}
                correct = 0    
                result = 0
                for question, answer in flashcards.items():
                    print(f"Question: {question}")
                    result = input("Answer: ")
                    # print(flashcards[question])  
                    if result == answer:
                         correct += 1
                         return result 
                    else:
                        correct += -1
                        return result
                        # cards_missed[question] = flashcards[question]
                        # cards_missed.update()     
def menu(): 
    while True:
        options = input("Main Menu:\n 1. Create New Flashcard\n 2. Study\n 3. View Scores\n 4. Quit\nChoose a number: ")
        if options == "1":
            create_cards()
            break
        elif options == "2":
            if flashcards == {}:
                  print("\nNo flashcards created\n")
                #   menu()
            else:
                  study(flashcards)
        elif options == "3":
                if scores == []:
                      print("\nScores: None\n")
                      
                else:
                      print(f"Scores: {scores}")
                # menu()
        
        elif options.strip() == "4":
              
              break
        
        else:
              print("\nPlease choose 1, 2, 3, or 4\n")
            
# list_functions.insert(0,menu)
# list_functions.insert(1,create_cards)
# list_functions.insert(2,study)
# list_functions[0]()
menu()