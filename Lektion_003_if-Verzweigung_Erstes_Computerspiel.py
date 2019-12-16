
import random

randomNumberToGuess = random.randint(1,10) # Zufallszahl von 1 bis einschließlich 10

print("\n\n\n")
print("\t################################")
print("\t## Unser erstes Computerspiel ##")
print("\t##       Zahlenraten !!!      ##")
print("\t################################")

while(True):  # <----------------------------------------------------------------------------------------
    while(True):   # <------------------------------------------------------------------                |
        try:                                                                         # |                |
            userNumber = int(input("\n\tRate meine Zahl zwischen 1 und 10  : "))     # |                |
            break  # Zeile 20 geht es weiter                                         # |                |
        except:                                                                      # |                |
            print("Das war keine Zahl....") #-------------------------------------------                |
                                                                                                      # |
    if userNumber == randomNumberToGuess:                                                             # |
        print("\n\n\n\tRichitg geraten. Die " + str(randomNumberToGuess) + " wurde gesucht.")         # |
        break                                                                                         # |
    else:                                                                                             # |
        print("\n\tversuche es nochmal.....") #----------------------------------------------------------

print("\n\tIch wünsche Dir einen schönen Tag. Bye Bye\n\n")