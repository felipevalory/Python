import Account
import AccountHolder


class Bank:
    def __init__(
        self,
        branches: list[int] | None = None,
        clients: list[AccountHolder.Client] | None = None,
        accounts: list[Account.Account] | None = None
    ):
        self.branches = branches or []
        self.clients = clients or []
        self.accounts = accounts or []

    def _check_branch(self, account):
        if account.branch in self.branches:
            return True
        return False

    def _check_client(self, client):
        if client in self.clients:
            return True
        return False

    def _check_account(self, account):
        if account in self.accounts:
            return True
        return False

    def _check_if_is_clients_account(self, client, account):
        if account is client.account:
            return True
        return False

    def auth(self, client: AccountHolder.Client, account: Account.Account):
        return self._check_branch(account) and \
            self._check_client(client) and \
            self._check_account(account) and \
            self._check_if_is_clients_account(client, account)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.branches!r}, {self.clients!r}, {self.accounts!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    client01 = AccountHolder.Client('Felipe', 30)
    bankaccount01 = Account.BankAccount(111, 222, 0, 0)
    client01.account = bankaccount01
    client02 = AccountHolder.Client('Pedro', 27)
    savingsaccount01 = Account.SavingsAccount(112, 223, 100)
    client02.account = savingsaccount01
    bank = Bank()
    bank.clients.extend([client01, client02])
    bank.accounts.extend([bankaccount01, savingsaccount01])
    bank.branches.extend([111, 222])

    if bank.auth(client01, bankaccount01):
        bankaccount01.withdrawal(10)
        print(client01.account)
