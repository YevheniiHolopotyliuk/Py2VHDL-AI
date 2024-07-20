import inspect
def Port(port_signal_name, input_output, port_signal_type=""):
    # Data area for checking all situations for inputing attributes
    port_end = ""

    if (port_signal_type != ""):
        port_end = "," + port_signal_type
    else:
        port_end = ""

    # print("Port(\""+ port_signal_name +"\","+input_output + port_end +")")
    return "Port(\"" + port_signal_name + "\"," + input_output + port_end + ") \n"

def Process(function_do, gpt_request=False):

    if (gpt_request == False):
        lines = inspect.getsource(function_do)
        return "Process(\"" + lines + "\")\n"

    if (gpt_request == True):
        return function_do


def Body(function_do, gpt_request=False):
    if (gpt_request == False):
        lines = inspect.getsource(function_do)
        return lines + ")\n"

    if (gpt_request == True):
        return function_do


def Signal(port_signal_name, port_signal_type=""):
    return "Signal(\"" + port_signal_name + "," + port_signal_type + ") \n"

def Constant(port_signal_name, port_signal_type=""):
    return "Constant(\"" + port_signal_name + ","  + port_signal_type + ") \n"

def Generic(elements = []):

    if (len(elements) > 0):

        list_of_elemetns = ""
        for el in elements:
            list_of_elemetns += el

        return "Generic (" + list_of_elemetns + ") \n"

    if (len(elements) == 0):
        return ""


# Add name for Component
def Component(name ="",elements = []):
    if(len(elements) > 0):
        list_of_elemetns = ""
        for el in elements:
            list_of_elemetns += el
        # return "Component "+name+" ("+list_of_elemetns+") \n"
        return "component "+ name + " (" + list_of_elemetns + ") \n"
    if(len(elements) == 0):
        return ""


def var(name, variable):
    return name+ " => "+ variable+ "  "

def Generic_map(name ="", to_element ="", map = [], port = []):
    if(len(map) > 0):
        list_of_map = ""

        for el in map:
            list_of_map += el

        list_of_port = ""

        for el in list_of_port:
            list_of_port += el

        # return "Component "+name+" ("+list_of_elemetns+") \n"
        return name+" : "+  to_element +"generic map (" + list_of_map + ") port map("+list_of_port+"); \n"
    if(len(map) == 0):
        return ""


