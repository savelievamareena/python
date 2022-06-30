# Kласс House: id, Номер квартиры, Площадь, Этаж, Количество комнат, Улица, Тип здания, Срок эксплуатации.
# Функции-члены реализуют запись и считывание полей (проверка корректности), расчета возраста задания (необходимость в кап. ремонте).
# Создать список объектов. Вывести:
# a)список квартир, имеющих заданное число комнат;
# б) список квартир, имеющих заданное число комнат и расположенных на этаже, который находится в заданном промежутке;

class House:
    __house_list = []
    __house_id = 0
    __apt = 0
    __square = 0
    __floor = 0
    __rooms_num = 0
    __street = ""
    __building_type = ""
    __lifetime = 0
    __count = 0

    def __init__(self, house_id, apt, square, floor, rooms_num, street, building_type, lifetime):
        self.set_house_id(house_id)
        self.set_apt(apt)
        self.set_square(square)
        self.set_floor(floor)
        self.set_rooms_num(rooms_num)
        self.set_street(street)
        self.set_building_type(building_type)
        self.set_lifetime(lifetime)
        House.add_house_to_list(self)

    def __str__(self):
        return "Id: {}, Apt: {}, Square: {}, Floor: {}, Rooms' Quantity: {}, Street: {}, Building Type: {}".format(
            self.get_house_id(), self.get_apt(), self.get_square(), self.get_floor(), self.get_rooms_num(),
            self.get_street(), self.get_building_type()
        )

    def __sub__(self, wc_square):
        return self.__square - wc_square

    def __eq__(self, other):
        return self.__square == other

    def __lt__(self, other):
        return self.__square < other

    def __gt__(self, other):
        return self.__square > other

    @classmethod
    def create_default_house(cls, house_id, apt, square, floor, rooms_num):
        default_house = cls(house_id, apt, square, floor, rooms_num, 'Slobodskaya', 'panel house', 70)
        return default_house

    @staticmethod
    def function_a(house_list, number_of_rooms):
        result = []
        for flat in house_list:
            if number_of_rooms == flat.get_rooms_num():
                result.append(flat)
        return result

    @staticmethod
    def function_b(house_list, number_of_rooms, min_floor, max_floor):
        result = []
        for flat in house_list:
            if number_of_rooms == flat.get_rooms_num() and min_floor <= flat.get_floor() <= max_floor:
                result.append(flat)
        return result

    def get_house_id(self):
        return self.__house_id

    def set_house_id(self, house_id):
        self.__house_id = house_id

    def get_apt(self):
        return self.__apt

    def set_apt(self, apt):
        self.__apt = apt

    def get_square(self):
        return self.__square

    def set_square(self, square):
        self.__square = square

    def get_floor(self):
        return self.__floor

    def set_floor(self, floor):
        self.__floor = floor

    def get_rooms_num(self):
        return self.__rooms_num

    def set_rooms_num(self, rooms_num):
        self.__rooms_num = rooms_num

    def get_street(self):
        return self.__street

    def set_street(self, street):
        self.__street = street

    def get_building_type(self):
        return self.__building_type

    def set_building_type(self, building_type):
        self.__building_type = building_type

    def get_lifetime(self):
        return self.__lifetime

    def set_lifetime(self, lifetime):
        self.__lifetime = lifetime

    @staticmethod
    def get_house_list():
        return House.__house_list

    @staticmethod
    def add_house_to_list(house):
        House.__house_list.append(house)

    @staticmethod
    def add_house():
        House.create_default_house(int(input('Enter House Id: ')),
                                   int(input('Enter Apartment Number: ')),
                                   int(input('Enter Square: ')),
                                   int(input('Enter Floor: ')),
                                   int(input('Enter Rooms Number: ')))
        return House.get_house_list()

    @staticmethod
    def see_house_list():
        for house in House.get_house_list():
            print(house)


text = input("How many houses do you want to enter: ")
for i in range(int(text)):
    House.add_house()
    House.see_house_list()

number_of_rooms = int(input("Enter number of rooms: "))
result1 = House.function_a(House.get_house_list(), number_of_rooms)
print("List of apartments with a given number of rooms: ")
for house in result1:
    print(house)

min_floor = int(input("Enter min floor: "))
max_floor = int(input("Enter max floor: "))
result2 = House.function_b(House.get_house_list(), number_of_rooms, min_floor, max_floor)
print("List of apartments with a given number of rooms that exists on the given range of floors: ")
for house in result2:
    print(house)
