'''
1 Write a word bank program
2 The program will ask to enter a word
3 The program will store the word in a list
4 The program will ask if the user wants to try again. The user will input
  Y/y if yes and N/n if no
5 If yes, refer to step 2.
6 If no, Display the total number of words and all the words that user entered.

'''
<<<<<<< HEAD
=======
1 Write a word bank program
2 The program will ask to enter a word
3 The program will store the word in a list
4 The program will ask if the user wants to try again. The user will input
  Y/y if yes and N/n if no
5 If yes, refer to step 2.
6 If no, Display the total number of words and all the words that user entered.
'''





>>>>>>> 4f0a6fb087d8f2ddb4b87fea98c0c42a7cbbfbc8

wordList = []

a = (str(input("Please Enter a word: ")))
wordList.append(a)


question = input("Do you want to add more words?: ")

<<<<<<< HEAD
if question == True:
        print(str(input("Please Enter a word: ")))
else: wordList.append(a)
=======

while question == "Y" or "Yes":
        print(a)
        if question == "N" or "no":
         break

print(wordList)
>>>>>>> 4f0a6fb087d8f2ddb4b87fea98c0c42a7cbbfbc8
     

