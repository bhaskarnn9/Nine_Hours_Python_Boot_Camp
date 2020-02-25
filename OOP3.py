# What we know:
# A regular method in a class takes self(an instance of class) as a first argument.

# What we should learn:
# A class method takes class as a first argument

class Manufacturer:

    num_of_oems = 0
    
    def __init__(self, oem, model, prod_rate, price):
        self.oem_name = oem
        self.model_name = model
        self.production_rate = prod_rate
        self.price_amount = price
        self.email_address = model + '@company.com'

        Manufacturer.num_of_oems += 1

    def full_model_name(self):
        return '{} {}'.format(self.oem_name, self.model_name)

    @classmethod
    def set_hike_rate(cls, amount):
        cls.hike_rate = amount

    # 5 percent increate in production rate
    def apply_production_hike(self):
        self.production_rate = int(self.production_rate * self.hike_rate)
    
    @classmethod
    def from_string(cls, inp_string):
        oem_name, model_name, production_rate, price_amount = inp_string.split('_')
        return cls(oem_name, model_name, production_rate, price_amount)
    
    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    


Hyundai = Manufacturer('Hyundai', 'Accent', 5000, 1000000)
Suzuki = Manufacturer('Suzuki', 'Swift', 10000, 750000)
Honda = Manufacturer.from_string('Honda_Civic_2000_2000000')

Hyundai.set_hike_rate(1.1)
Hyundai.apply_production_hike()
print(Hyundai.hike_rate)
print(Manufacturer.hike_rate)
print(Honda.__dict__)

print(Manufacturer.num_of_oems)

import datetime

day = datetime.date(2019, 12, 14)

print(Manufacturer.is_weekday(day))