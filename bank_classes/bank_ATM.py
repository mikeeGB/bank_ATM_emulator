from bank_classes.bank_account import MyBankAccount


class ATM:
    """Class of ATM"""

    def __init__(self, firstname, lastname):
        self._cash_dict = {
            500: 3,
            200: 5,
            100: 5,
            50: 5,
            20: 5,
            10: 10,
            5: 10,
        }
        self.__link_account(firstname, lastname)

    def __link_account(self, firstname: str, lastname: str) -> None:
        """Links bank account to the ATM, creates field user_account"""
        self.user_account = MyBankAccount(firstname, lastname)

    def __set_max_cash_available(self) -> None:
        """Checks max amount of cash available in ATM"""
        self._max_cash = sum(a * b for a, b in self._cash_dict.items())

    def check_cash_state(self) -> None:
        """Prints dictionary cash amount available in ATM"""
        print(f"Cash in ATM: {self._cash_dict}")

    def cash_out(self, cash: int) -> dict:
        """Gives cash to a client"""
        if self.__cash_out_available_checker(cash) and self.user_account.cash_amount >= cash:
            cash_sum = self.__create_cash_out_dict(cash)
            self.user_account.cash_amount -= cash  # cash amount on user credit card decreases after cashing out
            return cash_sum
        else:
            cash_sum = {'your cash': 0}
            return cash_sum

    def __create_cash_out_dict(self, cash: int) -> dict:
        """Creates cash_out dictionary"""
        cash_out_d = {}
        for nominal in self._cash_dict.keys():
            num_of_banknotes = cash // nominal
            if num_of_banknotes > 0:
                cash_out_d[nominal] = num_of_banknotes
            if num_of_banknotes > self._cash_dict[nominal]:
                cash_out_d[nominal] = self._cash_dict[nominal]
                cash = cash - nominal * self._cash_dict[nominal]
            else:
                remain_cash = cash % nominal
                cash = remain_cash
        self.__update_cash_state_in_atm(cash_out_d)
        return cash_out_d

    def __cash_out_available_checker(self, cash: int) -> bool:
        """Checks possibility to cash out requested amount"""
        self.__set_max_cash_available()
        try:
            assert cash <= self._max_cash
        except AssertionError:
            print(f"There is no such amount of cash ({cash}) in ATM")
            return False
        else:
            print(f"\n{cash} amount approved")
            return True

    def __update_cash_state_in_atm(self, cash_out_d: dict) -> None:
        """Updates cash amount in ATM"""
        for nominal, num_of_banknotes in cash_out_d.items():
            self._cash_dict[nominal] = self._cash_dict[nominal] - num_of_banknotes

    def interactive_atm(self):
        menu_prompt = """
        Client:
           1. Deposit cash
           2. Withdraw cash
           3. Show pin
           4. Generate pin
           5. Set new pin
        ATM:
           6. Check cash state
           7. Cash out
           8. Exit
           """
        actions = {"Deposit cash": self.user_account.deposit_cash_sum,
                   "Withdraw cash": self.user_account.withdraw_cash_sum,
                   "Show pin": self.user_account.show_pin,
                   "Generate pin": self.user_account.generate_pin,
                   "Set new pin": self.user_account.set_new_pin,
                   "Check cash state": self.check_cash_state,
                   "Cash out": self.cash_out,
                   }

        while True:
            inp_act = input(menu_prompt + "Action: ")
            if inp_act == "1":
                actions["Deposit cash"]()
            elif inp_act == "2":
                actions["Withdraw cash"]()
            elif inp_act == "3":
                actions["Show pin"]()
            elif inp_act == "4":
                actions["Generate pin"]()
            elif inp_act == "5":
                actions["Set new pin"]()
            elif inp_act == "6":
                actions["Check cash state"]()
            elif inp_act == "7":
                cash_s = int(input("Enter sum: "))
                cash_d = actions["Cash out"](cash_s)
                print(cash_d)
            elif inp_act == "8":
                print("Program executed...")
                break
