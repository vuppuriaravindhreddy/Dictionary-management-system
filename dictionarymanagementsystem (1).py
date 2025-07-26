#dictionary management
dictionary={}
while True:
    print("1.Add a word:")
    print("2.Search for a meaning:")
    print("3.Display all words:")
    print("4.update meaning:")
    print("5.delete the word")
    print("6.exting the program")
         
    choice=input("enter the choice:")

    if choice=="1":
        word=input("enter the word:").lower()
        meaning=input("enter the meaning:").lower()
        dictionary[word]=meaning
        print("word added successfully")


    elif choice=="2":
        word=input("enter the word:")
        if word in dictionary:
            print("meaning:",dictionary[word])
        else:
            print("word not found in dictionary")

    elif choice=="3":
            print(dictionary.items())

    elif choice=="4":
        word=input("enter the word:")
        if word in dictionary:
            new_meaning=input("enter the new meaning:")
            dictionary[word]=new_meaning
            print("meaning updated successfuly")
            print(f"updated meaning is {word} is {dictionary[word]}")
        if word not in dictionary:
          print("word not found in dictionary:")

    elif choice=="5":
       word=input("enter the word:").lower()
       if word in dictionary:
          dictionary.pop(word)
          print(dictionary)
       if word not in dictionary:
           print("word not found")

    elif choice=="6":
           print("exiting the program...")
           break
    else:
        print("entered invalid choice")