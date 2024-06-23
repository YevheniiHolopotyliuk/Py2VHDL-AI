from Classes.py2vhdl import *

def body(in_1,in_2,out_1):
    if in_1 > 0 :
        out_1 =in_1

    if in_1 < 0:
        out_1 = in_1 + in_2

    if in_2 >= in_1:
        out_1 = in_2

    if in_1 != 13:
        out_1 = in_1 + in_2

    if in_1 == in_2 and in_1 > 34:
        out_1 = 0

create_logic = Entity(
    name_entity= "logic_cort",

    port=[
        Port("in_1,in_2",IN, STD_LOGIC),
        Port("out_1",IN, STD_LOGIC)

    ],
    architecture=[
        Body(body)
    ]
)