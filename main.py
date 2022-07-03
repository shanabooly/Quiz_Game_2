#Multiple Choice Quiz

guesses = 0
correct = 0

print("Welcome to my multiple choice quiz. There is a total of 3 questions.")

print("\n\nWhat is the capital city of Estonia?")
print("(a.) Tartu\n(b.) Narva\n(c.) Tallinn\n(d.) Paernu\n")
list1 = ['c', 'tallinn', '(c.)', 'c.', '(c)', 'talinn', 'tallin', 'talin']

answer = input("Enter answer: ")
if answer.lower() in list1:
    print("\nCorrect!\n")
    guesses += 1
    correct += 1

else:
    print("\nIncorrect!\n")
    guesses += 1
print(str(correct) + "/" + str(guesses))
print("_______________________________\n")

print("What is the capital city of Montenegro?")
print("(a.) Pljevlja\n(b.) Nikšić\n(c.) Cetinje\n(d.) Podgorica\n")
list2 = ['d', 'podgorica', '(d.)', 'd.', '(d)']

answer = input("Enter answer: ")
if answer.lower() in list2:
    print("\nCorrect!\n")
    guesses += 1
    correct += 1
else:
    print("\nIncorrect!\n")
    guesses += 1
print(str(correct) + "/" + str(guesses))
print("_______________________________\n")

print("What is the capital city of Moldova?")
print("(a.) Chișinău\n(b.) Tiraspol\n(c.) Bălți\n(d.) Tighina\n")
list3 = ['a', 'chișinău', '(a.)', 'a.', '(a)', 'chisinau']

answer = input("Enter answer: ")
if answer.lower() in list3:
    print("\nCorrect!\n")
    guesses += 1
    correct += 1
else:
    print("\nIncorrect!\n")
    guesses += 1
print(str(correct) + "/" + str(guesses))
print("_______________________________\n")

print("What is the capital city of Moldova?")
print("(a.) Prilep\n(b.) Kumanovo\n(c.) Bitola\n(d.) Skopje\n")
list4 = ['d', 'skopje', '(d.)', 'd.', '(d)']

answer = input("Enter answer: ")
if answer.lower() in list4:
    print("\nCorrect!\n")
    guesses += 1
    correct += 1
else:
    print("\nIncorrect!\n")
    guesses += 1
print(str(correct) + "/" + str(guesses))
print("_______________________________\n")

print("What is the capital city of Latvia?")
print("(a.) Jelgava\n(b.) Riga\n(c.) Rezekne\n(d.) Cesis\n")
list5 = ['b', 'riga', '(b.)', 'b.', '(b)']

answer = input("Enter answer: ")
if answer.lower() in list5:
    print("\nCorrect!\n")
    correct += 1
    guesses += 1
else:
    print("\nIncorrect!\n")
    guesses += 1
print("-------------------------------\n")
calc = round(correct / 5 * 100, 2)
print("Quiz over.\n\nFinal Score: " + str(correct) + "/" + str(guesses) +
      ". " + str(calc) + "%.")
print("\n_______________________________\n")
