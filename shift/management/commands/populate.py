import os.path
from django.core.management.base import BaseCommand
import random
import string
from shift.models import Worker


def random_letter():
    random_letter = chr(random.randint(65, 90))
    return random_letter

class Command(BaseCommand):
    help = 'populate data base with random employee'

    def handle(self, *args, **options):
        login_length=random.randint(3,20)
        password_length=random.randint(4,10)
        login = ""
        password = ""
        for i in range(10):
            for j in range(login_length):
                login += random_letter()
            if Worker.objects.filter(login=login).count() != 0:
                print('login taken')
                login = ''
                password = ''
            else:
                for k in range(password_length):
                    password += random_letter()
                new_emploeey = Worker(login=login, password=password)
                new_emploeey.save()
                print('emploeey added')
                f=open('employees.txt', mode='a')
                f.writelines(f'{login} {password}\n')
                f.close()
                login=''
                password=''