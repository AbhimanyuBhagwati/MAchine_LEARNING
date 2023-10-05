import pandas as pd
import prettytable as pt
pt_obj = pt.PrettyTable()
TITANIC_DATA_SET = r'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'


class QUESTION3:
    def __init__(self):
        self.dataset = TITANIC_DATA_SET
        self.df = None

    def read_csv(self) -> None:
        """
        Read csv file
        :var: df
        :return: None
        """
        self.df = pd.read_csv(self.dataset)

    def disp_cnt_mean_std_min_25_50_75_max(self) -> None:
        """
        Display the count, mean, std, min, 25%, 50%, 75% and max for the loaded dataset.
        :return: None
        """
        self.df = self.df.describe(include='all')
        self.df.drop(['unique', 'top', 'freq'], axis=0, inplace=True)
        #using prettytable to display the data
        self.df.fillna("N/A", inplace=True)
        pt_obj.title = "Display the count, mean, std, min, 25%, 50%, 75% and max for the loaded dataset."
        #add name to row index
        self.df.index.name = "Parameters"
        self.df.reset_index(inplace=True)
        pt_obj.field_names = self.df.columns
        #add data to table
        for i in range(len(self.df)):
            pt_obj.add_row(self.df.iloc[i])
        print(pt_obj)

    def cal_missing_values(self) -> None:
        """
        Calculate the missing values in the dataset
        :return: None
        """
        if self.df.isna().sum().sum() == 0:
            print("No missing values in the dataset")
        else:
            print(f"Missing values in the dataset: {self.df.isna().sum().sum()}")

    def ident_nom_ord_ratio_int(self):
        """
        Identify the number of ordinal, nominal and ratio interval attributes in the dataset
        :return: None
        """
        nom, ord_, fl_type, int_type = 0, 0, 0, 0
        nom_name, ord_name, fl_name, int_name = [], [], [], []
        for i in self.df.columns:
            if self.df[i].dtype == 'object':
                nom += 1
                nom_name.append(i)
            elif self.df[i].dtype == 'int64':
                int_type += 1
                int_name.append(i)
            elif self.df[i].dtype == 'float64':
                fl_type += 1
                fl_name.append(i)
            else:
                ord_ += 1
                ord_name.append(i)
        print(f"Number of ordinal attributes: {ord_} || {ord_name}")
        print(f"Number of nominal attributes: {nom} || {nom_name}")
        print(f"Number of ratio interval attributes: {fl_type} || {fl_name}")
        print(f"Number of interval attributes: {int_type} || {int_name}")


if __name__ == "__main__":
    q3_obj = QUESTION3()
    q3_obj.read_csv()
    q3_obj.cal_missing_values()
    q3_obj.ident_nom_ord_ratio_int()
    q3_obj.disp_cnt_mean_std_min_25_50_75_max()
