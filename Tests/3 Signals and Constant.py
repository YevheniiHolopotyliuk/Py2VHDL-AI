from Classes.py2vhdl import *

def body():
    pass
create_logic = Entity(
    name_entity= "logic_cort",

    port=[


    ],
    architecture=[
        Signal("sig_vec", STD_VECTOR(3,0,DOWN)),
        Constant("init_2",STD_VECTOR(3,0,DOWN,["1100"])),
        Constant("init_3",STD_LOGIC),
        Body(body),
    ]
)