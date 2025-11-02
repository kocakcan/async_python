"""
	Intent

	Absract Factory is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.

	Problem

	Imagine that you're creating a furniture shop simulator. Your code consists of classes that represent:
	1. A family of related products, say: Chair + Sofa + CoffeeTable.
	2. Several variants of this family. For example, products Chair + Sofa + CoffeeTable are available in these variants: Modern, Victorian, ArtDeco.

	You need a way to create individual furniture objects so that they match other objects of the same family. Customers get quite mad when they receive non-matching furniture.
