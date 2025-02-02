import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scripts.fundamental_analysis import FinancialAnalyzer

ticker = "NVDA"
analyzer = FinancialAnalyzer(ticker)
analyzer.get_balance_sheet(plot=True)
analyzer.get_income_statement(plot=True)
analyzer.get_cash_flow(plot=True)
analyzer.get_financial_ratios()

plt.show()