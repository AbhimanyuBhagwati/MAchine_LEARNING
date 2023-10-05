import pandas as pd
from pandas_datareader import data as pdr
from matplotlib import pyplot as plt
import yfinance as yf
yf.pdr_override()
import numpy as np

np.random.seed(5808)

class data_preprocessing:
    def __init__(self, **kwargs):
        self.stock = kwargs['stock']
        self.start_date = kwargs['start_date']
        self.end_date = kwargs['end_date']
        self.df = None

    def read_data(self) -> None:
        """
        Read the data from the csv file.
        :return: None
        """
        self.df = pdr.get_data_yahoo(self.stock, start=self.start_date, end=self.end_date)


    def normalized(self):
        normalized_df = (self.df - self.df.min()) / (self.df.max() - self.df.min())
        normalized_df = normalized_df.round(2)
        return normalized_df

    def standardized(self):
        data_mean = self.df.mean()
        data_std = self.df.std()
        standardized_df = (self.df - data_mean) / data_std
        standardized_df = standardized_df.round(2)
        return standardized_df

    def iqr(self):
        Q1 = self.df.quantile(0.25)
        Q3 = self.df.quantile(0.75)
        IQR = Q3 - Q1
        iqr_data = (self.df - Q1) / IQR
        return iqr_data

    def show_original(self):
        self.df.plot()
        plt.title("Original Data")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.grid()
        plt.show()

    def show_normalized(self):
        self.normalized().plot()
        plt.title("Normalized Data")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.grid()
        plt.show()

    def show_standardized(self):
        self.standardized().plot()
        plt.title("Standardized Data")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.grid()
        plt.show()

    def show_iqr(self):
        self.iqr().plot()
        plt.title("Interquartile Range")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.grid()
        plt.show()
