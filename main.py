#from application.db.people import get_employees
#from application.salary import calculate_salary

from application import salary
from application.db import people
import datetime
import ycnbc

def top_news():
    data = ycnbc.News()
    trending_ = data.trending()
    print('Главная новость на сегодня')
    print(trending_.loc[0])
    print()


if __name__ == '__main__':
    print(datetime.date.today())
    top_news()
    salary.calculate_salary()
    people.get_employees()

