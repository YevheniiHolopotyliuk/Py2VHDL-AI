import os
import sys
print(sys.path)

from Classes.ChatGPT import *
from Classes.Entity_VHDL import *

from Classes.ChatGPT import *

# GPT tests
# gpt_test = ChatGPT()
# text =  gpt_test.response("")


# create_logic = [
#     "entity" = [
#         "port" = [
#             "in_port1" = "in std_logic",
#             "in_port2" = "in std_logic",
#
#             "out_port1" = "out std_logic",
#             "out_port2" = "out std_logic",
#         ]
#     "archicture" = ""
#     ]
# ]

def process_and(in_port1, in_port2):
    return Entity.text_to_code_GPT("For y_out need set input_1 and input_2 with logical element 'and' ")

def process_mux(in_port1,in_port2,in_port3):
    if in_port1  == 0:
        in_port3 = in_port2
    else:
        in_port2 = in_port3

def process_or(in_port1,in_port2,in_port3):

    if(in_port3 == 1):
        in_port3 = in_port1 or in_port2

create_logic = Entity(
    name_entity= "logic_cort",

    port=[
        Entity.Port("in_port1", VHDL_CONST.IN, VHDL_CONST.STD_LOGIC),
        Entity.Port("in_port2", VHDL_CONST.IN, VHDL_CONST.STD_LOGIC),
        Entity.Port("in_port3", VHDL_CONST.IN, VHDL_CONST.STD_LOGIC),
        Entity.Port("out_port2", VHDL_CONST.OUT, VHDL_CONST.STD_LOGIC),
    ],

    architecture=[
        Entity.Process(process_mux),
        Entity.Process(process_or),
        Entity.Process(process_and),

    ]
)

# create_logic = Entity(
#     entity = [
#         "port" = [
#           Port("in_port1", in, std_logic),
#           Port("in_port1", in, std_logic),
#           Port("out_port1",out, std_logic),
#           Port("out_port2",out, std_logic),
#         ],
#     ],
#     architecture = [
#         # function_prompt = "Checking in ports and equal for outs with inputs of variables",
#         body = [
#             Process(
#                  process_mux: process(B, S, A)
#                  begin
#                       if S = '0' then
#                           Y <= A;
#                       else
#                           Y <= B;
#                       end if;
#                   end process process_mux;
#             )
#         ]
#     ]
# )

#
# logic_cort = Entity( entity = [
#     "port" = [  Port("in_port1",in,std_logic)
#                 Port("in_port1",in,std_logic)
#                 Port("out_port1",out,std_logic)
#                 Port("out_port2",out,std_logic)
#             ]           ]
#  "architecture" = [
#  "body" = [  Process("def process_mux(B,S,A):
#     if S == 0:
#         Y = A
#     else:
#         Y = B
# ")
# ]])