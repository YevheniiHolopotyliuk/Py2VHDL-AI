from Classes.ChatGPT import *
from Classes.VHDL_CONST import *
import inspect

class Architecture:

    def __init__(self, ):

        print("Init Arch")

    @staticmethod
    def Process(function_do,gpt_request = False):

        if(gpt_request == False):
            lines = inspect.getsource(function_do)
            return "Process(\"" + lines + "\")\n"

        if(gpt_request == True):
            return function_do
        

    @staticmethod
    def Body(function_do,gpt_request = False):
        if(gpt_request == False):
            lines = inspect.getsource(function_do)
            return lines + ")\n"

        if(gpt_request == True):
            return function_do
        
    @staticmethod
    def Signal(names,type):
        return "Signal("+names+","+type+")"