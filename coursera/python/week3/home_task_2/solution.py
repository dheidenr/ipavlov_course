import os.path
import csv

# Ссылка в помощь к этому заданию
# https://www.coursera.org/learn/diving-in-python/programming/bd6aI/klassy-i-nasliedovaniie/discussions/threads/4lBKgugvRpiQSoLoL6aYEQ
class CarBase:
    car_type = ''

    def __init__(self,
                 # car_type=None,
                 brand=None,
                 photo_file_name=None, carrying=None):
        # self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        try:
            self.carrying = float(carrying)
        except TypeError:
            self.carrying = 0.0

    def get_photo_file_ext(self):
        ext = os.path.splitext(self.photo_file_name)[1]
        if ext == '' or ext not in ['.jpg', '.jpeg', '.png', '.gif']:
            raise ValueError
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self,
                 # car_type,
                 brand, photo_file_name, carrying,
                 passenger_seats_count=None):
        super().__init__(
            # car_type,
            brand, photo_file_name, carrying)
        try:
            self.passenger_seats_count = int(passenger_seats_count)
        except TypeError:
            self.passenger_seats_count = 0
        self.__class__.car_type = 'car'


class Truck(CarBase):
    body_length = None
    body_width = None
    body_height = None

    def __init__(self,
                 # car_type,
                 brand, photo_file_name, carrying,
                 body_whl):
        super().__init__(
            # car_type,
            brand, photo_file_name, carrying)
        try:
            whl = list(map(lambda x: float(x), body_whl.split('x')))
            if len(whl) > 3:
                raise IndexError
            self.body_width = whl[1]
            self.body_height = whl[2]
            self.body_length = whl[0]
        except (IndexError, ValueError):
            self.body_width, self.body_height, self.body_length = 0.0, 0.0, 0.0
        self.__class__.car_type = 'truck'

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    def __init__(self,
                 # car_type,
                 brand, photo_file_name, carrying, extra=None):
        super().__init__(
            # car_type,
            brand, photo_file_name, carrying)
        self.extra = extra
        self.__class__.car_type = 'spec_machine'


class ConstructorCar:
    def __init__(self, car_type, brand, passenger_seats_count, photo_file_name,
                 body_whl, carrying, extra):
        pass


def get_car_list(csv_filename):
    try:
        file = open(csv_filename, "r")
    except IOError:
        return []
    reader = csv.DictReader(file, delimiter=';')
    # print(reader.__dict__)
    # if reader.line_num == 0:
    #     return []
    car_list = []
    for line in reader:
        if line["car_type"] == '' or line["brand"] == '' \
                or line["photo_file_name"] == '' or line["carrying"] == '' \
                or line["car_type"] not in ['car', 'truck', 'spec_machine']:
            continue
        try:
            if line["carrying"] != '':
                float_test = float(line['carrying'])
        except TypeError:
            continue
        ext = os.path.splitext(line["photo_file_name"])[1]
        if ext == '' or ext not in ['.jpg', '.jpeg', '.png', '.gif']:
            continue
        if line["car_type"] == 'car':
            try:
                int(line["passenger_seats_count"])
                if line["passenger_seats_count"] == '':
                    raise TypeError
            except (TypeError, ValueError):
                continue
            car = Car(
                # line["car_type"],
                line["brand"],
                line["photo_file_name"],
                line['carrying'],
                line['passenger_seats_count'])
            car.car_type = line["car_type"]
            car_list.append(car)
        elif line["car_type"] == 'truck':
            # if line['body_whl'] == '':
            #     continue
            car = Truck(
                # line["car_type"],
                line["brand"],
                line["photo_file_name"],
                line['carrying'],
                line['body_whl'])
            car.car_type = line["car_type"]
            car_list.append(car)
        elif line["car_type"] == 'spec_machine':
            if line['extra'] == '':
                continue
            car = SpecMachine(
                # line["car_type"],
                line["brand"],
                line["photo_file_name"],
                line['carrying'],
                line['extra'])
            car.car_type = line["car_type"]
            car_list.append(car)
    if reader.fieldnames is None:
        return []
    return car_list
