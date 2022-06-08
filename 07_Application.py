"""
This task is very much related to data analytics and machine learning and involves various errors that are relatively
common in projects.
Run the program and gradually solve the problems using the debugger. Some errors can be fixed quickly, others are not
directly obvious and belong more to the semantic errors (program works, but does not deliver the expected output).
"""
from pathlib import Path
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
from typing import List, Tuple, Union, Iterable


def load_dataset(path: Path) -> pd.DataFrame:
    dataset = pd.DataFrame()
    for file in os.listdir(path):
        df = pd.read_csv(path.joinpath(file), index_col=0)
        df['label'] = file.split('_')[0]
        dataset = pd.concat([dataset, df], axis=1)
    dataset = dataset.drop(columns=['time'], inplace=True)
    return dataset


def plot_clusters_3d(dataset: pd.DataFrame, plot_columns: List[Tuple[str, str, str]], label_col: str, title: str = ''):
    # Create figure and add 3d subplot
    fig = plt.figure()
    fig.suptitle(title, fontsize=16)
    subplots = []
    for i in range(len(plot_columns)):
        subplot = int(f'{1}{len(plot_columns)}{i + 1}')
        subplots.append(fig.add_subplot(subplot, projection='3d'))
    # Scatter points in each subplot using the set attributes
    for index, ax in enumerate(subplots):
        x, y, z = plot_columns[index]
        ax.set(xlabel=x, ylabel=y, zlabel=z)
        for label in np.unique(dataset[label_col]):
            relevant_rows = dataset[dataset[label_col] == label]
            ax.scatter(relevant_rows[x], relevant_rows[y], relevant_rows[z], label=label)
        ax.legend()
    plt.show()


def plot_confusion_matrix(y_true: Union[np.ndarray, Iterable], y_pred: Union[np.ndarray, Iterable], title: str = ''):
    cm = confusion_matrix(y_true=y_true, y_pred=y_pred, normalize='true')
    labels = np.unique(y_true)
    fig, axs = plt.subplots()
    fig.suptitle(title, fontsize=16)
    sns.heatmap(cm, annot=True, fmt='.2f', ax=axs, cmap='Blues', xticklabels=labels, yticklabels=labels)
    plt.show()


def main():
    # Load the dataset from the data folder
    dataset = load_dataset(Path('data'))

    # Plot some values to get first impression of the data
    plot_clusters_3d(dataset=dataset, plot_columns=[('x_mean', 'y_mean', 'z_mean'), ('x_std', 'y_std', 'z_std')],
                     label_col='label', title='Mean and Std of all three Axis')

    # Prepare the data for Machine Learning by splitting into train and test partition
    features = pd.get_dummies(dataset, columns=['label'])
    labels = dataset['label']
    x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

    # Scale the data to speed up the training
    scaler = StandardScaler()
    scaler.fit(x_train)
    x_train = scaler.transform(x_train)

    # Fit the model
    model = SVC()
    model.fit(x_train, y_test)
    print(f'Train Score = {model.score(x_train, y_train)}')

    # Predict the test data and evaluate the predictions
    y_pred = model.predict(x_test)
    print(f'Test Accuracy = {accuracy_score(y_test, y_pred)}')
    plot_confusion_matrix(y_true=y_test, y_pred=y_pred, title='Test Confusion Matrix')


if __name__ == '__main__':
    main()
