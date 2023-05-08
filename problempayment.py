# YOUR NAME
# ASAS SAINS KOMPUTER (ASK)
# Problem Set 3 – Problem 1
# Simple Pay Program
""" 
Inputs, Processes and Outputs (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Input(s):
Processes:
Output(s):
"""

def main():
    pay_rate = 25
    print("Simple Pay Program\n")
    hours = int(input("How many hours did you work: "))

    tax = .125
    pay = (pay_rate) * hours
    taxes = pay * tax
    net_pay = pay - taxes

    print("\nPay Stub")
    print(f"\t\tHours: {hours}")
    print(f"\t\tRate: ${pay_rate:.2f}")
    print(f"\t\tPay: ${pay:.2f}")
    print(f"\t\tTax: ${taxes:.2f}")
    print(f"\t\tNet Pay: ${net_pay:.2f}")

if __name__ == "__main__":
    main()
