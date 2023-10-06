import random

class ATMCard:
    def __init__(self, card_num, card_pin, checking_balance):
        self.card_num = card_num
        self.card_pin = card_pin
        self.checking_balance = checking_balance

def initialize_card_db():
    cards_db = {}
    cards_data = [
        ("123456789", "1111"),
        ("135792468", "2097"),
        ("019283746", "6194"),
        ("675849302", "0071"),
        ("347821904", "9871")
    ]
    for card_num, card_pin in cards_data:
        # Generate a random balance between 100 and 1000
        checking_balance = random.randint(100, 1000)
        cards_db[card_num] = ATMCard(card_num, card_pin, checking_balance)
    return cards_db

def insert_card(cards_db, card_num):
    return cards_db.get(card_num, None)

def process_card(card):
    print(f"Current balance: ${card.checking_balance}")
    action = input("Select an action: (1) Withdraw, (2) Deposit, (3) Check Balance: ")

    if action == "1":
        withdraw_amount = int(input("Enter the amount to withdraw: $"))
        if card.checking_balance >= withdraw_amount:
            card.checking_balance -= withdraw_amount
            dispense_funds(withdraw_amount)
            print(f"Withdrawal successful. New balance: ${card.checking_balance}\n")
            continue_transaction(card)
        else:
            print("Insufficient funds.\n")
    elif action == "2":
        deposit_amount = int(input("Enter the amount to deposit: $"))
        card.checking_balance += deposit_amount
        print(f"Deposit successful. New balance: ${card.checking_balance}\n")
    elif action == "3":
        print(f"Your balance: ${card.checking_balance}\n")
    else:
        print("Invalid action.\n")

def dispense_funds(amount):
    print(f"Dispensing ${amount}")

def continue_transaction(card):
    while True:
        print(f"Your remaining balance: ${card.checking_balance}")
        action = input("Select an action: (1) Withdraw, (2) Deposit, (3) Check Balance, (4) Exit: ")

        if action == "1":
            withdraw_amount = int(input("Enter the amount to withdraw: $"))
            if card.checking_balance >= withdraw_amount:
                card.checking_balance -= withdraw_amount
                dispense_funds(withdraw_amount)
                print(f"Withdrawal successful. New balance: ${card.checking_balance}\n")
            else:
                print("Insufficient funds.\n")
        elif action == "2":
            deposit_amount = int(input("Enter the amount to deposit: $"))
            card.checking_balance += deposit_amount
            print(f"Deposit successful. New balance: ${card.checking_balance}\n")
        elif action == "3":
            print(f"Your balance: ${card.checking_balance}\n")
        elif action == "4":
            print_receipt(card)
            print("\nThank you for using RayPay. Goodbye!")
            break
        else:
            print("Invalid action.\n")

def print_receipt(card):
    print("Receipt:")
    print(f"Card Number: {card.card_num}")
    print(f"Balance: ${card.checking_balance}")

def main():
    print("Welcome to RayPay, Raymond James's digital ATM, what would you like to do?")
    print("\nOptions:")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance\n")

    cards_db = initialize_card_db()

    # Simulate transactions
    card_num = input("Insert your ATM card: ")
    card = insert_card(cards_db, card_num)

    if card:
        pin_attempts = 0
        while pin_attempts < 4:
            pin = input("Enter your PIN: ")
            if card.card_pin == pin:
                process_card(card)
                break
            else:
                pin_attempts += 1
                print(f"\nWrong PIN. Attempts left: {4 - pin_attempts}")
        else:
            print("\nCard eaten due to incorrect PIN attempts.")

if __name__ == "__main__":
    main()
