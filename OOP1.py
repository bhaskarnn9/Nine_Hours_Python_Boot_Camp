# Classes and Instances

# class Manu:
#     pass


# Hyundai = Manu()
# Suzuki = Manu()

# Hyundai.model = 'Creta'
# Hyundai.price = 1000000
# Hyundai.capacity = 5

# Suzuki.model = 'Swift'
# Suzuki.price = '900000'
# Suzuki.capacity = 4

# print(Hyundai.model)
# print(Suzuki.model)

class Manufacturer:
    
    def __init__(self, oem, model, capacity, price):
        self.oem_name = oem
        self.model_name = model
        self.capacity_num = capacity
        self.price_amount = price
        self.email_address = model + '@company.com'

    def full_model_name(self):
        return '{} {}'.format(self.oem_name, self.model_name)

Hyundai = Manufacturer('Hyundai', 'Creta', 5, 1500000)
Suzuki = Manufacturer('Suzuki', 'Swift', 4, 750000)


print(Hyundai.email_address)
print(Suzuki.model_name)
print(Hyundai.full_model_name())