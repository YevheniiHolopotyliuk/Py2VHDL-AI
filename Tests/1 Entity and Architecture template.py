from Classes.py2vhdl import *

create_logic = Entity(
    name_entity= "logic_cort",
    port=[
        Port("in_1",IN,STD_LOGIC),
        Port("out_1, out_2", OUT, STD_LOGIC)
    ],
    architecture=[
        
    ]
)

