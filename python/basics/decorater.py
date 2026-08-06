""" decorater in python are the fuction we can use to modify the behaviour of other function or class. """

def decorater_function(original_function):
    def start():
        print("start")
        original_function()
  
        print("end")
    return start


@decorater_function
def goodbye():
    print("goodbye")

goodbye()