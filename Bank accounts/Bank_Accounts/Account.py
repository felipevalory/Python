import abc


class Account(abc.ABC):
    def __init__(self, branch: int, account: int, balance: float = 0) -> None:
        self.branch = branch
        self.account = account
        self.balance = balance

    @abc.abstractmethod
    def withdrawal(self, value: float) -> float:
        ...

    def deposit(self, value: float) -> float:
        self.balance += value
        self.details(f'(DEPOSIT US$ {value:.2f})')
        return self.balance

    def details(self, msg: str = '') -> None:
        print(f'Your balance is US$ {self.balance:.2f} {msg}')
        print('--')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.branch!r}, {self.account!r}, {self.balance!r})'
        return f'{class_name}{attrs}'


class SavingsAccount(Account):
    def withdrawal(self, value: float):
        value_after_withdrawal = self.balance - value

        if value_after_withdrawal >= 0:
            self.balance -= value
            self.details(f'(WITHDRAWAL US$ {value:.2f})')
            return self.balance

        print('Unable to withdraw desired amount')
        self.details(f'(WITHDRAWAL DENIED US$ {value:.2f})')
        return self.balance


class BankAccount(Account):
    def __init__(
        self, branch: int, account: int,
        balance: float = 0, overdraft_limit: float = 0
    ):
        super().__init__(branch, account, balance)
        self.overdraft_limit = overdraft_limit

    def withdrawal(self, value: float) -> float:
        value_after_withdrawal = self.balance - value
        max_limit = -self.overdraft_limit

        if value_after_withdrawal >= max_limit:
            self.balance -= value
            self.details(f'(WITHDRAW US$ {value:.2f})')
            return self.balance

        print('Unable to withdraw desired amount')
        print(f'\nYour overdraft limit is US$ {self.overdraft_limit:.2f}\n')
        self.details(f'(WITHDRAWAL DENIED US$ {value:.2f})')
        return self.balance

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.branch!r}, {self.account!r}, {self.balance!r}, '\
            f' {self.overdraft_limit!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    account01 = SavingsAccount(111, 222)
    account01.withdrawal(1)
    account01.deposit(1)
    account01.withdrawal(1)
    account01.withdrawal(1)
    print('##')
    account01 = BankAccount(111, 222, 0, 100)
    account01.withdrawal(1)
    account01.deposit(1)
    account01.withdrawal(1)
    account01.withdrawal(1)
    account01.withdrawal(98)
    account01.withdrawal(1)
