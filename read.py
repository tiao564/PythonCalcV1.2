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
#Define order of Ops
MD = ["*","/","%"]
AS = ["+","-"]
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
    MathParts = do_Ops(MathParts, MD) 
    MathParts = do_Ops(MathParts, AS)
    MathParts = "".join(MathParts)
    return MathParts

#def read_string(MathParts):
#    List_len = len(MathParts)
#    Looper = 0
#    while iter < List_len:
#        if MathParts[iter] != " ":
#            if MathParts[iter] == "(":
#
#            elif MathParts[iter] == ")":

def do_Ops(MathParts, Ops):
    Looper = 0
    Arguments = []
    First_arg = []
    Secnd_arg = []
    while (Looper < len(MathParts)):
        if (MathParts[Looper] in Ops):
            First_arg = []
            Secnd_arg= []
            List_len = len(MathParts)
            Op = MathParts[Looper]                                                    #gets op
            First_num = Looper-1                                                    #starts pull for first number 
            Secnd_num = Looper+1                                                      #starts pull for second number
            First_bool = True
            Secnd_bool = True
            while First_bool == True:                                      #while the value is a num 
                if First_num != -1:
                    if MathParts[First_num] in IsNum:
                        First_arg.append(MathParts[First_num])                                #add to first num list
                        First_num = First_num-1                                               #decrement loop
                    else:
                            First_bool = False
                else:
                    First_bool = False
            while Secnd_bool == True:                                                 #while the value is a num
                if Secnd_num != List_len:
                    if MathParts[Secnd_num] in IsNum:
                        Secnd_arg.append(MathParts[Secnd_num])                                #add to second num list
                        Secnd_num = Secnd_num+1                                               #increment loop
                    else:
                        Secnd_bool = False
                else:
                    Secnd_bool = False
            InsertPoint = First_num+1                                                #save point to save answer back into array
            First_arg = list(reversed(First_arg))                                           #get the correct first value
            First_arg = "".join(First_arg)
            Secnd_arg = "".join(Secnd_arg)
            First_arg = float(First_arg)
            Secnd_arg = float(Secnd_arg)
            Insert = operation(Op, First_arg, Secnd_arg)                                           #get answer of equations
            Insert = str(Insert)
            Insert = list(Insert)

            Del_len = (Secnd_num-1)-(First_num+1)                                                #start point to remove from string
            Del = First_num+1
            Del_loop = 0                                                   #stop point to remove from string
            while (Del_loop <= Del_len):
              Value = MathParts[Del]                                            #get value to remove
              MathParts.remove(Value)                                                 #remove value
              Del_loop = Del_loop+1
            for num in Insert:
                MathParts.insert(InsertPoint, num)
                InsertPoint = InsertPoint+1
            Answer = "".join(MathParts)
            Looper = 0
        else:
            Looper = Looper+1
    return MathParts
