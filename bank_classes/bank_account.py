from random import randint


class MyBankAccount:
    """Class of user Bank Account"""
    def __init__(self, firstname: str, lastname: str):
        self.__pin = '2510'
        self.firstname = firstname
        self.lastname = lastname
        self.cash_amount = 0
        self.__keyword_unblock = 'unblock_me'
        self.__greeting_user()

    def __cash_withdraw_input_helper(self) -> int:
        """Private method. Checks possibility to withdraw cash, withdraws it"""
        cash_sum = input("Enter cash amount to withdraw: ")
        if cash_sum.isdigit() and (0 <= int(cash_sum) <= self.cash_amount):
            self.cash_amount -= int(cash_sum)
            return int(cash_sum)
        else:
            print("Repeat input")
            return self.__cash_withdraw_input_helper()

    def __cash_deposit_input_helper(self) -> int:
        """Private method. Checks possibility to deposit cash, deposits it"""
        cash_sum = input("Enter cash amount to deposit: ")
        if cash_sum.isdigit() and int(cash_sum) >= 0:
            self.cash_amount += int(cash_sum)
            return int(cash_sum)
        else:
            print("Repeat input")
            return self.__cash_deposit_input_helper()

    def deposit_cash_sum(self) -> None:
        """Deposit cash to the account"""
        if self._pin_entering():
            cash_after_deposit = self.__cash_deposit_input_helper()
            print(f"\n{cash_after_deposit} is deposited to the account\n"
                  f"Current account sum: {self.cash_amount}")

    def withdraw_cash_sum(self) -> None:
        """Withdraw money from the account"""
        if self._pin_entering():
            cash_after_withdraw = self.__cash_withdraw_input_helper()
            print(f"\n{cash_after_withdraw} is withdrawn from the account\n"
                  f"Current account sum: {self.cash_amount}")

    def __greeting_user(self) -> None:
        """Greets user, shows default pin to user"""
        print(f"Hi, {self.firstname} {self.lastname}. Your default pin is: {self.__pin}")

    def generate_pin(self) -> None:
        """Generates random pin"""
        self.__pin = ''.join([str(randint(0, 9)) for _ in range(4)])

    def __set_new_pin_helper(self) -> str:
        """Setting new pin, helper. Checks correctness of pin input"""
        new_pin_inp = input("New pin: ")
        if new_pin_inp.isdigit() and len(new_pin_inp) == 4:
            self.__pin = new_pin_inp
            return new_pin_inp
        print("Incorrect pin input")
        return self.__set_new_pin_helper()

    def set_new_pin(self) -> None:
        """Sets new pin"""
        if self._pin_entering():
            self.__pin = self.__set_new_pin_helper()
            print("New pin is set")

    def show_pin(self) -> None:
        """Shows current pin"""
        print(self.__pin)

    def _pin_entering(self, attempts=2) -> bool:
        """Pin entering process"""
        pin_input = input("\nEnter pin-code: ")
        if self.__pin == pin_input:
            return True
        elif attempts > 0:
            print(f"Incorrect pin, attempts left: {attempts}")
            return self._pin_entering(attempts-1)
        else:
            print(f"{self.firstname} {self.lastname}, Your account is blocked!")
            self.__block_account()

    def __block_account(self) -> None:
        """Blocking account and unblocking by keyword"""
        unblock_inp = input("Enter keyword to unblock account: ")
        if unblock_inp == self.__keyword_unblock:
            print("\nAccount unblocked!")
            self.generate_pin()
            print(f"Your new pin: {self.__pin}")
        else:
            return self.__block_account()
