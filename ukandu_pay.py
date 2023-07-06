
    #The function calculates the total pay for an employee based on their hourly rate and hours worked, including overtime pay.
    
    #:param hourly_rate: The rate of pay per hour for the employee. It is a numeric value (float or integer) representing the amount of money the employee earns per hour of work
    #:param hours_worked: The number of hours worked by the employee in the past month
    #:return: The function `calculate_pay` returns the total pay for an employee based on their hourly rate and hours worked, taking into account any overtime pay. The `main` function prints out the employee's name, hourly rate, hours worked, and the total pay for the month.
        

def calculate_pay(hourly_rate, hours_worked):
    
    regular_hours = min(hours_worked, 160)
    overtime_hours = max(hours_worked - 160, 0)

    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5

    total_pay = regular_pay + overtime_pay
    return total_pay

def main():
    employee_name = input("Enter the employee name: ")
    hourly_rate = 15
    hours_worked = float(input("Enter the number of hours worked in the past month: "))

    total_pay = calculate_pay(hourly_rate, hours_worked)

    print(f"Employee name: {employee_name}")
    print(f"Hourly rate: ${hourly_rate}")
    print(f"Hours worked: {hours_worked}")
    print(f"The total pay for the month will be ${total_pay:.2f} for {hours_worked} hours of work")

if __name__ == "__main__":
    main()
