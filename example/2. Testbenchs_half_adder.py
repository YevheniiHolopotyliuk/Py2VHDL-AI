# From this requirements definition we can write a natural language specification:
# “The circuit must add two binary inputs, producing two outputs. One output is the sum from the addition and the other is the carry.”

import os
import sys

from Classes.ChatGPT import *

from Classes.Entity_VHDL import *
from Classes.Architecture_VHDL import *

from Classes.VHDL_CONST import *


def tb():
    period = ns(20)
    count = int(156)

    a_tb = '0'
    b_tb = '1'

    wait(period)
    assert("sum_tb = 0", "carry_out_tb = 0")
    report("test failed for input combination 00", FAILURE) 
    
    ISR = a_tb and b_tb



create_logic = Entity(
    name_entity= "test_bench",

    port=[
        
    ],

    architecture=[
        Architecture.Signal("a_tb,b_tb,sum_tb,carry_out_tb", STD_LOGIC),
        Architecture.Process(tb),
    ]
)
