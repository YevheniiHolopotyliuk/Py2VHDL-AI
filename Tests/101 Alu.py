# https://www.fpga4student.com/2017/07/16-bit-alu-design-in-vhdl.html

from Classes.py2vhdl import *

# Global var
N = 0

def body():


def process(ALUctrl,ABUS,BBUS,tmp_out1,tmp):
    if lang == "JavaScript":
        return "You can become a web developer."
    elif lang == "PHP":

Entity(
    name_entity= "ALU",

    port=[
        Port("ABUS,BBUS",IN, STD_VECTOR(15,0,DOWN)),
        Port("ALUctrl",IN, STD_VECTOR(3,0,DOWN)),
        Port("ALUOUT",OUT, STD_VECTOR(15,0,DOWN)),
    ],
    architecture=[

        Component(
            "N_bit_adder",
            [
                Generic([
                    int("N",32),
                ]),
                Port("input1,input2", IN, STD_VECTOR("N-1",0,DOWN)),
                Port("answer", OUT , STD_VECTOR("N-1",0,DOWN)),
            ]
        ),
        Signal("BBUS_not, tmp_out1, tmp_out2, tmp", STD_VECTOR("16-1",0,DOWN)),
        Body(),
        Process()

    ]
)