# main.py
# Simple Tech project in Python

def greet():
    print("Welcome to Tech!")
    print("This is a simple Python app for a tech project.")

def show_services():
    services = [
        "Web Development",
        "AI Solutions",
        "Cloud Services",
        "Cybersecurity",
        "Automation"
    ]

    print("\nOur Services:")
    for i, service in enumerate(services, start=1):
        print(f"{i}. {service}")

def calculate_growth(start, end, years):
    growth = ((end - start) / start) * 100
    return round(growth, 2)

def main():
    greet()
    show_services()

    print("\nGrowth Calculator")
    start_value = float(input("Enter starting value: "))
    end_value = float(input("Enter ending value: "))
    years = float(input("Enter number of years: "))

    growth_percent = calculate_growth(start_value, end_value, years)
    print(f"\nGrowth in {years} years: {growth_percent}%")

    print("\nThank you for using Tech!")

if __name__ == "__main__":
    main()
