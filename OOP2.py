# class variables

# class variables are tha variables whose values are same thought out the instances of the class

class Manufacturer:

    num_of_oems = 0
    hike_rate = 1.05
    
    def __init__(self, oem, model, prod_rate, price):
        self.oem_name = oem
        self.model_name = model
        self.production_rate = prod_rate
        self.price_amount = price
        self.email_address = model + '@company.com'

        Manufacturer.num_of_oems += 1

    def full_model_name(self):
        return '{} {}'.format(self.oem_name, self.model_name)


    # 5 percent increate in production rate
    def hike_production(self):
        self.production_rate = int(self.production_rate * self.hike_rate)

Hyundai = Manufacturer('Hyundai', 'Accent', 5000, 1000000)
Suzuki = Manufacturer('Suzuki', 'Swift', 10000, 750000)
Honda = Manufacturer('Honda', 'Civic', 2000, 2000000)


print(Hyundai.production_rate)
Hyundai.hike_rate = 1.10
Hyundai.hike_production()
print(Hyundai.__dict__)
print(Hyundai.production_rate)

print(Suzuki.production_rate)
Suzuki.hike_production()
print(Suzuki.__dict__)
print(Suzuki.production_rate)

print(Manufacturer.num_of_oems)