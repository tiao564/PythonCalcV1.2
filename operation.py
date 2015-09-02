##################################
#Holds and applys math operations#
##################################

#############################
#List of current operations #
#-Addition         "x+y"    #
#-Subtraction      "x-y"    #
#-Multiplication   "x*y"    #
#-Devision         "x/y"    #
#-Power            "x^y"    #
#############################

def operation(op,a,b):
        if(op=="+"):
		answer = a+b
		return answer
        if(op=="-"):
		answer = a-b
		return answer
        if(op=="*"):
		answer = a*b
		return answer
        if(op=="/"):
		answer = a/b
		return answer
        if(op=="%"):
                answer = a%b
                return answer
        if(op=="^"):
		answer = a**b
		return answer
