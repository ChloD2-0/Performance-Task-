
def menu():
    options = input("Main Menu:\n 1. Create New Flashcard\n 2. Study\n 3. Delete Flashcard\nChoose an option: ")
   
    while options:
        if options == "1":
            def create_cards(): 
                # print("Before studying, create some new flashcards.")
                flashcard_dict = {}

                go = "start"

                while go:
                    question = input("Enter new question or type 'Q' to end: ")
                    if question == "Q":
                        break
                    else:
                        answer = input("Enter new answer: ")
                        flashcard_dict[question] = answer
                        print("New flashcard created")
                        return flashcard_dict
            create_cards()
            break
        elif options == "2":
            def study(dictionary):
                flashcards = dictionary 
                length = len(flashcards)
                cards_missed = {}
                correct = 0
                for card in flashcards:
                    print(card)
                    input("")
                    print(flashcards[card])

        elif options == "3":
            return options
     
menu()


