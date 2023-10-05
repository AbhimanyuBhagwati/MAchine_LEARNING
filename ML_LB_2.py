import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

stock_data = r"https://raw.githubusercontent.com/rjafari979/Information-Visualization-Data-Analytics-Dataset-/main/stock%20prices.csv"
CLEANED_DATA = None


class QUESTION:
    def __init__(self):
        self.file_data = stock_data
        self.df = None

    def read_file(self):
        self.df = pd.read_csv(self.file_data)

class QUESTION1(QUESTION):
    def __init__(self):
        super().__init__()
        self.read_file()
        self._df_with_nan = None
        self.df_index_with_nan = None

    def ck_nan_value(self):
        if self.df.isnull().sum().sum() > 0:
            print("There is NaN value in the dataset. \n")
            print(f"Missing features :\n {self.df.isnull().sum()}", end='\n\n')
            print(f"Number of missing entries : {self.df.isnull().sum().sum()} \n")
            self._df_with_nan = self.df[self.df.isnull().any(axis=1)].to_string()
            self.df_index_with_nan = self.df[self.df.isnull().any(axis=1)].index
            self.nan_to_mean()
        else:
            print("There is no NaN value in the dataset")

    def nan_to_mean(self) -> pd.DataFrame:
        """
        Replace NaN values with mean value of the column
        :return: None
        """
        df_all_val = self.df.describe()
        df_mn = self.df.fillna(df_all_val.loc['mean'])
        print(f"The missing values in table :\n {self._df_with_nan}", end='\n\n')
        print(f"Mean values of all columns :\n {df_all_val.loc['mean']}")
        print("*-" * 50, end='\n\n')
        print("Test Case : ")
        print(f"Number of missing entries after replacing with mean : {df_mn.isnull().sum().sum()}")
        print(f"Missing features after replacing with mean :\n {df_mn.isnull().sum()}")
        print("The missing values in table after replacing with mean : ")
        print(df_mn.loc[self.df_index_with_nan])
        print("*-" * 50, end='\n\n')
        print("Now replaced NaN values with mean value dataframe is final dataframe for rest of the questions")
        self.df = df_mn
        global CLEANED_DATA
        CLEANED_DATA = self.df

class QUESTION2:
    def __init__(self):
        self.unique_cmp = None
        self.df = CLEANED_DATA
        self._ggl_df = None
        self._appl_df = None

    def get_unique(self):
        self.unique_cmp =self.df['symbol'].unique().tolist()
        print(f"Number of unique companies : {len(self.unique_cmp)}")
        print(f"Unique companies name : {self.unique_cmp}")

    def get_quantitative_qualitative(self):
        print("Quantitative predictors : ")
        print(self.df.select_dtypes(include=np.number).columns.tolist())
        print("Qualitative predictors : ")
        print(self.df.select_dtypes(include=np.object_).columns.tolist())

    def make_ggl_and_appl_df(self):
        self.app_gg_df = self.df[(self.df['symbol'] == 'AAPL') | (self.df['symbol'] == 'GOOGL')]

    def plot_ggl_appl_close(self):
        self.app_gg_df.loc[:, 'date'] = pd.to_datetime(self.app_gg_df['date'])
        plt.figure(figsize=(12,8))
        self.app_gg_df.pivot(index='date', columns='symbol', values='close').plot()
        plt.xlabel("Date")
        plt.ylabel("USD ($)")
        plt.title("Close Price of Google and Apple")
        plt.legend(["Apple", "Google"])
        plt.grid()
        plt.show()


class QUESTION3:
    def __init__(self):
        self.df = CLEANED_DATA
        self.df_agg = None

    def agg_df(self):
        self.df_agg = self.df.groupby(['symbol']).sum()
        print(f"Number of objects in the cleaned data set : {len(self.df)}")
        print(f"Number of objects in the aggregated data set : {len(self.df_agg)}")
        print(f"First 5 rows of the aggregated dataset : \n{self.df_agg[['open', 'high', 'low', 'close', 'volume', 'date']].head().to_string()}")

class QUESTION4:
    def __init__(self):
        self.df = CLEANED_DATA
        self.scl_df = CLEANED_DATA[['symbol', 'close', 'volume']]
        self.scl_df_agg = None

    def agg_df(self):
        self.scl_df_agg = self.scl_df.groupby(['symbol']).agg(['mean', 'var'])
        max_var = self.scl_df_agg.loc[self.scl_df_agg['close']['var'].idxmax()]
        print(f"Company that has the maximum variance in the closing cost : {max_var.name}")
        print(f"Maximum variance in the closing cost : {max_var['close']['var']:.2f}")

class QUESTION5:
    def __init__(self):
        self.start_date = '2015-01-01'
        self.df = CLEANED_DATA
        self.gg_df = None

    def make_ggl_df(self):
        self.gg_df = self.df.loc[(self.df['symbol'] == 'GOOGL') & (self.df['date'] > self.start_date)]

    def print_ggl_df(self):
        print(f"First 5 rows of the newly constructed dataset : \n{self.gg_df.head().to_string()}")

class QUESTION6(QUESTION5):
    def __init__(self):
        super().__init__()
        self.make_ggl_df()
        self.df = self.gg_df

    def plot_ggl_close(self):
        self.df.loc[:, 'date'] = pd.to_datetime(self.df['date'])
        self.df.set_index('date', inplace=True)
        rollong_window = self.df['close'].rolling(window=30, center = True).mean()
        print(f"Missed obv -> {rollong_window.isna().sum()}")
        rollong_window.plot()
        self.df['close'].plot()
        plt.xlabel("Date")
        plt.ylabel("USD ($)")
        plt.title("Close Price of Google with Rolling Window")
        plt.legend(["Close Price", "Avg"])
        plt.xticks(rotation=45)
        plt.grid()
        plt.show()

class QUESTION7(QUESTION5):
    def __init__(self):
        super().__init__()
        self.make_ggl_df()
        self.df = self.gg_df

    def plot_new_bins(self):
        lable_info = {
            'very low': 'blue',
            'low': 'orange',
            'normal': 'green',
            'high': 'red',
            'very high': 'purple'
        }
        self.df['price_category'] = pd.cut(self.df['close'], 5, labels=lable_info.keys(), ordered=False)
        self.df['price_category'].value_counts().plot(kind='bar', color=lable_info.values())
        plt.xlabel("Price Category")
        plt.ylabel("Frequency")
        plt.title("Equal width discretization")
        plt.grid()
        plt.xticks(rotation=45)
        plt.show()
        prnt_spc_info = self.df[['symbol', 'date', 'close', 'price_category']]
        print(f"First 5 rows of the newly constructed dataset : \n{prnt_spc_info.head().to_string()}")

class QUESTION8(QUESTION5):
    def __init__(self):
        super().__init__()
        self.make_ggl_df()
        self.df = self.gg_df

    def plot_new_bins(self):
        self.df['close'].hist(bins=5, color='orange', edgecolor='black')
        plt.xlabel("Close Price")
        plt.ylabel("Frequency")
        plt.title("Histogram of Close Price")
        plt.grid(True)
        plt.show()

class QUESTION9(QUESTION5):
    def __init__(self):
        super().__init__()
        self.make_ggl_df()
        self.df = self.gg_df

    def plot_new_bins(self):
        lable_info = {
            'very low': 'blue',
            'low': 'orange',
            'normal': 'green',
            'high': 'red',
            'very high': 'purple'
        }
        self.df['price_category'] = pd.qcut(self.df['close'], 5, labels=lable_info.keys())
        self.df['price_category'].value_counts().plot(kind='bar', color=lable_info.values())
        plt.xlabel("Price Category")
        plt.ylabel("Count")
        plt.title("Equal frequency discretization")
        plt.grid()
        plt.xticks(rotation=360)
        plt.show()
        prnt_spc_info = self.df[['symbol', 'date', 'close', 'price_category']]
        print(f"Rows of the newly constructed dataset : \n{prnt_spc_info.to_string(index=False)}")

class QUESTION10(QUESTION5):
    def __init__(self):
        super().__init__()
        self.make_ggl_df()
        self.df = self.gg_df[['open', 'high', 'low', 'close', 'volume']]

    def cal_cov_mat(self):
        total_obv = len(self.df)
        _df_ = pd.DataFrame(columns=self.df.columns, index=self.df.columns)
        for colmn_1 in self.df.columns:
            for colmn_2 in self.df.columns:
                cov_val = ((self.df[colmn_1] - self.df[colmn_1].mean()) * (self.df[colmn_2] - self.df[colmn_2].mean())).sum() / (total_obv -1)
                cov_val = round(cov_val, 2)
                _df_.loc[colmn_1, colmn_2] = cov_val
        _df_ = pd.DataFrame(_df_)
        print(f"Covariance Matrix : \n{_df_.to_string()}")

class QUESTION11(QUESTION5):
    def __init__(self):
        super().__init__()
        self.make_ggl_df()
        self.df = self.gg_df[['open', 'high', 'low', 'close', 'volume']]

    def cal_cov_mat(self):
        _df_ = self.df.cov()
        _df_ = _df_.round(2)
        print(f"Covariance Matrix using Built-in function : \n{_df_.to_string()}")

    def get_linear_relation(self):
        _df_ = self.df.corr()
        _df_ = _df_.round(2)
        print(f"Correlation Matrix using Built-in function : \n{_df_.to_string()}")


if __name__ == "__main__":
    print("Question 1 : "+ "*-" * 50)
    q1_obj = QUESTION1()
    q1_obj.ck_nan_value()
    print("Question 2 : "+ "*-" * 50)
    q2_obj = QUESTION2()
    q2_obj.get_unique()
    q2_obj.get_quantitative_qualitative()
    q2_obj.make_ggl_and_appl_df()
    q2_obj.plot_ggl_appl_close()
    print("Question 3 : "+ "*-" * 50)
    q3_obj = QUESTION3()
    q3_obj.agg_df()
    print("Question 4 : "+ "*-" * 50)
    q4_obj = QUESTION4()
    q4_obj.agg_df()
    print("Question 5 : "+ "*-" * 50)
    q5_obj = QUESTION5()
    q5_obj.make_ggl_df()
    q5_obj.print_ggl_df()
    print("Question 6 : "+ "*-" * 50)
    q6_obj = QUESTION6()
    q6_obj.plot_ggl_close()
    print("Question 7 : "+ "*-" * 50)
    q7_obj = QUESTION7()
    q7_obj.plot_new_bins()
    print("Question 8 : "+ "*-" * 50)
    q8_obj = QUESTION8()
    q8_obj.plot_new_bins()
    print("Question 9 : "+ "*-" * 50)
    q9_obj = QUESTION9()
    q9_obj.plot_new_bins()
    print("Question 10 : "+ "*-" * 50)
    q10_obj = QUESTION10()
    q10_obj.cal_cov_mat()
    print("Question 11 : "+ "*-" * 50)
    q11_obj = QUESTION11()
    q11_obj.cal_cov_mat()
    q11_obj.get_linear_relation()
