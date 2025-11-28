from faker import Faker
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysqlpro.settings')

import django
django.setup()

from mysqlpro.models import Employee   # <-- change 'appname' to your actual app name

fake = Faker()

def inserting(n):
    for i in range(n):
        fname = fake.name()
        fage = fake.random_int(min=10, max=40)
        fsal = fake.random_int(min=1000, max=50000)
        femail = fake.email()
        fdate = fake.date()

        Employee.objects.get_or_create(
            name=fname,
            email=femail,
            age=fage,
            salary=fsal,
            doj=fdate
        )

    print(f"{n} records inserted successfully")


# --- MAIN EXECUTION ---
num = int(input("Enter the number of records you want to insert: "))
inserting(num)
