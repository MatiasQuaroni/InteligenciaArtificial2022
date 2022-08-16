def VacuumCleanerAgentFunction(location,status):
    if status == "dirty":
        print("Cleaning")
        Clean()
    else:
        if location == "a":
            Right()
        elif location == "b":
            Left()

def Right():
    location = "b"

def Left():
    location = "a"

def Clean():
    status="clean"

VacuumCleanerAgentFunction("a","dirty")