from Classes.py2vhdl import *


create_logic = Entity(
    name_entity= "logic_cort",

    port=[
        Port("in_1,in_2",IN,STD_VECTOR(7,0,DOWN)),
        Port("in_3,in_4",IN,STD_LOGIC),
        Port("in_5,in_6",IN,STD_VECTOR(31,1,DOWN, ["others","1"])),
        Port("out_1",OUT,STD_LOGIC),

    ],
    architecture=[
        # Architecture.Signal()
    ]
)