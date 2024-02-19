## Python Dunder/Magic methods
- Dunder means Double UnderScore </br>
- Also call Magic Methods </br>
- Built in classes of python </br> 
- They are defined by built-in classes in Python and commonly used for operator overloading. </br>
- Starting and Ending with underscore (__magic_methods__) </br> 
### To Show magic methods inherited by class
`print(dir(int))`
or `dir(int)` in python terminal.

## Uses of Magic Methods
### Initialization and Construction
- `__new__`: To get called in an object’s instantiation.</br>
- `__init__`: To get called by the __new__ method. </br>
- `__del__`: It is the destructor. </br>

### Numeric magic methods
- `__trunc__(self)`: Implements behavior for math.trunc() </br>
- `__ceil__(self)`: Implements behavior for math.ceil()
- `__floor__(self)`: Implements behavior for math.floor()
- `__round__(self,n)`: Implements behavior for the built-in round() </br>
... </br>

### Arithmetic operators
- `__add__(self, other)`: Implements behavior for math.trunc() </br>
- `__sub__(self, other)`: Implements behavior for math.ceil()
- `__mul__(self, other)`: Implements behavior for math.floor()
- `__floordiv__(self, other)`: Implements behavior for the built-in round()
- `__div__(self, other)`: Implements behavior for inversion using the ~ operator. </br>
... </br>

### String Magic Methods
- `__str__(self)`: Defines behavior for when str() is called on an instance of your class. </br>
- `__repr__(self)`: To get called by built-int repr() method to return a machine readable representation of a type. </br>
... </br>

### Comparison magic methods
- `__eq__(self, other)`: Defines behavior for the equality operator, ==.
- `__ne__(self, other)`: Defines behavior for the inequality operator, !=. </br>
... </br>