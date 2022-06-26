# Kласс House: id, Номер квартиры, Площадь, Этаж, Количество комнат, Улица, Тип здания, Срок эксплуатации.
# Функции-члены реализуют запись и считывание полей (проверка корректности), расчета возраста задания (необходимость в кап. ремонте).
# Создать список объектов. Вывести:
# a)список квартир, имеющих заданное число комнат;
# б) список квартир, имеющих заданное число комнат и расположенных на этаже, который находится в заданном промежутке;

class House:
    house_list = []
    _house_id = 0
    _apt = 0
    _square = 0
    _floor = 0
    _rooms_num = 0
    _street = ""
    _building_type = ""
    _lifetime = 0

    def __init__(self, house_id, apt, square, floor, rooms_num, street, building_type, lifetime):
        self.set_house_id(house_id)
        self.set_apt = apt
        self.set_square = square
        self.set_floor = floor
        self.set_rooms_num = rooms_num
        self.set_street = street
        self.set_building_type = building_type
        self.set_lifetime = lifetime

    @classmethod
    def create_default_house(cls, house_id, apt, square, floor, rooms_num):
        default_house = cls(house_id, apt, square, floor, rooms_num, 'Slobodskaya', 'panel house', 70)
        return default_house

    def function_a(self, house_list, number_of_rooms):
        result = []
        for house in house_list:
            if number_of_rooms == self.get_rooms_num():
                result.append(house)
        return result

    def function_b(self, number_of_rooms, min_floor, max_floor):
        result = []
        for house in self.house_list:
            if number_of_rooms == self.get_rooms_num() and min_floor <= self.get_floor() <= max_floor:
                result.append(house)
        return result

    def get_house_id(self):
        return self._house_id

    def set_house_id(self, house_id):
        self._house_id = house_id

    def get_apt(self):
        return self._apt

    def set_apt(self, apt):
        self._apt = apt

    def get_square(self):
        return self._square

    def set_square(self, square):
        self._square = square

    def get_floor(self):
        return self._floor

    def set_floor(self, floor):
        self._floor = floor

    def get_rooms_num(self):
        return self._rooms_num

    def set_rooms_num(self, rooms_num):
        self._rooms_num = rooms_num

    def get_street(self):
        return self._street

    def set_street(self, street):
        self._street = street

    def get_building_type(self):
        return self._building_type

    def set_building_type(self, building_type):
        self._building_type = building_type

    def get_lifetime(self):
        return self._lifetime

    def set_lifetime(self, lifetime):
        self._lifetime = lifetime


house1 = House.create_default_house(int(input('Enter House Id: ')),
                                    int(input('Enter Apartment Number: ')),
                                    int(input('Enter Square: ')),
                                    int(input('Enter Floor: ')),
                                    int(input('Enter Room: ')))

print(house1)
