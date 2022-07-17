# First we need to determine the income the potenal property could make 
# Second we need to find out much the expances are going to be for the property
# Third we need to find the cash flow (monthly about of money that the owner will pocket after expances)
# Last we will find the ROI (Return On Investment)


class ROI():
    
    def __init__(self, income, expances, cash_flow, return_on_investment,  purchase_price):
        self.gross = income
        self.exp = expances
        self.flow = cash_flow
        self.return_investment = return_on_investment
        self.price =  purchase_price

    def income(self):
        monthly_rent = int(input("Enter monthly rent: "))
        other_monthly_income = int(input("Please enter the amount of any other income the property may make: "))
        self.gross = monthly_rent + other_monthly_income
        print(f"Your monthly income for this property is ${self.gross}")
        return ROI

    def expances (self):
        vacacy = self.gross * .10
        repairs = self.gross * .07
        property_manager = self.gross * .10
        capex = self.gross * .05
        monthly_mortage = int(input("What is the expected motrage on the property: "))
        insurance = int(input("If you choose to carry insurance on the property what is your premiuem going to be: "))
        if insurance > 0:
            monthly_insurance = insurance / 12
        landscape = int(input("If you are planning on paying for lawn care and or snow removeal please enter an amount here: "))
        utilites = int(input("If paying for utilites please enter amount here: "))
        yearly_tax_amount = int(input("Enter amount of annual property taxes: "))
        if yearly_tax_amount > 0:
            monthly_tax_amount = yearly_tax_amount / 12
        hoa = int(input("If the property has an HOA please enter the monthly amount: "))
        self.exp = vacacy+repairs+property_manager+capex+monthly_mortage+monthly_insurance+landscape+utilites+monthly_tax_amount+hoa
        print(f"Your total monthly expances for this property are ${self.exp}")
    
    def cash_flow(self):
        self.flow = self.gross - self.exp
        print(f"Your monthly cash flow for this property is ${self.flow}")

    def return_on_investment(self):
        self.price = int(input("Enter the price you are buying the property for: "))
        down_payment = self.price * .20
        closing_cost = self.price * .03
        rehab = int(input("If there are any repaires need please enter the amount: "))
        misc = int(input("Please enter anyother fees that you may incounter: "))
        self.return_investment = down_payment + closing_cost + rehab + misc
        cash_on_cash = (self.flow / self.return_investment) * 1000
        print(f"Your ROI for this property is {cash_on_cash}%")

    

h1 = ROI(0,0,0,0,0)
h1.income()
h1.expances()
h1.cash_flow()
h1.return_on_investment()


# Here I was trying to create a seprate class for the 1% rule. 
# To see if the potential propery would pass or not but I can not get the math to work out. 
# No matter what I do it comes out with everything passing the rule. 

# class Good_Investment_or_not(ROI):
#     def __init__(self, income, expances, cash_flow, return_on_investment, purchase_price):
#         super().__init__(income, expances, cash_flow, return_on_investment, purchase_price)
    

#     def one_rule(self):
#         one_percent_rule_meaning = """
#         The 1% rule of real estate investing measures the price of the investment 
#         property against the gross income it will generate. For a potential investment 
#         to pass the 1% rule, its monthly rent must be equal to or no less than 1% of the purchase price.
#         To calculate the 1% rule, simply multiply the property purchase price by 1%. 
#         The result is the minimum monthly rent that the home should generate.
#         """

#         one_percent_rule = self.price * .01
#         print(one_percent_rule)
#         if one_percent_rule >= self.gross:
#             print("This property passes the 1% rule!")
#         else:
#             print("This property does not pass the 1% rule")
    
# h1 = Good_Investment_or_not(0,0,0,0,0)
# h1.one_rule()