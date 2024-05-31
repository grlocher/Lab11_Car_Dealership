class Vehicle:

    def __init__(self, make: str = '', miles: int = 0, price: float = 0.0):
        self.make = make
        self.miles = miles
        self.price = price
        self.engine_on = False

    def start_engine(self):
        print('Starting engine...')
        self.engine_on = True

    def make_noise(self):
        print('Beep beep!')

    def get_info(self) -> str:
        return f'Make: {self.make}, Miles: {self.miles}, Price: {self.price}'


class Truck(Vehicle):

    def __init__(self, make: str = '', miles: int = 0, price: float = 0.0):
        super().__init__(make, miles, price)
        self.cargo_property = False

    def load_cargo(self):
        print('Loading the truck bed...')
        self.cargo_property = True


class Motorcycle(Vehicle):

    def __init__(self, make: str = '', miles: int = 0, price: float = 0.0, top_speed: int = 0):
        super().__init__(make, miles, price)
        self.top_speed = top_speed

    def make_noise(self):
        print('Vroom vroom!')

    def get_info(self) -> str:
        return f'{super().get_info()}, Top Speed: {self.top_speed}'