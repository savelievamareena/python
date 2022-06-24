# Kласс House: id, Номер квартиры, Площадь, Этаж, Количество комнат, Улица, Тип здания, Срок эксплуатации.
# Функции-члены реализуют запись и считывание полей (проверка корректности), расчета возраста задания (необходимость в кап. ремонте).
# Создать список объектов. Вывести:
# a)список квартир, имеющих заданное число комнат;
# б) список квартир, имеющих заданное число комнат и расположенных на этаже, который находится в заданном промежутке;

class House:
    house_list = []
    _house_id_ = 0
    _apt_ = 0
    _square_ = 0
    _floor_ = 0
    _rooms_num_ = 0
    _street_ = ""
    _building_type_ = ""
    _lifetime_ = 0

    def __init__(self, house_id, apt, square, floor, rooms_num, street, building_type, lifetime):
        self.set_house_id(house_id)
        self.set_apt = apt
        self.set_square = square
        self.set_floor = floor
        self.set_rooms_num = rooms_num
        self.set_street = street
        self.set_building_type = building_type
        self.set_lifetime = lifetime
        self.house_list.append(self)

    @classmethod
    def create_default_house(cls, house_id, apt, square, floor, rooms_num):
        default_house = cls(house_id, apt, square, floor, rooms_num, 'Slobodskaya', 'panel house', 70)
        return default_house

    @staticmethod
    def function_a(house_list, number_of_rooms):
        result = []
        for house in house_list:
            if number_of_rooms == house.__rooms_num:
                result.append(house)
        return result

    def function_b(self, number_of_rooms, min_floor, max_floor):
        result = []
        for house in self.house_list:
            if number_of_rooms == house.__rooms_num and min_floor <= house.__floor <= max_floor:
                result.append(house)
        return result

    def get_house_id(self):
        return self._house_id_

    def set_house_id(self, house_id):
        self._house_id_ = house_id

    def get_apt(self):
        return self._apt_

    def set_apt(self, apt):
        self._apt_ = apt

    def get_square(self):
        return self._square_

    def set_square(self, square):
        self._square_ = square

    def get_floor(self):
        return self._floor_

    def set_floor(self, floor):
        self._floor_ = floor

    def get_rooms_num(self):
        return self._rooms_num_

    def set_rooms_num(self, rooms_num):
        self._rooms_num_ = rooms_num

    def get_street(self):
        return self._street_

    def set_street(self, street):
        self._street_ = street

    def get_building_type(self):
        return self._building_type_

    def set_building_type(self, building_type):
        self._building_type_ = building_type

    def get_lifetime(self):
        return self._lifetime_

    def set_lifetime(self, lifetime):
        self._lifetime_ = lifetime


my_house_id = int(input('Enter House Id: '))
my_apt = int(input('Enter Apartment Number: '))
my_square = int(input('Enter Square: '))
my_floor = int(input('Enter Floor: '))
my_rooms_num = int(input('Enter Room: '))

house1 = House.create_default_house(my_house_id, my_apt, my_square, my_floor, my_rooms_num)
print(house1)
