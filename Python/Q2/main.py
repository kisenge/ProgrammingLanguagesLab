# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



#Bug in Code- All puncuation needs space before and after
            # Repeating words breaks the code
            # Before replacing words, print the paragraph and it will show if there are straggling spaces,
            # infront of the keys. Failed to eliminate spaces.
            #unable to implement most common uncommon words- unable to process repeating words

def main():
    # Use a breakpoint in the code line below to debug your script.
    position = 0
    incrementor = 0
    startPos = 0
    paragraphDictionary = {}

    f = open('CommonWords.txt', 'r')
    txt= f.read()



    paragraphIn= input("Please input a paragraph:\n")
    print(paragraphIn)

    for elems in range(0, len(paragraphIn)):
        subString = paragraphIn[elems]
        print(subString)
        print("\n")
        if subString == " "  :
            position = position + 1
                #incrementor=incrementor+1
            stringSplice = paragraphIn[startPos:incrementor]
            paragraphDictionary.update({stringSplice: position})
            startPos = incrementor

        incrementor = incrementor + 1


    while (1):
        selection= input("\nMake a selection:\n"
                         +"\n\t R: Replace a Word"
                         +"\n\t D: Print the Dictionary"
                         + "\n\t P: Print the Paragraph"
                         +"\n\t C: Print Most Frequent Uncommon Word"
                         +"\n\t X: Exit the program.\n")
        #x=int(x)


        if selection== "D":

            for key,val in paragraphDictionary.items():
                print(key+"->["+"->",val,"]\n")


        if selection == "P":
           # for key, val in paragraphDictionary.items():
                #print(key)
                #print('where')
           print(paragraphDictionary.keys())


        if selection == "X":
            print("\nProgram exited successfully")
            exit()

        if selection == "R":
            replaceCount=0
            toReplace= input("What word would you like to replace\n")
            replacerWord= input("What word would you like to replace it with?\n")

            for key, val in paragraphDictionary.items():
                key2=key
                if key==toReplace:
                    paragraphDictionary[replacerWord] = paragraphDictionary.pop(key)
                    replaceCount = replaceCount + 1

                   # key=key2

                            #paragraphDictionary.update({replacerWord: val})

            print(replaceCount, "words were replaced")

        if selection == "C":
            commonWords = []
            commonwordsIncrementor = 0
            commonwordsInc=0
            mostCommon=""

            for entry in txt:
                for key in paragraphDictionary.items():
                    if entry== key:
                        commonWords[commonwordsIncrementor]=entry
                        commonwordsIncrementor= commonwordsIncrementor+1

                commonWordCount = []
                for val in commonWords:

                    commonWordCount.append(commonWords.count(val))

                min=0
                for val2 in commonWordCount:
                    if commonWordCount[val2]>min:
                        min= commonWordCount

                for minCount in commonWordCount:
                    if min==commonWordCount[minCount]:
                        mostCommon= commonWordCount[commonwordsInc]
                    commonwordsInc=commonwordsInc +1


                print("The most common word is" + mostCommon)
                f.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
