# Description: Calculates the interest on a bank account

def calculate_monthly_balance(initial_balance, annual_interest_rate, months):
    monthly_interest_rate = annual_interest_rate / 12
    balance = initial_balance

    for i in range(months):
        balance += balance * (monthly_interest_rate / 100)
        print(f"Balance after month {i+1}: ${balance:.2f}")

    return balance

def main():
    initial_balance = 2000
    annual_interest_rate = 4

    print(f"The Initial Balance is: ${initial_balance:.2f}")
    print(f"The Annual Interest rate is: {annual_interest_rate}%")
    balance_after_four_months = calculate_monthly_balance(initial_balance, annual_interest_rate, 4)
    
    
    

if __name__ == "__main__":
    main()
