import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

titanic_DATA_SET = r'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'

class QUESTION5:
    def __init__(self):
        self.titanic_data = titanic_DATA_SET
        self.df = None
        self.df_with_na = None

    def read_csv(self, dataset) -> None:
        """
        Read csv file
        :param dataset:
        :return: None
        """
        self.df = pd.read_csv(dataset)

    def rem_na_obv(self) -> None:
        """
        Remove NA observations from the dataset ->
        1) Print the number of observations removed.
        2) Print the percentage of data eliminated
        :var: df_with_na
        :return: None
        """
        self.df_with_na = self.df.dropna()
        num_obv = len(self.df) - len(self.df_with_na)
        print(f"Number of missing observations: {num_obv}")
        perc_value = (len(self.df) - len(self.df_with_na)) / len(self.df) * 100
        sns.pairplot(df)
        plt.show()
        print(f"Percentage(%) of data is eliminated to clean the dataset: {perc_value} || {perc_value:.2f}")




if __name__ == '__main__':
    q5_obj = QUESTION5()
    q5_obj.read_csv(q5_obj.titanic_data)
    q5_obj.rem_na_obv()
