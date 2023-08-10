import Account


class Client:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.name!r}, {self.age!r})'
        return f'{class_name}{attrs}'


class AccountHolder(Client):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.account: Account.Account | None = None


if __name__ == '__main__':
    client01 = AccountHolder('Felipe', 30)
    client01.account = Account.BankAccount(111, 222, 0, 0)
    print(client01)
    print(client01.account)
    client02 = AccountHolder('Pedro', 27)
    client02.account = Account.SavingsAccount(112, 223, 100)
    print(client02)
    print(client02.account)
