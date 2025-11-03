from abc import ABC, abstractmethod


class SUV(ABC):
    @abstractmethod
    def drive(self):
        pass


class Sedan(ABC):
    @abstractmethod
    def drive(self):
        pass


class WhiteSUV(SUV):
    def drive(self):
        return "Riding a white SUV"


class WhiteSedan(Sedan):
    def drive(self):
        return "Riding a white Sedan"


class DarkSUV(SUV):
    def drive(self):
        return "Riding a dark SUV"


class DarkSedan(Sedan):
    def drive(self):
        return "Riding a dark Sedan"


class CarFactory(ABC):
    @abstractmethod
    def create_suv(self):
        pass

    @abstractmethod
    def create_sedan(self):
        pass


class WhiteCarFactory(CarFactory):
    def create_suv(self):
        return WhiteSUV()

    def create_sedan(self):
        return WhiteSedan()


class DarkCarFactory(CarFactory):
    def create_suv(self):
        return DarkSUV()

    def create_sedan(self):
        return DarkSedan()


def create_car(factory: CarFactory):
    suv = factory.create_suv()
    sedan = factory.create_sedan()

    print(suv.drive())
    print(sedan.drive())


if __name__ == "__main__":
    print("Driving white cars")
    create_car(WhiteCarFactory())
    print("\nDriving dark cars")
    create_car(DarkCarFactory())
