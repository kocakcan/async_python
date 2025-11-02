"""
Core Concept:
- The creational pattern that creates families of related objects without
  specifying their concrete classes
- Think of it as a "factory of factories"

Problem It Solves:
- When you need to ensure that created objects are compatible with each other
- When you want to create families of related objects (e.g., furniture sets in
  different styles)
- When you want to avoid tight coupling between concrete products and client
  code

Structure:
1. Abstract Products
- Interfaces for each type of product (e.g., Chair, Sofa, Table)
2. Concrete Products
- Actual implementations of these products (e.g., ModernChair, VictorianChair)
3. Abstract Factory
- Interface declaring creation methods for all abstract products
4. Concrete Factories
- Implementations of the abstract factory (e.g., ModernFurnitureFactory,
  VictorianFurnitureFactory)

Key Benefits:

1. Ensures product compatibility
2. Supports easy addition of new product families
3. Eliminates direct coupling between products and client code

Main Drawbacks:

- Can increase code complexity due to many interfaces and classes

When to Use:

- When your system needs to create multiple families of related objects
- When you want to ensure cross-product compatibility
- When you want to provide a library of products without exposing their
  limitations.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are
    usually able to collaborate among themselves. A family of products may have
    several variants, but the products of one variant are incompatible with
    products of another.
    """

    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible.
    Note that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """
