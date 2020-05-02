from coursera.python.week3.home_task_2.solution import *


whl = '8x3x2.5'
if __name__ == '__main__':
    print(whl.split('x'))
    whl = list(map(float, whl.split('x')))
    print(list(whl))
    body_width = whl[0]
    print(body_width)
    try:
        print(float('2.9'))
    except ValueError:
        print('error')
    else:
        print('NORMAl')
    l = []
    # print(l[50])
    cars = get_car_list('coursera_week3_cars.csv')
    print(len(cars))
    print(cars)
    for car in cars:
        if isinstance(car, Truck):
            print(f"truck, w{car.body_width}, h{car.body_height}, l{car.body_length}")
        print(type(car))
        print(type(car.car_type))
    print('end')
    # print(cars[0].get_photo_file_ext())

    # print(cars[0].passenger_seats_count)
    # print(cars[1].get_body_volume())
    # print(cars[0].car_type)
    # print(cars[4].extra)
    # print(cars[2].body_width)
