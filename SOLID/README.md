# SOLID
## Single-responsibility principle (SRP)
### This principle comes from Robert C.Martin, known by Uncle Bob
- The single-responsibility principle states that: </br>
`A class should have only one reason to change.`
- This means that a class should have only one responsibility, as expressed through its methods. If a class takes care of more than one task, then you should separate those tasks into separate classes. </br>
- This principle is closely related to the concept of separation of concerns, which suggests that you should split your programs into different sections. Each section must address a separate concern. </br>
- To illustrate this principle, follow [S]-[Before]-Example.py and [S]-[After]-Example.py </br>
#### In [S]-[Before]-Example.py
- FileManager class has 2 different responsibilites. It uses the .read() and .write() methods to manage the file. </br>
- It also deals with ZIP archives by providing the .compress() and .decompress() methods. </br> 
=> Therefore, this class violates the S principle because it has 2 reasons for changing its internal implementation. </br>
- To fix this issue and make your design more robust, split the class into 2 smaller, more focused classes.  
#### In [S]-[After]-Example.py
- We have two smaller classes, each having only a single responsibility. FileManager takes care of managing a file, while ZipFileManager handles the compression and depression of a file using ZIP format. These 2 classes are smaller, so they're more manageable. They are also easier to reason about, test and debug.