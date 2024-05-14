#Source: https://stackoverflow.com/questions/76616348/attributeerror-xyz-object-has-no-attribute-yzx
from src.invoice_generator.models.client import Client


class Seller(Client):
    """
    Seller model

    Attributes:
        :param name: str - seller name
        :param street: str - seller street
        :param city: str - seller city
        :param postal_code: str - seller postal code
        :param phone: str - seller phone number
        :param email: str - seller email address
        :param nip: str - seller NIP number
        :param regon: str - seller REGON number
        :param bank_account: str - seller bank account number

    Methods:
        :__init__: initialize Seller object
        :__str__: return string representation of Seller object
    """

    def __init__(self, name: str, street: str, city: str, postal_code: str, phone: str, email: str, nip: str, regon: str, bank_account: str) -> None:
        super().__init__(name, street, city, postal_code, phone, email, nip)
        self.regon = regon
        self.bank_account = bank_account

        if not self.validate():
            if not self.validate_regon():
                raise ValueError('Invalid REGON number')
            if not self.validate_bank_account():
                raise ValueError('Invalid bank account number')

    def __str__(self) -> str:
        return f'super().__str__(), {self.regon}, {self.bank_account}'

    def validate(self) -> bool:
        """
        Validate Seller object
        :return: bool - True if Seller object is valid, False otherwise
        """
        return super().validate() and self.validate_regon() and self.validate_bank_account()

    def validate_regon(self) -> bool:
        """
        Validate REGON number
        :return: bool - True if REGON number is valid, False otherwise
        """
        regon = self.regon.replace('-', '')
        if len(regon) != 9:
            return False
        weights = [8, 9, 2, 3, 4, 5, 6, 7]
        check_sum = sum([int(regon[i]) * weights[i] for i in range(len(weights))])
        return check_sum % 11 == int(regon[-1])

    def validate_bank_account(self) -> bool:
        """
        Validate bank account number
        :return: bool - True if bank account number is valid, False otherwise
        """
        bank_account = self.bank_account.replace('-', '')
        if len(bank_account) != 26:
            return False
        weights = [1, 10, 3, 30, 9, 90, 27, 76, 81, 34, 49, 5, 50, 15, 53, 45, 62, 38, 89, 17, 73, 51, 25, 56, 75, 71]
        check_sum = sum([int(bank_account[i]) * weights[i] for i in range(len(weights))])
        return check_sum % 97 == 1