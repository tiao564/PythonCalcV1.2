#########################################
#Handles the reading of the string and  #
# order of operations                   #
#########################################

###########
#Variables#
###########
#Holds possible values to check against numbers
IsNum = ["1","2","3","4","5","6","7","8","9","0","."]
#Holds possible operations to check against
IsOp = ["+","-","*","/","%","^"]


def read_string(MathParts):
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
     
    return Arguments
