from __future__ import annotations
from abc import ABC, abstractmethod

class ArmourCreator(ABC):
	@abstractmethod
	def factory_method(self):
		pass

	def get_durability(self):
		product = self.factory_method()
		result = f"Durability: {product.durability()}"
		return result

class HelmetCreator(ArmourCreator):
	def factory_method(self):
		return Helmet()

class PauldronCreator(ArmourCreator):
	def factory_method(self):
		return Pauldron()

class Armour(ABC):
	@abstractmethod
	def durability(self):
		pass

class Helmet(Armour):
	def durability(self):
		return f"Helmet durability: 300/300"

class Pauldron(Armour):
	def durability(self):
		return f"Pauldron durability: 400/400"

def client_code(creator: ArmourCreator) -> None:
	print(f"Client: I'm not aware of the creator's class, but it still works.\n"
f"{creator.get_durability()}", end="")

if __name__ == "__main__":
	print("App: Launched with HelmetCreator.")
	client_code(HelmetCreator())
	print("\n")

	print("App: Launched with PauldronCreator.")
	client_code(PauldronCreator())
	print("\n")
