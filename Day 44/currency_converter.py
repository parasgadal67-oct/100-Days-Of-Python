import requests
def get_amount(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Enter the Valid Input!")
            continue
        if value <= 0:
            print("Amount must be greater than 0!")
        else:
            return value
from_currency = input("Enter your currency: ").upper().strip() 
to_currency =input("Enter the currency to get changed: ").upper().strip()
amount = get_amount("Enter the amount: ")
url = f"https://open.er-api.com/v6/latest/{from_currency}"
try:
    response = requests.get(url, timeout=10)
except requests.exceptions.ConnectionError:
    print("No Internet Connection. Check Your internet!")
except requests.exceptions.Timeout:
    print("Requests TimedOut. Try again later")
else:
    if response.status_code != 200:
        print("Something went wrong !", response.status_code)
    else:
        data = response.json()
        if data.get("result") != "success":
            print("Currency not supported!", from_currency)
        else:
            rates = data["rates"].get(to_currency)

            if rates is None:
                print("Currency not found!", to_currency)
            else:
                result = amount * rates
                print(f"{amount} {from_currency} = {result:.2f} {to_currency}")

            
            