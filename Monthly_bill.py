# Constants for package prices and additional usage costs
PACKAGE_A_MONTHLY_FEE = 9.95
PACKAGE_B_MONTHLY_FEE = 14.95
PACKAGE_C_MONTHLY_FEE = 19.95
PACKAGE_A_HOURLY_LIMIT = 5
PACKAGE_B_HOURLY_LIMIT = 10
PACKAGE_A_ADDITIONAL_COST_PER_MINUTE = 0.08
PACKAGE_B_ADDITIONAL_COST_PER_MINUTE = 0.06

def calculate_package_a_bill(hours_used):
    total_cost = PACKAGE_A_MONTHLY_FEE
    if hours_used > PACKAGE_A_HOURLY_LIMIT:
        extra_hours = hours_used - PACKAGE_A_HOURLY_LIMIT
        total_cost += extra_hours * 60 * PACKAGE_A_ADDITIONAL_COST_PER_MINUTE
    return total_cost

def calculate_package_b_bill(hours_used):
    total_cost = PACKAGE_B_MONTHLY_FEE
    if hours_used > PACKAGE_B_HOURLY_LIMIT:
        extra_hours = hours_used - PACKAGE_B_HOURLY_LIMIT
        total_cost += extra_hours * 60 * PACKAGE_B_ADDITIONAL_COST_PER_MINUTE
    return total_cost

def calculate_savings(package_choice, total_amount_due):
    if package_choice == 'A':
        package_b_saving = calculate_package_a_bill(PACKAGE_B_HOURLY_LIMIT) - total_amount_due
        package_c_saving = PACKAGE_C_MONTHLY_FEE - total_amount_due
        if package_b_saving > 0:
            print(f"You could save ${package_b_saving:.2f} by switching to Package B.")
        if package_c_saving > 0:
            print(f"You could save ${package_c_saving:.2f} by switching to Package C.")
    elif package_choice == 'B':
        package_c_saving = PACKAGE_C_MONTHLY_FEE - total_amount_due
        if package_c_saving > 0:
            print(f"You could save ${package_c_saving:.2f} by switching to Package C.")

def print_bill_to_file(bill_details):
    file_path = "MyBill.txt"
    with open(file_path, 'w') as file:
        file.write(bill_details)
    print("Bill printed to", file_path)

def main():
    try_again = 'Y'
    while try_again == 'Y':
        print("Welcome to the International Internet Phone Company Billing System!")
        
        # Get user input
        customer_name = input("Enter customer name: ")
        package_choice = input("Enter package (A, B, or C): ").upper()
        hours_used = float(input("Enter hours used: "))
        
        total_amount_due = 0
        
        # Calculate total amount due based on package and usage
        if package_choice == 'A':
            total_amount_due = calculate_package_a_bill(hours_used)
        elif package_choice == 'B':
            total_amount_due = calculate_package_b_bill(hours_used)
        elif package_choice == 'C':
            total_amount_due = PACKAGE_C_MONTHLY_FEE
        else:
            print("Invalid package choice. Please choose A, B, or C.")
            continue
        
        # Display bill
        print("\nCustomer Name:", customer_name)
        print("Package:", package_choice)
        print("Hours Used:", hours_used)
        print("Total Amount Due: $", "{:.2f}".format(total_amount_due))
        
        # Calculate and display savings
        calculate_savings(package_choice, total_amount_due)
        
        # Ask if the user wants to try again
        try_again = input("\nTry again? (Y/N): ").upper()
        
    # Print bill to file
    print_bill_to_file("Bill details here")

if __name__ == "__main__":
    main()
