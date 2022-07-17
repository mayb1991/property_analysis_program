# First we need to determine the income the potenal property could make 
# Second we need to find out much the expances are going to be for the property
# Third we need to find the cash flow (monthly about of money that the owner will pocket after expances)
# Last we will find the ROI (Return On Investment)


class ROI():
    
    def __init__(self, income, expances, cash_flow, return_on_investment):
        self.reveune = income
        self.exp = expances
        self.flow = cash_flow
        self.return_investment = return_on_investment

    def income(self):
        monthly_rent = int(input("Enter monthly rent: "))
        other_monthly_income = int(input("Please enter the amount of any other income the property may make: "))
        self.reveune = monthly_rent + other_monthly_income
        print(f"Your monthly income for this property is ${self.reveune}")
        return ROI

    def expances (self):
        vacacy = self.reveune * .10
        repairs = self.reveune * .07
        property_manager = self.reveune * .10
        capex = self.reveune * .05
        monthly_mortage = int(input("What is the expected motrage on the property: "))
        insurance = int(input("If you choose to carry insurance on the property what is your premiuem going to be: "))
        if insurance > 0:
            monthly_insurance = insurance / 12
            print(monthly_insurance)
        landscape = int(input("If you are planning on paying for lawn care and or snow removeal please enter an amount here: "))
        utilites = int(input("If paying for utilites please enter amount here: "))
        yearly_tax_amount = int(input("Enter amount of annual property taxes: "))
        if yearly_tax_amount > 0:
            monthly_tax_amount = yearly_tax_amount / 12
        hoa = int(input("If the property has an HOA please enter the monthly amount: "))
        self.exp = vacacy+repairs+property_manager+capex+monthly_mortage+monthly_insurance+landscape+utilites+monthly_tax_amount+hoa
        print(f"Your total monthly expances for this property are ${self.exp}")
    
    def cash_flow(self):
        self.flow = self.reveune - self.exp
        print(f"Your monthly cash flow for this property is ${self.flow}")

    def return_on_investment(self):
        purchase_price = int(input("Enter the price you are buying the property for: "))
        down_payment = purchase_price * .20
        closing_cost = purchase_price * .03
        rehab = int(input("If there are any repaires need please enter the amount: "))
        misc = int(input("Please enter anyother fees that you may incounter: "))
        self.return_investment = down_payment + closing_cost + rehab + misc
        cash_on_cash = (self.flow / self.return_investment) * 1000
        print(f"Your ROI for this property is {cash_on_cash}%")

h1 = ROI(0,0,0,0)
h1.income()
h1.expances()
h1.cash_flow()
h1.return_on_investment()