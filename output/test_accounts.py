import unittest

class TestAccount(unittest.TestCase):
    def test_account_init(self):
        account = Account("test_account", 1000.0)
        self.assertEqual(account.account_id, "test_account")
        self.assertEqual(account.balance, 1000.0)

    def test_deposit_funds(self):
        account = Account("test_account", 1000.0)
        account.deposit_funds(500.0)
        self.assertEqual(account.balance, 1500.0)

    def test_withdraw_funds(self):
        account = Account("test_account", 1000.0)
        account.withdraw_funds(200.0)
        self.assertEqual(account.balance, 800.0)

    def test_buy_shares(self):
        account = Account("test_account", 1000.0)
        account.buy_shares("AAPL", 10)
        self.assertEqual(account.get_holding_quantity("AAPL"), 10)

    def test_sell_shares(self):
        account = Account("test_account", 1000.0)
        account.buy_shares("AAPL", 10)
        account.sell_shares("AAPL", 5)
        self.assertEqual(account.get_holding_quantity("AAPL"), 5)


if __name__ == "__main__":
    unittest.main()