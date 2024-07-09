import  pandas as pd
import sys
def load_raw_data():
    print("Inside load_raw_data method of load_data step")
    heart_df = pd.read_csv('data/heart.csv')
    return  heart_df