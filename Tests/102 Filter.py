# https://www.fpga4student.com/2017/07/16-bit-alu-design-in-vhdl.html

from Classes.py2vhdl import *

# Global var

def process(ALUctrl,ABUS,BBUS,tmp_out1,tmp):
    # Case VHDL
    if ALUctrl == "0000":
        ALUOUT = tmp_out1
    elif ALUctrl == "0001":
        ALUOUT = tmp
    elif ALUctrl == "0010":
        ALUOUT = ABUS and BBUS
    elif ALUctrl == "0011":
        ALUOUT = ABUS or BBUS
    elif ALUctrl == "0100":
        ALUOUT = xor(ABUS,BBUS)
    elif ALUctrl == "0101":
        ALUOUT = not ABUS
    elif ALUctrl == "0110":
        ALUOUT = not ABUS
    elif "others":
        ALUOUT = tmp_out1


Entity(
    name_entity= "FILTER",

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
        Generic_map(
            "u1_N_bit_adder",
            "N_bit_adder",
            [
                var("input1","ABUS"),
                var("input2","BBUS"),
                var("answer","tmp_out1 ")
            ]
        ),
        Generic_map(
            "u2_N_bit_adder",
            "N_bit_adder",
            [
                var("input1","ABUS"),
                var("input2","BBUS_not"),
                var("answer ","tmp_out2")
            ]
        ),
        Generic_map(
            "u3_N_bit_adder",
            "N_bit_adder",
            [
                var("input1","tmp_out2"),
                var("input2",'x"0001"'),
                var("answer ","tmp")
            ]
        ),
        var("BBUS_not","not BBUS"),
        # Body(),
        Process(process),

    ]
)