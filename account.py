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
        :param amount: amount to be deposited into account
        :return: True if successfully added amount to account balance, False if unsuccessful
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        return False

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
