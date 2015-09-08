#########################################
#Handles the reading of the string and  #
# order of operations                   #
#########################################
#########
#Imports#
#########
from operation import *
###########
#Variables#
###########
#Holds possible values to check against numbers
IsNum = ["1","2","3","4","5","6","7","8","9","0","."]
#Holds possible operations to check against
IsOp = ["+","-","*","/","%","^"]


def get_answer(MathParts):
    Arguments = list() 
    TempArgument = list()
    for Unit in MathParts:
        if Unit != " ":
            if Unit in IsNum:
                TempArgument.append(Unit)
            else:
                TempArgument = "".join(TempArgument)
                TempArgument = float(TempArgument)
                Arguments.append(TempArgument)
                TempArgument = []
        if Unit in IsOp:
             Arguments.append(Unit)
    TempArgument = "".join(TempArgument)
    TempArgument = float(TempArgument)
    Arguments.append(TempArgument)
    TempArgument = []
    Arguments.append(Unit) 
    answer = operation(Arguments[1],Arguments[0],Arguments[2])  #get answer
    print answer
    answer = str(answer)                                        #change to string
    print answer
    answer = list(answer)                                       #split into list
    print answer
    return answer

def order_of_op(MathParts):
    List_len = len(MathParts)
    print List_len
    Looper = 0
    Arguments = []
    First_arg = []
    Secnd_arg = []
    while (Looper < List_len):
        if (MathParts[Looper] == "*" or MathParts[Looper] == "/" or MathParts[Looper] == "%"):
            print"\n in main loop\n"
            Op = MathParts[Looper]                                                    #gets op
            First_num = Looper-1                                                      #starts pull for first number 
            Secnd_num = Looper+1                                                      #starts pull for second number
            while MathParts[First_num] in IsNum:                                      #while the value is a num 
                print "\n in first_num loop \n"
                First_arg.append(MathParts[First_num])                                #add to first num list
                First_num = First_num-1                                               #decrement loop
            InstertPoint = First_num+1                                                #save point to save answer back into array
            while (MathParts[Secnd_num] in IsNum) and Secnd_num != List_len:          #while the value is a num
                print "\n in second num loop \n"
                Secnd_arg.append(MathParts[Secnd_num])                                #add to second num list
                Secnd_num = Secnd_num+1                                               #increment loop
            if Secnd_num == List_len and MathParts[Secnd_num]:
                Secnd_arg.append(MathParts[Secnd_num])
            First_arg = reversed(First_arg)                                           #get the correct first value
            Arguments = [First_arg, Op, Secnd_arg]        
            Instert = get_answer(Arguments)                                           #get answer of equations
            Del_start = First_num+1                                                   #start point to remove from string
            Del_end   = Secnd_num-1                                                   #stop point to remove from string
            while (First_num < Secnd_num):
              Value = MathParts[First_num]                                            #get value to remove
              MathParts.remove(Value)                                                 #remove value
              First_num = First_num+1                                                 #increment loop
            MathParts.insert(InsertPoint, Insert)
            Answer = "".join(MathParts)
            Looper = 0
        else:
            Looper = Looper+1
            
    Answer = float(Answer)
    return Answer


   
#def read_string(MathParts):
#    List_len = len(MathParts)
#    Looper = 0
#    while iter < List_len:
#        if MathParts[iter] != " ":
#            if MathParts[iter] == "(":
#
#            elif MathParts[iter] == ")":






