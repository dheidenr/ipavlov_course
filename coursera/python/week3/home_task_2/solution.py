import os.path
import csv


class CarBase:
    def __init__(self, car_type=None, brand=None,
                 photo_file_name=None, carrying=None):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        try:
            self.carrying = float(carrying)
        except TypeError:
            self.carrying = None

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)


class Car(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying,
                 passenger_seats_count=None):
        super().__init__(car_type, brand, photo_file_name, carrying)
        try:
            self.passenger_seats_count = int(passenger_seats_count)
        except TypeError:
            self.passenger_seats_count = None


class Truck(CarBase):
    body_length = None
    body_width = None
    body_height = None

    def __init__(self, car_type, brand, photo_file_name, carrying,
                 body_whl: str):
        super().__init__(car_type, brand, photo_file_name, carrying)
        try:
            whl = list(map(lambda x: float(x), body_whl.split('x')))
            self.body_width = whl[0]
            self.body_height = whl[1]
            self.body_length = whl[2]
        except (IndexError, ValueError):
            self.body_width, self.body_height, self.body_length = 0.0, 0.0, 0.0

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra=None):
        super().__init__(brand, car_type, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    file = open(csv_filename, "r")
    print(file)
    reader = csv.DictReader(file, delimiter=';')
    car_list = []
    for line in reader:
        print(line)
        if line["car_type"] == 'car':
            car_list.append(Car(line["car_type"],
                                line["brand"],
                                line["photo_file_name"],
                                line['carrying'],
                                line['passenger_seats_count']))
        elif line["car_type"] == 'truck':
            car_list.append(Truck(line["car_type"],
                                  line["brand"],
                                  line["photo_file_name"],
                                  line['carrying'],
                                  line['body_whl']))
        elif line["car_type"] == 'spec_machine':
            car_list.append(SpecMachine(line["car_type"],
                                        line["brand"],
                                        line["photo_file_name"],
                                        line['carrying'],
                                        line['extra']))
    return car_list
