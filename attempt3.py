# Final ---------------------- v

grades = []
flashcards = {}
def create_cards(): 
      while True:
                    q = input("\nEnter new question or type 'Q' to quit: ")
                    if q.upper().strip() == "Q":
                        print("")
                        menu()
                        break
                    else:
                        a = input("Enter new answer: ")
                        flashcards[q] = a
                        print("Flashcard added!")
def study(flashcards):
                # flashcards = len(flashcards)
                # cards_missed = {}
                correct = 0    
                result = 0
                for question, answer in flashcards.items():
                    print(f"Question: {question}")
                    result = input("Answer: ")
                    # print(flashcards[question])  
                    if result.strip().lower() == answer.strip().lower():
                         correct += 1
                         print("Correct!\n")
                    else:
                        print(f"Wrong! The correct answer is: {answer}\n")
                grade = (correct / len(flashcards) * 100)
                score_calc(grade)
                    
                        # cards_missed[question] = flashcards[question]
                        # cards_missed.update()     
def menu(): 
    while True:
        options = input("Main Menu:\n " \
        "1. Create New Flashcard\n " \
        "2. Study\n " \
        "3. View Grades\n " \
        "4. Quit\n" \
        "Choose a number: ")
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
                if grades == []:
                      print("\nGrades: None\n")
                      
                else:
                      print(f"Grades: {grades}")
                # menu()
        
        elif options.strip() == "4":
              
              break
        
        else:
              print("\nPlease choose 1, 2, 3, or 4\n")

def score_calc(grade):
    if grade <= 100 and grade >= 90:
            grade = ("A")
    elif grade <= 89 and grade >= 80:
            grade = ("B")
    elif grade <= 79 and grade >= 70:
            grade = ("C")
    elif grade <= 69 and grade >= 60:
            grade = ("D")
    else:
            grade = ("F")
    print(f"Grade: {grade}")
    grades.append(grade)

menu()

