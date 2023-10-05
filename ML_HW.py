import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.datasets import make_regression
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.datasets import make_blobs
class QUESTION:
    def __init__(self):
        pass

    def question1(self):
        x, y = make_regression(n_samples=1000, n_features=100, n_informative=100, n_targets=1, random_state=5805)
        col = ['Feature ' + str(i) for i in range(1, 101)]
        df_x = pd.DataFrame(x, columns=col)
        df_y = pd.DataFrame(y, columns=['Target'])
        df_x.round(2)
        df_y.round(2)
        print(df_x.head(5))
        print(df_y.head(5).to_string())

    def question2(self):
        x, y = make_regression(n_samples=1000, n_features=100, n_informative=100, n_targets=1, random_state=5805)
        col = ['Feature ' + str(i) for i in range(1, 101)]
        df_x = pd.DataFrame(x, columns=col)
        df_y = pd.DataFrame(y, columns=['Target'])
        df_x.round(2)
        df_y.round(2)
        df = pd.concat([df_x, df_y], axis=1)
        print(df.tail(5))

    def question3(self):
        x, y = make_regression(n_samples=1000, n_features=100, n_informative=100, n_targets=1, random_state=5805)
        col = ['Feature ' + str(i) for i in range(1, 101)]
        df_x = pd.DataFrame(x, columns=col)
        df_y = pd.DataFrame(y, columns=['Target'])
        df_x.round(2)
        df_y.round(2)
        df = pd.concat([df_x, df_y], axis=1)
        slc_df = df.iloc[:, 0:5]
        print(slc_df.tail(5))

    def question4(self):
        x, y = make_regression(n_samples=1000, n_features=100, n_informative=100, n_targets=1, random_state=5805)
        col = ['Feature ' + str(i) for i in range(1, 101)]
        df_x = pd.DataFrame(x, columns=col)
        df_y = pd.DataFrame(y, columns=['Target'])
        df_x.round(2)
        df_y.round(2)
        df = pd.concat([df_x, df_y], axis=1)
        slc_df = df.iloc[:, 0:5]
        mat_cr = slc_df.corr()
        mat_cv = slc_df.cov()
        print("Covariance Matrix")
        print(mat_cv)
        print("Correlation Matrix")
        print(mat_cr)

    def question5(self):
        x, y = make_regression(n_samples=1000, n_features=100, n_informative=100, n_targets=1, random_state=5805)
        col = ['Feature ' + str(i) for i in range(1, 101)]
        df_x = pd.DataFrame(x, columns=col)
        df_y = pd.DataFrame(y, columns=['Target'])
        df_x.round(2)
        df_y.round(2)
        df = pd.concat([df_x, df_y], axis=1)
        slc_df = df.iloc[:, 0:5]
        sns.pairplot(slc_df, markers='o')
        plt.figure(figsize=(5, 5))
        plt.show()

    def question6(self):
        x, y = make_regression(n_samples=1000, n_features=100, n_informative=100, n_targets=1, random_state=5805)
        col = ['Feature ' + str(i) for i in range(1, 101)]
        df_x = pd.DataFrame(x, columns=col)
        df_y = pd.DataFrame(y, columns=['Target'])
        df_x.round(2)
        df_y.round(2)
        df = pd.concat([df_x, df_y], axis=1)
        sns.scatterplot(x='Feature 1', y='Target', data=df)
        plt.grid()
        plt.xlabel('Feature 1')
        plt.ylabel('Target')
        plt.legend(['Feature 1', 'Target'])
        plt.title('Scatter Plot of Feature 1 and Target')
        plt.show()

    def questioin7(self):
        x, y = make_classification(n_samples=1000, n_features=100, n_informative=100, n_redundant=0, n_repeated=0,
                                    n_classes=4, random_state=5805)
        col = ['Feature ' + str(i) for i in range(1, 101)]
        df_x = pd.DataFrame(x, columns=col)
        df_y = pd.DataFrame(y, columns=['Target'])
        df_x.round(2)
        df_y.round(2)
        df = pd.concat([df_x, df_y], axis=1)
        print(df.head(5))
        print(df.tail(5))

    def question8(self):
        x, y = make_classification(n_samples=1000, n_features=100, n_informative=100, n_redundant=0, n_repeated=0,
                                    n_classes=4, random_state=5805)
        col = ['Feature ' + str(i) for i in range(1, 101)]
        df_x = pd.DataFrame(x, columns=col)
        df_y = pd.DataFrame(y, columns=['Target'])
        df_x.round(2)
        df_y.round(2)
        df = pd.concat([df_x, df_y], axis=1)
        slc_df = df.iloc[:, 0:5]
        sns.pairplot(slc_df, markers='o')
        plt.figure(figsize=(5, 5))
        plt.show()

    def question9(self):
        """
        Develop a python program that generates a synthetic isotropic Gaussian blob for clustering dataset with 5000 samples, 4 centers, 2 features and random state of 5805. Create a Dataframe that includes the features and the target variable. The row represents the # of observations and columns represents # of features. The last columns must represent the target. Rename the columns to ‘feature 1’,’ feature 2’ and the last column should be labeled as ‘target’
        """
        x, y = make_blobs(n_samples=5000, n_features=2, centers=4, random_state=5805)
        col = ['Feature 1', 'Feature 2']
        df_x = pd.DataFrame(x, columns=col)
        df_y = pd.DataFrame(y, columns=['Target'])
        df_x.round(2)
        df_y.round(2)
        df = pd.concat([df_x, df_y], axis=1)
        print(df.head(5))

    def question10(self):
        x, y = make_blobs(n_samples=5000, n_features=2, centers=4, random_state=5805)
        col = ['Feature 1', 'Feature 2']
        df_x = pd.DataFrame(x, columns=col)
        df_y = pd.DataFrame(y, columns=['Target'])
        df_x.round(2)
        df_y.round(2)
        df = pd.concat([df_x, df_y], axis=1)
        sns.scatterplot(x='Feature 1', y='Feature 2', hue='Target', data=df)
        plt.grid()
        plt.show()



if __name__ == "__main__":
    q_obj = QUESTION()
    print("Question 1")
    q_obj.question1()
    print("Question 2")
    q_obj.question2()
    print("Question 3")
    q_obj.question3()
    print("Question 4")
    q_obj.question4()
    print("Question 5")
    q_obj.question5()
    print("Question 6")
    q_obj.question6()
    print("Question 7")
    q_obj.questioin7()
    print("Question 8")
    q_obj.question8()
    print("Question 9")
    q_obj.question9()
    print("Question 10")
    q_obj.question10()