

    #The function calculates financial assistance based on income and number of children.    
    #:param income: The income of the person applying for financial assistance
    #:param num_children: The number of children in the household
    #:return: the amount of financial assistance based on the income and number of children provided as
    #input. The amount returned depends on the income and number of children according to the conditions specified in the if-elif-else statements. If none of the conditions are met, the function returns 0.
def calculate_financial_assistance(income, num_children):
    
    if 40000 <= income <= 50000 and num_children >= 3:
        return 1200 * num_children
    elif 30000 <= income < 40000 and num_children >= 2:
        return 1700 * num_children
    elif income < 30000:
        return 2100 * num_children
    else:
        return 0

def main():
    print("Financial Assistance Calculator for Needy Families")

    while True:
        try:
            income = float(input("Enter the annual household income (-1 to exit): "))
            if income == -1:
                break

            num_children = int(input("Enter the number of children: "))

            assistance_amount = calculate_financial_assistance(income, num_children)
            print(f"Financial assistance amount: ${assistance_amount:.2f}\n")
        except ValueError:
            print("Invalid input. Please enter valid values for income and number of children.")

if __name__ == "__main__":
    main()
