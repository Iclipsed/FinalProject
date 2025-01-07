import os
import pandas as pd

data = pd.read_csv("Dataset/2019.csv")
print(data.head(5))

def test_exists():
    # See if the dataset exists in the repo
    assert os.path.exists('Dataset/2019.csv'), "The dataset file must be missing."

def test_readable():
    #Can the datset be read clearly?
    data = pd.read_csv('Dataset/2019.csv')
    assert data is not None, "Couldn't read the dataset."

def test_notEmpty():
    # if the dataset is not empty
    data = pd.read_csv('Dataset/2019.csv')
    assert len(data) > 0, "The dataset ain't empty."