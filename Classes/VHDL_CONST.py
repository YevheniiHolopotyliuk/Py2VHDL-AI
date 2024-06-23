# ENTITY
#  1.1 Bits and Vectors in Port
OUT = "out"
IN = "in"
INOUT = "inout"
BUFFER = "buffer"
LINKAGE = "linkage"
BIT = "bit"
STD_LOGIC = "std_logic"

def STD_VECTOR(from_bit,to_bit,type,additionally = []):

    if(len(additionally) > 0):
        text_additionally = ""

        for i in additionally:
            text_additionally += " " + i

        return "STD_VECTOR(" + str(from_bit) + " " + type + " " + str(to_bit) +")" + ":= " + text_additionally
    else:
        return "STD_VECTOR(" + str(from_bit) + " " + type + " " + str(to_bit) + ")"



# VECTOR
DOWN = "downto"
TO = "to"

# 1.2 Signals




# Architecture

# Logical 
def NOT():
    pass
def OR():
    pass
def wait():
    pass

# types of variable
def ns():
    pass

def int(name,value):
    return "int(" + name + "," + str(value) + ")"





# others
def report(val,type):
    pass

FAILURE = "FAILURE"

# class VHDL_CONST:

# #Entity
#     #Port

#     OUT = "out"
#     IN = "in"
#     STD_LOGIC = "std_logic"



