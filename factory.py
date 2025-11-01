"""
	Intent

	Factory Method is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

	Imagine that you're creating a logistics management application. The first version of your app can only handle transportation by trucks, so the bulk of your code lives inside the Truck class.

	After a while, your app becomes pretty popular. Each day you receive dozens of requests from sea transportation companies to incorporate sea logistics into the app.

	Adding Ships into the app would require making changes to the entire codebase. Moreover, if later you decide to add another type of transportation to the app, you will probably need to make all of these changes again.

	As a result, you will end up with pretty nasty code, riddled with conditionals that switch the app's behaviour depending on the class of transportation objects.

	Solution

	The Factory Method pattern suggests that you replace direct object construction calls (using the new operator) with calls to a special factory method. The objects are still created via the new operator, but it's being called from within the factory method. Objects returned by a factory method are often referred to as products.

	At first glance, this change may look pointless: we just moved the constructor call from one part of the program to another. However, consider this: now you can override the factory method in a subclass and change the class of products being created by the method.

	There's a slight limitation though: subclasses may return different types of products only if these products have a common base class or interface. Also, the factory method in the base class should have its return type declared as this interface.

	For example, both Truck and Ship classes should implement the Transport interface, which declares a method called deliver. Each class implements this method differently: trucks deliver cargo by land, ships deliver cargo by sea. The factory method in the RoadLogistics class returns truck objects, whereas the factory method in the SeaLogistics class return ships.

	The code that uses the factory method (often called the client code) doesn't see a difference between the actual products returned by various subclasses. The client treats all the products as abstract Transport. The client knows that all transport objects are supposed to have the deliver method, but exactly how it works isn't important to the client.	 
	Structure

	1. The Product declares the interface, which is common to all objects that can be produced by the creator and its subclasses.
	2. Concrete Products are different implementations of the product interface.
	3. The Creator class declares the factory method that returns new Product objects. It's important that the return type of this method matches the Product interface.

	You can declare the factory method as abstract to force all subclasses to implement their own versions of the method. As an alternative, the base factory method can return some default product type.

	Note, despite its name, product creation is not the primary responsibility of the Creator. Usually, the Creator class already has some business logic related to Products. The factory method helps to decouple this logic from the concrete product classes. 

	Applicability

	Use the Factory Method when you don't know beforehand the exact types and dependencies of the objects your code should work with.
	The Factory Method seperates product construction code from the code that actually uses the product. Therefore, it's easier to extend the product construction code independently from the rest of the code. For example, to add a new product type to the app, you'll only need to create a new creator subclass and override the factory method on it.

	Use the Factory Method when you want to provide users of your library or framework with a way to extend its internal components.
	Inheritance is probably the easiest way to extend the default behaviour of a library of framework. But how would the framework recognize that your subclass should be used instead of a standard component? The solution is to reduce the code that constructs components across the framework into a single factory method and let anyone override this method in addition to extending the component itself. 

	Use the Factory Method when you want to save system resources by reusing existing objects instead of rebuilding them each time.
	You often experience this need when dealing with large, resource-intensive objects such as database connections, file systems, and network resources.
	
	How to Implement

	1. Make all products follow the same interface. This interface should declare methods that make sense in every product.
	2. Add an empty factory method inside the creator class. The return type of the method should match the common product interface.
	3. In the creator's code find all references to product constructors. One by one, replace them with calls to the factory method, while extracting the product creation code into the factory method.
	4. Now, create a set of creator subclasses for each type of product listed in the factory method. Override the factory method in the subclasses and extract the appropriate bits of construction code from the base method.
	5. If there are too many product types and it doesn't make sense to create subclasses for all of them, you can reuse the control parameter from the base class in subclasses.
	6. If, after all of the extractions, the base factory method has become empty, you can make it abstract. If there's something left, you can make it a default behaviour of the method.

	Pros and Cons

	+ You avoid tight coupling between the creator and the concrete products.
	- The code may become more complicated since you need to introduce a lot of new subclasses to implement the pattern. The best case scenario is when you're introducing the pattern into an existing hierarchy of creator classes.
	+ Single Responsibility Principle. You can move the product creation code into one place in the program, making the code easier to support.
	+ Open/Closed Principle. You can introduce new types of products into the program without breaking existing client code.
"""
from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
	"""
	The Creator class declares the factory method that is supposed to return an object of a Product class. The Creator's subclasses usually provide the implementation of this method.
	"""
	@abstractmethod
	def factory_method(self):
		"""
		Note that the Creator may also provide some default implementation of the factory method.
		"""
		pass

	def some_operation(self) -> str:
		"""
		Also note that, despite its name, the Creator's primary responsibility is not creating products. Usually, it contains some core business logic that relies on Product objects, returned by the factory method. Subclasses can indirectly change the business logic by overriding the factory method and returning a different type of Product from it.
		"""
		# Call the factory method to create a Product object.
		product = self.factory_method()
		# Now, use the product.
		result = f"Creator: The same creator's code has just worked with {product.operation()}"
		return result

"""
Concreate Creators override this factory method in order to change the resulting Product's type.
"""

class ConcreteCreator1(Creator):
	"""
	Note that the signature of the method still uses the abstract Product type, even though the concrete product is actually returned from the method. This way the Creator can stay independent of concrete product classes.
	"""
	def factory_method(self) -> Product:
		return ConcreteProduct1()

class ConcreteCreator2(Creator):
	def factory_method(self) -> Product:
		return ConcreteProduct2()

class Product(ABC):
	"""
	The Product interface declares the operations that all concrete products must implement.
	"""
	@abstractmethod
	def operation(self) -> str:
		pass

"""
Concrete Products provide various implementations of the Product interface.
"""
class ConcreteProduct1(Product):
	def operation(self) -> str:
		return "{Result of the ConcreteProduct1}"

class ConcreteProduct2(Product):
	def operation(self) -> str:
		return "{Result of the ConcreteProduct2}"

def client_code(creator: Creator) -> None:
	"""
	The client code works with an instance of a concrete creator, albeit through its base interface. As long as the client keeps working with the creator via the base interface, you can pass it any creator's subclass.
	"""
	print(f"Client: I'm not aware of the creator's class, but it still works.\n"
	      f"{creator.some_operation()}", end="")

if __name__ == "__main__":
	print("App: Launched with the ConcreteCreator1.")
	client_code(ConcreteCreator1())
	print("\n")

	print("App: Launched with the ConcreteCreator2.")
	client_code(ConcreteCreator2())
	print("\n")
