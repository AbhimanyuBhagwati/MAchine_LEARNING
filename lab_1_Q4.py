""" Question 4: Read the titanic dataset into a pandas dataframe. Print the first 5 rows of the dataframe. """
import pandas as pd
import prettytable as pt
titanic_DATA_SET = r'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'

class QUESTION4:
    def __init__(self):
        self.titanic_data = titanic_DATA_SET
        self.df = None
        self.df_num = None

    def read_csv(self, dataset):
        self.df = pd.read_csv(dataset)

    def sel_num_dtype(self):
        """
        Select numeric data type
        :return: None
        """
        self.df_num = self.df.select_dtypes(include=['number'])
        #print(self.df.select_dtypes(include=['int64', 'float64']).head(2).to_string())

    def print_df(self):
        """
        Print original and numeric data Create_table is used to print data in tabular format
        :var: org_table, new_table
        :return: None
        """
        org_table = self.create_table(self.df.head(5), 'Original Data')
        new_table = self.create_table(self.df_num.head(5), 'Numeric Data')
        print(org_table)
        print(new_table)

    def create_table(self, _df_, _title_=None) -> pt.PrettyTable:
        """
        Create table using PrettyTable
        :param: _df_, _title_ = None
        :return: pt_obj
        """
        pt_obj = pt.PrettyTable()
        pt_obj.field_names = _df_.columns
        pt_obj.title = _title_
        for row in _df_.itertuples():
            pt_obj.add_row(row[1:])
        return pt_obj


if __name__ == '__main__':
    q4_obj = QUESTION4()
    q4_obj.read_csv(q4_obj.titanic_data)
    q4_obj.sel_num_dtype()
    q4_obj.print_df()
