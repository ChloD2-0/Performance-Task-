list_functions = []
def menu(): 
    options = input("Main Menu:\n 1. Create New Flashcard\n 2. Study\n 3. Delete Flashcard\nChoose a number: ")
   
    while options:
        if options == "1":
            def create_cards(): 
                # print("Before studying, create some new flashcards.")
                flashcard_dict = {}

                go = "start"

                while go:
                    question = input("Enter new question or type 'Q' to end: ")
                    if question == "Q":
                        print("")
                        menu()
                    else:
                        answer = input("Enter new answer: ")
                        flashcard_dict[question] = answer
                        print("New flashcard created")
                        return flashcard_dict
            list_functions.append(create_cards())
            break
        
        elif options == "2":
             for i,(question, answer) in enumerate
            # def study(dictionary):
            #     flashcards = dictionary 
            #     length = len(flashcards)
            #     cards_missed = {}
            #     correct = 0
            #     for card in flashcards:
            #         print(card)
            #         input("")
            #         print(flashcards[card])  

        elif options == "3":
            # return options
            # answer = input("Do you want to see the menu again (yes or no): ")
            # if answer == "yes":
            #     list_functions[1]
            
            


def want_another():
            answer = input("Do you want to see the menu again (yes or no): ")
            if answer == "yes":
                list_functions[1]