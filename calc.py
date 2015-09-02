#! /usr/bin/env python
######################
#Main file, runs calc#
######################

#########
#Imports#
#########
import sys
from operation import *
from read import *

###########
#Variables#
###########
#Input function
MathString = ""
#Holds numbers to put into operations
Arguments = list()
#Array of nums
IsNum = ["1","2","3","4","5","6","7","8","9","0","."]
#Arry of operations
IsOp = ["+","-","*","/","%","^"]
#Temp to hold arguments
TempArgument = list()
#End variables

#################################
#Query input and find operations#
#################################

print "\nWelcome to a simple calculator, type help to get a full list of commands and exit to exit the program.\n"

#While not exit, the leave condition, accept inputs
while (MathString != "exit" and MathString != "exit"):
    MathString = raw_input("")
    if (MathString == "exit" or MathString == "exit " or MathString == "Exit" or MathString == "Exit "):
        print "\nThank you, have a nice day.\n"
        sys.exit(0)
    MathParts = list(MathString)
    Arguments = read_string(MathParts)
    print "______________________"
    print operation(Arguments[1],Arguments[0],Arguments[2])
    print "\n"
    Arguments = []
