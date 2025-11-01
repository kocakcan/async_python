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
