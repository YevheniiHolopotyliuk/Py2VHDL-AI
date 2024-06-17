from Classes.ChatGPT import *
from Classes.VHDL_CONST import *
import inspect

class Entity:

    def __init__(self, name_entity, port = "" , architecture = "" ):

        # Attributes set
        self.name_entity = name_entity
        self.port = port
        self.architecture = architecture
        self.gpt = ChatGPT()

        # Code VHDL creating
        self.PYTHON_CODE = ""
        self.VHDL_CODE = ""
        self.elements_init()

        # Entity header creating (Entity)
        self.PYTHON_CODE =  self.create_entity_header(port)

        # Archicture (Entity)
        self.PYTHON_CODE += self.create_arch(architecture)

        # Print results
        print(self.PYTHON_CODE)
        print(self.VHDL_entity_header(self.PYTHON_CODE))


        # self.VHDL_CODE = self.VHDL_entity_header(self.PYTHON_CODE)

    # Create architecture
    def create_entity_header(self, port):
        entity_header_python = ""
        # If port hasnt 
        if(len(port)  <= 0):
            entity_header_python= self.beggin_entity + self.beggin_header_entity
            entity_header_python += self.beggin_header_end + self.end_entity
        # Port checking on number
        if(len(port) > 1):
            # Creating begin text of part for VHDL
            entity_header_python= self.beggin_entity + self.beggin_header_entity + self.beggin_port
            for el_port in port:
                entity_header_python += el_port

            # Creating end of part for VHDL
            entity_header_python += self.end_port + self.beggin_header_end + self.end_entity

        return entity_header_python

    def create_arch(self, body):

        arch_python = self.architecture_begin + self.architecture_body_begin

        for el in body:
            arch_python += el

        arch_python += self.architecture_body_end + self.architecture_end

        print(arch_python)
        # Creating end of part for VHDL

        return arch_python

    @staticmethod
    def text_to_code_GPT(text_to_code):
        prompt = "Convert text to Python code. \" " + text_to_code + "\""
        return ChatGPT.response(prompt)

    @staticmethod
    def Python_to_VHDL_full(code):
        prompt = "Convert code from Python to VHDL: \n" + code
        return ChatGPT.response(prompt)
    
    def VHDL_entity_header(self, code):
        prompt = "Convert code from Python to VHDL and create Entity and add library: \n" + code
        return ChatGPT.response(prompt)

    def VHDL_entity_process(self,code):
        prompt = "Convert code from Python to VHDL and create Process: \n" + code
        return ChatGPT.response(prompt)
    #
    #
    @staticmethod
    def Port(port_signal_name , input_output,port_signal_type = "" ):
        # Data area for checking all situations for inputing attributes
        port_end = ""

        if(port_signal_type != ""):
            port_end = ","+ port_signal_type
        else:
            port_end = ""

        # print("Port(\""+ port_signal_name +"\","+input_output + port_end +")")
        return "Port(\""+ port_signal_name +"\","+input_output + port_end +") \n"

    # Migration to "Architeture_VHDL.py"
    # @staticmethod
    # def Process(function_do,gpt_request = False):

    #     if(gpt_request == False):
    #         lines = inspect.getsource(function_do)
    #         return "Process(\"" + lines + "\")\n"

    #     if(gpt_request == True):
    #         return function_do

        # If need for remove first line that init attributes and name of function
        # postString = lines.split("\n", 1)[1]
        # print(postString)



    # Elements for convert
    def elements_init(self):
        # Entity ------------------------------------------------
        self.beggin_entity = (
            self.name_entity + " = Entity( "
        )
        self.end_entity = ")"

        self.beggin_header_entity = "entity = ["
        self.beggin_header_end = "]"

        # End Entity

        # Port
        self.beggin_port = "\n \"port\" = [  "
        self.end_port = "]"
        # End Port

        # End Entity ----------------------------------------------

        # Architecture --------------------------------------------
        self.architecture_begin = "\n \"architecture\" = [  "
        self.architecture_end = "]"

        self.architecture_body_begin = "\n \"body\" = [  "
        self.architecture_body_end = "]"

        # Process

        # End Process

        # End Architecture ----------------------------------------




