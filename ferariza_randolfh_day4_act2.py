
'''
1 Write a word bank program
2 The program will ask to enter a word
3 The program will store the word in a list
4 The program will ask if the user wants to try again. The user will input
  Y/y if yes and N/n if no
5 If yes, refer to step 2.
6 If no, Display the total number of words and all the words that user entered.
'''






wordList = []

a = (str(input("Please Enter a word: ")))
wordList.append(a)


question = input("Do you want to add more words?: ")


while question == "Y" or "Yes":
        print(a)
        if question == "N" or "no":
         break

print(wordList)
     

