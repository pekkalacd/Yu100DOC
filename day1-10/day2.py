"""
Requirements

1. if the bill was $150.000, split between 5 people, with 12% tip.
2. Each person should pay (150.00 / 5) * 1.12
3. Round the result to 2 decimal places ~ 33.60
"""

class PercentError(Exception):
    def __init__(self, msg: str=''):
        super().__init__(msg)

def banner() -> None:
    print("Welcome to the Tip Calculator.")

def total_bill() -> float:
    total = input("What was the total bill? ")
    try:
        return float(total)
    except ValueError:
        print("Err. That looks like an invalid numerical amount. Try again.")
        return total_bill()

def percentage() -> float:
    pct = input("What percentage tip would you like to give? 10, 12, or 15? ")
    accepted = {10,12,15}
    try:
        pct = float(pct)
        if pct not in accepted:
            raise PercentError
        return int(pct)/100
    except ValueError:
        print("Err. That looks like an invalid percentage numerically. Try again.")
        return percentage()
    except PercentError:
        print("Err. You can only tip 10, 12, or 15%")
        return percentage()

def split_by_n() -> int:
    amt = input("How many people to split the bill? ")
    while not amt.isdigit():
        print("Must be an integer amount of people to split bill")
        amt = input("How many people to split the bill? ")
    return int(amt)

def bill_per(total: float, split: int, tip_pct: float) -> float:
    per_person_with_tip = (total/split) * (1.0+tip_pct)
    return per_person_with_tip

def again() -> bool:
    print("\nWant to calculate another tip? (Y|N)")
    while (ans := input().lower()) not in {'y','n'}:
        print("Err. I don't know what you mean")
        print("\nWant to calculate another tip? (Y|N)")
    if ans == 'y':
        return True
    return False

def loop():
    playing = True
    while playing:
        banner()
        bill = total_bill()
        tip = percentage()
        party = split_by_n()
        per_person = bill_per(bill, party, tip)
        print(f"Each person should pay: ${per_person:,.2f}")
        playing = again()
    print("\nThanks for playing!")
    print("Later....")


if __name__ == "__main__":
    loop()



