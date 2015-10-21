
import os

import time


WIDTH = 100


message = "dead memories".upper()

printedMessage = [ "","","","","","","","","","","","","",""]


characters = { " " : [ " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " " ],

               "E" : [ "*****",
                       "*    ",
                       "*    ",
                       "*****",
                       "*    ",
                       "*    ",
                       "*****" ],
               
               "D" : [ "***  ",
                       "*  * ",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*  * ",
                       "***  " ], 

               "O" : [ "*****",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*****" ],

               "A" : [ "  *  ",
                       " * * ",
                       "*   *",
                       "*****",
                       "*   *",
                       "*   *",
                       "*   *" ],

               "R" : [ "***  ",
                       "*   *",
                       "*   *",
                       "**** ",
                       "*   *",
                       "*   *",
                       "*   *" ],

                "S" : ["*****",
                       "*    ",
                       "*    ",
                       "*****",
                       "    *",
                       "    *",
                       "*****"],

                "M" : ["*     *",
                       "*     *",
                       "* * * *",
                       "*  *  *",
                       "*     *",
                       "*     *",
                       "*     *"],

                "I" : ["  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  "]
               
               }



try:
    # the code that can cause the error
    for row in range(14):
        for char in message:
            printedMessage[row] += (str(characters[char][row]) + "  ")

except IndexError: # catch the error
    pass # pass will basically ignore it
         # and execution will continue on to whatever comes
         # after the try/except block

offset = WIDTH
while True:
    os.system("cls")
    for row in range(14):
        print(" " * offset + printedMessage[row][max(0,offset*-1):WIDTH - offset])

    offset -=1

    if offset <= ((len(message)+2)*13) * -1:
        offset = WIDTH
