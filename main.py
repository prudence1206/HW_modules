import datetime
from turtle import *
import application.salary
import application.db.people


def get_date():
    print(datetime.datetime.now())


def make_sun():
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    done()


application.salary.calculate_salary()
application.db.people.get_employees()
get_date()
make_sun()
