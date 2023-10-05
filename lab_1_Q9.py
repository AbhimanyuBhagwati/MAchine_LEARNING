import matplotlib.pyplot as plt
from lab_1_Q8 import QUESTION8 as Q8

class QUESTION9:
    def __init__(self):
        q8_obj = Q8()
        q8_obj.read_csv()
        self.df_num = q8_obj.get_num_obv()
        print(self.df_num.to_string())

    def plot_age_graph(self) -> None:
        """
        Plot Histogram for Age & Fare
        :return: None
        """
        plt.hist(self.df_num['age'], bins=10, label='Age')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.title('Age Graph')
        plt.grid(True)
        plt.legend()
        plt.show()

    def plot_fare_graph(self) -> None:
        """
        Plot Histogram for Age & Fare
        :return: None
        """
        #use log scale to see the distribution better especially on y-axis
        plt.yscale('log')
        plt.hist(self.df_num['fare'], bins=10, label='Fare', color='red')
        plt.xlabel('Fare')
        plt.ylabel('Frequency')
        plt.title('Fare Graph')
        plt.grid(True)
        plt.legend()
        plt.show()


if __name__ == "__main__":
    q9_obj = QUESTION9()
    q9_obj.plot_age_graph()
    q9_obj.plot_fare_graph()
