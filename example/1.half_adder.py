# From this requirements definition we can write a natural language specification:
# “The circuit must add two binary inputs, producing two outputs. One output is the sum from the addition and the other is the carry.”

import os
import sys


from Classes.ChatGPT import *

from Classes.Entity_VHDL import *
from Classes.Architecture_VHDL import *

  


def dataflow():
    sum = (NOT(a) * b) + (a * NOT(b))
    carry_out = a * b

create_logic = Entity(
    name_entity= "logic_cort",

    port=[
        Entity.Port("a,b", IN, STD_LOGIC),
        Entity.Port("sum,carry_out", OUT, STD_LOGIC),
    ],

    architecture=[
        Architecture.Body(dataflow),
    ]
)
