import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

def email_spam_classifier(training_file, testing_file):
    
    # --- training phase ---
    df = pd.read_csv(training_file, sep='\n', header=None, names=['message'])
    df['label'] = df['message'].str.split(' ').str[0]
    print("SOMETHING")