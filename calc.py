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
    Answer = order_of_op(MathParts)
    print "______________________"
    print Answer 
    print "\n"
    Arguments = []
