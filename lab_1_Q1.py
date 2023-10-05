""" LAB 1 Question 1 """
import seaborn as sns

class QUESTION1:
    def print_gvn_info(self) -> None:
        """
        Print package dataset names in seaborn
        :return: None
        """
        gvn_info = sns.get_dataset_names()
        for dataset in gvn_info:
            print(dataset)


if __name__ == "__main__":
    q1 = QUESTION1()
    q1.print_gvn_info()
