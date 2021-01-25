

[Object-oriented programming (OOP)](https://en.wikipedia.org/wiki/Object-oriented_programming) is a programming paradigm based on the concept of objects, which may contain data, in the form of fields, often known as *attributes*; and code, in the form of procedures, often known as *methods*. This is often compared to [procedural programming](https://en.wikipedia.org/wiki/Procedural_programming) which structures a program like a recipe in that it provides a set of steps, and it is organized in routines or functions. Examples of procedural languages are Fortran, ALGOL, COBOL, BASIC, Pascal, C and Ada. Go is an example of a more modern procedural language, first published in 2009

Main properties
---------------

1. **Encapsulation**: in some OOP languages both attributes and methods are kept safe against misuse. For instance in C++ it is possible to declare methods as public, private, or protected. In other languages such as Python the encapsulation is only obtained by convention, adding an underscore behind the methods that should not be used.

2. **Inheritance**: objects can relate to each other with relationships like *has-a*, *uses-a* or *is-a*. A particular super-class is the *abstract* class used in C++ or C#. Abstract classes cannot be really instantiated, they can only be used as a super-class for other classes that extend the abstract class. This is also related to the concept of encapsulation, since an abstract class is not accessible.

3. **Polymorphism**: poly-morphism means many-forms.  Polymorphism manifests itself by having multiple methods all with the same name, but different functionality. There are two type of polymorphism, overriding and overloading. In *overriding* the method used is decided at runtime, based on the variables passed to the method itself. It is a language feature that allows a subclass to override a specific implementation of a method that is already provided by one of its super-classes. On the other hand, *overloading* determines the method used only at compile time. It is the ability to define several methods all with the same name. An example are operators like plus or minus that are treated as polymorphic functions and as such have different behaviours depending on the types of the arguments. At compile time the variables used by the operator are estimated and the correct method is associated to the operator.

4. **Abstraction**: it places the emphasis on what an object is or does rather than how it is represented or how it works. It reduces complexity by hiding irrelevant detail. It is a programming (and design) technique that relies on the separation of interface and implementation. An example could be a computer, you can use the keyboard to write a text file, you can regulate the monitor brightness but the internal functioning is hidden inside the case. You can use the interface, but the implementation is not directly accessible. In OOP the classes provide great level of abstraction giving methods to the outside world without actually showing how the class has been designed internally.


