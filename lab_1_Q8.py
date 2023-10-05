import pandas as pd
import numpy as np
titanic_DATA_SET = r'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'

class QUESTION8:
    def __init__(self):
        self.titanic_data = titanic_DATA_SET
        self.df = None
        self.df_num = None
        self.arith_mean, self.harmonic_mean, self.geometric_mean = {}, {}, {}

    def read_csv(self) -> pd.DataFrame:
        """
        Read given csv file
        :param dataset: csv file
        :return: pd.DataFrame
        """
        self.df = pd.read_csv(self.titanic_data)
        return self.df

    def get_num_obv(self) -> pd.DataFrame:
        """
        Get number of observations in the dataset
        :return: pd.DataFrame
        """
        self.df_num = self.df.select_dtypes(include=['number'])
        return self.df_num

    def cal_arith_mean(self) -> None:
        """
        Calculate arithmetic mean
        :return: None
        """
        all_value = self.df_num.describe().loc['mean']
        for clm in self.df_num.columns:
            self.arith_mean[clm] = all_value[clm]

    def cal_stat_mean(self) -> None:
        """
        Calculate harmonic, Geometric mean calling respective functions
        1)cal_harmonic_mean()
        2)cal_geometric_mean()
        :return: None
        """
        clm_list = self.df_num.columns
        for clm in clm_list:
            hm_value = self.cal_harmonic_mean(self.df_num[clm].to_numpy())
            gm_value = self.cal_geometric_mean(self.df_num[clm].to_numpy())
            self.harmonic_mean[clm] = hm_value
            self.geometric_mean[clm] = gm_value

    def cal_harmonic_mean(self, value: np.ndarray) -> [float, int, str]:
        """
        Add inverse of each value in the array
        :param value:
        :return: [float, int, str]
        """
        len_obv = len(value)
        sum = 0
        status = True
        for ele in value:
            try:
                sum += 1/float(ele)
            except ZeroDivisionError:
                status = False

        if status:
            return len_obv/sum
        else:
            return "ZeroDivisionError and DataSet contains 0"

    def cal_geometric_mean(self, value: np.ndarray) -> [float, int, str]:
        """
        Calculate geometric mean
        :return: [float, int, str]
        """
        len_obv = len(value)
        sum = 1
        status = True
        for ele in value:
            if ele == 0:
                status = False
                break
            else:
                sum *= float(ele)
        if status:
            return sum**(1/len_obv)
        else:
            return "DataSet contains 0"

    def print_all_va(self) -> None:
        """
        Gets all values calling get_all_value() function
        :param: dict_value: Dictionary of values
        :return: None
        """
        self.get_all_value(self.arith_mean, "Arithmetic")
        self.get_all_value(self.harmonic_mean, "Harmonic")
        self.get_all_value(self.geometric_mean, "Geometric")

    def get_all_value(self, dict_value: dict, op_type: str) -> None:
        """
        Print all values in the dictionary Arithmetic mean, Harmonic mean, Geometric mean
        :return: None
        """
        for key, value in dict_value.items():
            if type(value) == str:
                print(f"{op_type} mean of {key} is Undefined due to {value}")
            else:
                print(f"{op_type} mean of {key} is : {value:.2f} || {value}")


if __name__ == "__main__":
    q8_obj = QUESTION8()
    q8_obj.read_csv()
    q8_obj.get_num_obv()
    q8_obj.cal_stat_mean()
    q8_obj.cal_arith_mean()
    q8_obj.print_all_va()
