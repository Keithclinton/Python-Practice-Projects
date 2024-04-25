using System;
using System.IO;

namespace PhoneCompanyBillingSystem
{
    class Program
    {
        // Constants for package prices and additional usage costs
        const double PackageA_MonthlyFee = 9.95;
        const double PackageB_MonthlyFee = 14.95;
        const double PackageC_MonthlyFee = 19.95;
        const double PackageA_HourlyLimit = 5;
        const double PackageB_HourlyLimit = 10;
        const double PackageA_AdditionalCostPerMinute = 0.08;
        const double PackageB_AdditionalCostPerMinute = 0.06;

        static void Main(string[] args)
        {
            char tryAgain = 'Y';
            while (tryAgain == 'Y')
            {
                Console.WriteLine("Welcome to the International Internet Phone Company Billing System!");

                // Print package details
                Console.WriteLine("\nPackage A: For $9.95 per month 5 hours of call time are provided. Additional usage costs $0.08 per minute.");
                Console.WriteLine("Package B: For $14.95 per month 10 hours of call time are provided. Additional usage costs $0.06 per minute.");
                Console.WriteLine("Package C: For $19.95 per month unlimited call time is provided.");

                // Get user input
                Console.Write("\nEnter customer name: ");
                string customerName = Console.ReadLine();

                // Check if customer name is a number
                if (int.TryParse(customerName, out _))
                {
                    Console.WriteLine("Error: Customer name cannot be an integer. Only letters are allowed.");
                    continue;
                }

                Console.Write("Enter package (A, B, or C): ");
                char packageChoice = Char.ToUpper(Console.ReadKey().KeyChar);
                Console.WriteLine();

                // Validate package choice
                if (packageChoice != 'A' && packageChoice != 'B' && packageChoice != 'C')
                {
                    Console.WriteLine("Error: Please select A, B, or C.");
                    continue;
                }

                Console.Write("Enter hours used: ");
                double hoursUsed = Convert.ToDouble(Console.ReadLine());

                double totalAmountDue = 0;

                // Calculate total amount due based on package and usage
                switch (packageChoice)
                {
                    case 'A':
                        totalAmountDue = CalculatePackageABill(hoursUsed);
                        break;
                    case 'B':
                        totalAmountDue = CalculatePackageBBill(hoursUsed);
                        break;
                    case 'C':
                        totalAmountDue = PackageC_MonthlyFee;
                        break;
                }

                // Display bill
                Console.WriteLine("\nCustomer Name: " + customerName);
                Console.WriteLine("Package: " + packageChoice);
                Console.WriteLine("Hours Used: " + hoursUsed);
                Console.WriteLine("Total Amount Due: $" + totalAmountDue.ToString("0.00"));

                // Calculate and display savings
                CalculateSavings(packageChoice, totalAmountDue);

                // Ask if the user wants to try again
                Console.Write("\nTry again? (Y/N): ");
                tryAgain = Char.ToUpper(Console.ReadKey().KeyChar);
                Console.WriteLine();
            }

            // Print bill to file
            PrintBillToFile(customerName, packageChoice, hoursUsed, totalAmountDue);
        }

        static double CalculatePackageABill(double hoursUsed)
        {
            double totalCost = PackageA_MonthlyFee;
            if (hoursUsed > PackageA_HourlyLimit)
            {
                double extraHours = hoursUsed - PackageA_HourlyLimit;
                totalCost += extraHours * 60 * PackageA_AdditionalCostPerMinute;
            }
            return totalCost;
        }

        static double CalculatePackageBBill(double hoursUsed)
        {
            double totalCost = PackageB_MonthlyFee;
            if (hoursUsed > PackageB_HourlyLimit)
            {
                double extraHours = hoursUsed - PackageB_HourlyLimit;
                totalCost += extraHours * 60 * PackageB_AdditionalCostPerMinute;
            }
            return totalCost;
        }

        static void CalculateSavings(char packageChoice, double totalAmountDue)
        {
            switch (packageChoice)
            {
                case 'A':
                    double packageBSaving = CalculatePackageABill(PackageB_HourlyLimit) - totalAmountDue;
                    double packageCSaving = PackageC_MonthlyFee - totalAmountDue;
                    if (packageBSaving > 0)
                        Console.WriteLine("You could save $" + packageBSaving.ToString("0.00") + " by switching to Package B.");
                    if (packageCSaving > 0)
                        Console.WriteLine("You could save $" + packageCSaving.ToString("0.00") + " by switching to Package C.");
                    break;
                case 'B':
                    double packageCSavingB = PackageC_MonthlyFee - totalAmountDue;
                    if (packageCSavingB > 0)
                        Console.WriteLine("You could save $" + packageCSavingB.ToString("0.00") + " by switching to Package C.");
                    break;
            }
        }

        static void PrintBillToFile(string customerName, char packageChoice, double hoursUsed, double totalAmountDue)
        {
            // Retrieve bill details
            string billDetails = $"Customer Name: {customerName}\nPackage: {packageChoice}\nHours Used: {hoursUsed}\nTotal Amount Due: ${totalAmountDue.ToString("0.00")}";

            // Write to file
            string filePath = "MyBill.txt";
            File.WriteAllText(filePath, billDetails);

            Console.WriteLine("\nBill printed to " + filePath);
        }
    }
}