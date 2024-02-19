# __init__ methods
# The __init__ method for initialization is invoked without any call,
# when an instance of a class is created, like constructors in certain other programming languages such as C++, Java, C#, PHP, etc.


# declare our own string class
class String:
    # magic method to initiate object
    def __init__(self, string):
        self.string = string


# Driver Code
if __name__ == "__main__":
    # object creation
    string1 = String("Hello")

    # print object location
    print(string1)
