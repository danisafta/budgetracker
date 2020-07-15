from stocks_manager import manager
import unittest


class TestCluster(unittest.TestCase):
    total = manager.get_total_invested()
    tickers = manager.get_tickers_from_db()
    tt = manager.get_investment_tuples(tickers=tickers)
    weights = manager.get_weights_dict(tt, total)
    data = manager.get_financial_data(tickers)
    ret = manager.get_simple_returns(data)
    ar = manager.get_annual_returns(ret)

    def test_data(self):
        self.assertIsNotNone(self.data)

    def test_total(self):
        self.assertIsInstance(self.total, float)

    def test_tickers(self):
        self.assertIsInstance(self.tickers, list)

    def test_ticker_tuples(self):
        self.assertIsInstance(self.tt, list)
        self.assertIsInstance(self.tt[0], tuple)

    def test_weights(self):
        self.assertIsInstance(self.weights, dict)
        all = 0
        for _, value in self.weights.items():
            all += value
        self.assertAlmostEqual(all, 1.0, delta=0.0001)

    def test_return(self):
        retun = manager.get_portfolio_return(weights=self.weights, annual_returns=self.ar)
        self.assertLess(retun, 1.0)


if __name__ == "__main__":
    unittest.main()
