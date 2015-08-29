######################
#Main file, runs calc#
######################

#########
#Imports#
#########
import sys
from operation import *
#################################
#Query input and find operations#
#################################
###########
#Variables#
###########
#Input function
MathString = ""
#Holds numbers to put into operations
Arguments = list()
#Array of nums
IsNum = ["1","2","3","4","5","6","7","8","9","0"]
#Temp to hold arguments
TempArgument = list()
#End variables

print "\nWelcome to a simple calculator, type help to get a full list of commands and exit to exit the program.\n"

#While not exit, the leave condition, accept inputs
while (MathString != "exit" and MathString != "exit"):
    MathString = raw_input("")
    MathParts = list(MathString)
    for I in MathParts:
        if I in IsNum:
            TempArgument.append(I)
    TempArgument = "".join(TempArgument)
    float(TempArgument)
    print TempArgument
    
