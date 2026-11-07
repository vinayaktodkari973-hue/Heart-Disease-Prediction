import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score
heart=pd.read_csv(r"C:\Users\vinay\Downloads\archive\heart.csv")
#print(heart.head())
