class Mobile() :
    def __init__(self, company_name, name, storage, serial_num, dual_sim, support4k):
        self.company_name = company_name
        self.storage = storage
        self.serial_num = serial_num
        self.name = name
        self.dual_sim = dual_sim
        self.support4k = support4k

    def info(self):
        print(f"Phone: {self.company_name} {self.name} \nStorage: \
{self.storage}GB \nSerial number: {self.serial_num} \nDual Sim: {self.dual_sim} \nSupport 4k: \
{self.support4k}")


phone1 = Mobile("Samsung","Galaxy S23", 256, 12345678910, "Yes", "Yes")

phone2 = Mobile("Apple","Iphone 14", 512, 109876543210, "Yes", "Yes")

phone1.info()


