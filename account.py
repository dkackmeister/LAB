class Account:
    """
    A class representing a user's bank account
    """
    def __init__(self, name: str) -> None:
        """
        Constructor to create initial state of an account object
        :param name: user's name
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: int) -> bool:
        """
        Method to add a deposit to account balance
        :param amount: amount to add to account balance
        :return: True if successfully added amount to account balance, False if unsuccessful
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        return False

    def withdraw(self, amount: int) -> bool:
        """
        Method to subtract amount from account balance
        :param amount: amount to subtract to account balance
        :return: True if successfully subtracted amount from account balance, False is unsuccessful
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        self.__account_balance -= amount
        return True

    def get_balance(self) -> int:
        """
        Method to access user account balance
        :return: Account balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to access user account name
        :return: return Account name
        """
        return self.__account_name
