import pandas as pd
from prettytable import PrettyTable
# These are the data sets that we will be using for this question
IRIS_DATA_SET = r'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
TIPS_DATA_SET = r'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
TITANIC_DATA_SET = r'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
DIAMONDS_DATA_SET = r'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv'
PENGUINS_DATA_SET = r'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv'

class QUESTION2:
    def __init__(self):
        self.iris_data = IRIS_DATA_SET
        self.tips_data = TIPS_DATA_SET
        self.titanic_data = TITANIC_DATA_SET
        self.dim_data = DIAMONDS_DATA_SET
        self.penguin_data = PENGUINS_DATA_SET
        self.list_data =[]

    def read_data(self, file_path: str) -> pd.DataFrame:
        # Read the data from the csv file
        df = pd.read_csv(file_path)
        return df

    def get_data_types(self):
        """
        Get data types from the data set
        In name variable string is passed to get the name of the data set from the path
        :param: dt_set, name: str, df: pd.DataFrame
        :return: None
        """
        _data_set_list = [self.iris_data, self.tips_data, self.titanic_data, self.dim_data, self.penguin_data]
        for dt_set in _data_set_list:
            df = self.read_data(dt_set)
            #Call print_data_type() to print the data type of the columns in the data set
            self.print_data_type(df, dt_set)
            name = dt_set.split('/')[-1].split('.')[0].upper()
            self.get_cat_num_typ(df, name)

    def print_data_type(self, df: pd.DataFrame, name: str) -> None:
        """
        Print the data type of the columns
        :param df: The data frame
        :param name: The name of the data set
        :return: None
        """
        print(f"{name} Data Set:")
        print(df.head(4).to_string())
        print(df.dtypes)

    def get_cat_num_typ(self, _data_set_: pd.DataFrame, _name_: str) -> None:
        """
        Get categorical and numerical data types from the data set.
        Dict is used to store the data and then append it to the list.
        :param _data_set_: The data set to be processed
        :return: None
        """
        cat_list = []
        num_list = []
        for i in _data_set_.columns:
            if _data_set_[i].dtype == 'object' or _data_set_[i].dtype == 'bool':
                cat_list.append(i)
            elif _data_set_[i].dtype == 'int64' or _data_set_[i].dtype == 'float64':
                num_list.append(i)
        total_obv = len(cat_list) + len(num_list)
        _dict = {'Dataset Title': _name_, 'Total Observations': total_obv, 'List of Categorical Features': cat_list,
                 'List of Numerical Features': num_list}
        self.list_data.append(_dict)

    def make_table(self):
        """
        Make table using prettytable
        :return: None
        """
        pt_obj = PrettyTable()
        pt_obj.field_names = ['Dataset Title', 'Total Observations', 'List of Categorical Features',
                              'List of Numerical Features']
        for i in self.list_data:
            pt_obj.add_row([i['Dataset Title'], i['Total Observations'], i['List of Categorical Features'],
                            i['List of Numerical Features']])
        print(pt_obj)

if __name__ == "__main__":
    q2 = QUESTION2()
    q2.get_data_types()
    q2.make_table()
