import random
from faker import Faker


class Utils():

    @staticmethod
    def password():
        password = ''
        for x in range(9):
            password = password + random.choice(list('1234567890qwertyuiopASDFGHJKLZXCVBMNMNM'))
        print(password)
        return password

    @staticmethod
    def email():
        fake = Faker()
        email = fake.email()
        print(email)
        return email
