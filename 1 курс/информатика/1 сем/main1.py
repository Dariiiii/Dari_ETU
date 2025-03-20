class HouseScheme:
    def __init__(self, living_rooms, living_space, combined_bathroom):
        if isinstance(living_rooms, (int, float)) and isinstance(living_space, (int, float)) \
                and living_space >= 0 and isinstance(combined_bathroom, bool):
            self.living_rooms = living_rooms
            self.living_space = living_space
            self.combined_bathroom = combined_bathroom
        else:
            raise ValueError('Invalid value')


class CountryHouse(HouseScheme):
    def __init__(self, living_rooms, living_space, combined_bathroom, floors_num, land_area):
        super().__init__(living_rooms, living_space, combined_bathroom)
        if isinstance(floors_num, (int, float)) and isinstance(land_area, (int, float)):
            self.floors_num = floors_num
            self.land_area = land_area
        else:
            raise ValueError('Invalid value')

    def __str__(self):
        tx = [self.living_rooms, self.living_space, self.combined_bathroom, self.floors_num, self.land_area]
        return 'Country House: Количество жилых комнат {}, Жилая площадь {}, Совмещенный санузел {}, Количество этажей {}, Площадь участка {}.'.format(
            *tx)

    def __eq__(self, other):
        if not isinstance(other, CountryHouse):
            raise ValueError('Invalid value')

        return self.living_space == other.living_space and self.land_area == other.land_area and \
               abs(self.floors_num - other.floors_num) <= 1


class Apartment(HouseScheme):
    def __init__(self, living_rooms, living_space, combined_bathroom, floor, windows_direction):
        super().__init__(living_rooms, living_space, combined_bathroom)
        if isinstance(floor, (int, float)) and floor >= 1 and floor <= 15 and ['N', 'S', 'W', 'E'].__contains__(
                windows_direction):
            self.floor = floor
            self.windows_direction = windows_direction
        else:
            raise ValueError('Invalid value')

    def __str__(self):
        tx = [self.living_rooms, self.living_space, self.combined_bathroom, self.floor, self.windows_direction]
        return 'Apartment: Количество жилых комнат {}, Жилая площадь {}, Совмещенный санузел {}, Этаж {}, Окна выходят на {}.'.format(
            *tx)


class CountryHouseList(list):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def append(self, p_object):
        if isinstance(p_object, CountryHouse):
            super().append(p_object)
        else:
            raise TypeError('Invalid type {}'.format(type(p_object)))

    def total_square(self):
        all_living_space = 0
        for i in self:
            all_living_space += i.living_space
        return all_living_space


class ApartmentList(list):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def extend(self, iterable):
        super().extend(list(filter(lambda obj: isinstance(obj, Apartment), iterable)))

    def floor_view(self, floors, directions):
        f = lambda x: floors[0] <= x.floor and x.floor <= floors[-1] and x.windows_direction in directions
        view = list(filter(f, self))
        for i in view:
            print(f'{i.windows_direction}: {i.floor}')
