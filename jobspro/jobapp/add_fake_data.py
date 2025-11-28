import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jobspro.settings")

import django
django.setup()

from faker import Faker
from jobapp.models import Punejob, Bangjob, Bhiharjob

fake = Faker()

def create_jobs(model, count=10):
    for _ in range(count):
        model.objects.create(
            date=fake.date(),
            company=fake.company(),
            title=fake.job(),
            address=fake.address()[:50],
            salary=fake.random_int(min=20000, max=150000),
            email=fake.email(),
            phone=fake.random_int(min=6000000000, max=9999999999),
        )
    print(f"{count} records inserted into {model.__name__}")


if __name__ == "__main__":
    num = int(input("Enter number of fake records: "))

    create_jobs(Punejob, num)
    create_jobs(Bangjob, num)
    create_jobs(Bhiharjob, num)

    print("All fake job records inserted successfully!")
