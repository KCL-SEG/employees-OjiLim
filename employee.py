"""Employee pay calculator."""
def str(employee):
    return employee.__str__()

class Employee:
    def __init__(self, name, contract, commission =  None):
        self.name = name
        self.contract = contract
        self.commission = commission
    def get_pay(self):
        if self.commission != None:
            contractPay = self.contract.calculatePay()
            commissionPay = self.commission.calculateCommission()
            return commissionPay + contractPay
        else:
            return self.contract.calculatePay()

    def __str__(self):
        if self.commission != None:
            return f"{self.name} works on a {self.contract.type} and receives a {self.commission.type}. Their total pay is {self.get_pay()}"
        else:
            return f"{self.name} works on a {self.contract.type}. Their total pay is {self.get_pay()}"

class SalaryContract:
    def __init__(self,salary):
        self.salary = salary
        self.type = f"monthly salary of {salary}"
    def calculatePay(self):
        return self.salary

class HourlyContract:
    def __init__(self,hourly,hours):
        self.hourly = hourly
        self.hours = hours
        self.type = f"contract of {hours} hours at {hourly}/hour"
    def calculatePay(self):
        return self.hourly * self.hours

class ContractCommission:
    def __init__(self,commissionRate, contracts):
        self.commissionRate = commissionRate
        self.contracts = contracts
        self.type = f"commission for {contracts} contract(s) at {commissionRate}/contract"
    def calculateCommission(self):
        return self.commissionRate*self.contracts

class BonusCommision:
    def __init__(self,bonusRate):
        self.bonusRate = bonusRate
        self.type = f"bonus commission of {bonusRate}"
    def calculateCommission(self):
        return self.bonusRate



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billieContract = SalaryContract(4000)
billie = Employee('Billie',contract = billieContract)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlieContract = HourlyContract(25,100)
charlie = Employee('Charlie', contract = charlieContract)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
reneeContract = SalaryContract(3000)
reneeCommission = ContractCommission(200,4)
renee = Employee('Renee', contract = reneeContract, commission = reneeCommission)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
janContract = HourlyContract(25,150)
janCommission = ContractCommission(220,3)
jan = Employee('Jan', contract = janContract, commission = janCommission)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbieContract = SalaryContract(2000)
robbieCommission = BonusCommision(1500)
robbie = Employee('Robbie', contract = robbieContract, commission = robbieCommission)


# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
arialContract = HourlyContract(30,120)
arialCommission = BonusCommision(600)
ariel = Employee('Ariel', contract = arialContract, commission = arialCommission)
