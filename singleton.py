"""
	Singleton is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance.

	The Singleton pattern solves two problems at the same time, violating the Single Responsibility Principle:
	1) Ensure that a class has just a single instance. The most common reason for why anyone would want to control how many instances a class has is to control access to some shared resource-for example, a database or a file.

	2) Provide a global access point to that instance. Just like a global variable, the Singleton pattern lets you access some object from anywhere in the program. However, it also protects that instance from being overwritten by other code. There's another side to this problem: you don't want the code that solves problem #1 to be scattered all over your program. It's much better to have it within one class, especially if the rest of your code already depends on it.

	All implementations of the Singleton have these two steps in common:
	- Make the default constructor private, to prevent other objects from using the new operator with the Singleton class.
	- Create a static creation method that acts as a constructor. Under the hood, this method calls the private constructor to create an object and saves it in a static field. All following calls to this method return the cached object.

	If your code has access to the Singleton class, then it's able to call the Singleton's static method. So whenever that method is called, the same object is always returned.

	Applicability

	Use the Singleton pattern when a class in your program should have just a single instance available to all clients; for example, a single database object shared by different parts of the program.
	The Singleton pattern disables other means of creating objects of a class except for the special creation method. This method either creates a new object or returns an existing one if it has already been created.

	Use the Singleton pattern when you need stricter control over global variables.
	Unlike global variables, the Singleton pattern guarantees that there's just one instance of a class. Nothing, except for the Singleton class itself, can replace the cached instance.


	Pros and Cons
	
	+ You can be sure that a class has only a single instance.
	- Violates the Single Responsibility Principle. The pattern solves two problems at the same time.
	+ You gain a global access point to that instance.
	- The Singleton pattern can mask bad design, for instance, when the components of the program know too much about each other.
	+ The singleton object is initialized only when it's requested for the first time.
	- The pattern requires special treatment in a multithreaded environment so that multiple threads won't create a singleton object several times.
	- It may be difficult to unit test the client code of the Singleton because many test frameworks rely on inheritance when producing mock objects. Since the constructor of the singleton class is private and overriding static methods is impossible in most languages, you will need to think of a creative way to mock the singleton. Or just don't write the test, Or don't use the Singleton pattern
"""
class Singleton:
	_instance = None
	
	def __new__(cls):
		if cls._instance is None:
			cls._instance = super().__new__(cls)
		return cls._instance

class Example:
	def __new__(cls, *args, **kwargs):
		print("Inside __new__")
		# instance = super().__new__(cls)
		instance = object.__new__(cls)
		return instance

	def __init__(self):
		print("Inside __init__")

class Parent:
	def greet(self):
		print("Hello from Parent")

class Child(Parent):
	def greet(self):
		super().greet()
		print("Hello from Child")

def main():
	obj1 = Singleton()
	obj2 = Singleton()
	print(obj1 is obj2)
	example = Example()
	c = Child()
	c.greet()

if __name__ == "__main__":
	main()
