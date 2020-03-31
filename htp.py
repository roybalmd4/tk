import pandas as pd 

def getData():

    # Reading the data from the AZMET website.
    df1 = pd.read_csv("azmet.txt")
    print(df1)

