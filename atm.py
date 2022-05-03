class Atm:
    def __init__(self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin

    def checkBalance(self):
        print("Your balance is 50000")

    def withdrawel(self, amount):
        new_amount = 50000 - amount
        print("You have withdrawn amount " + str(amount) +
              " Your remaining balance is " + str(new_amount))


def main():
    card_number = input("Insert your card number: ")
    pin_number = input("Enter your pin number: ")
    new_user = Atm(card_number, pin_number)
    print('Choose your activity: ')
    print('1. Balance inquiry 2. withdrawel')
    activity = int(input('Enter the activity number: '))
    if (activity == 1):
        new_user.checkBalance()
    elif (activity == 2):
        amount = int(input('Enter the amount: '))
        new_user.withdrawel(amount)
    else:
        print('Enter a valid number: ')


main()
