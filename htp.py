import pandas as pd 

'''
    Inputs: None

    Pull AZMET data from AZMET website for hourly values.

    Created df2 dataframe.  Adds no additional value to the application.
'''

def getData():

    # Reading the data from the AZMET website.
    df1 = pd.read_csv("https://cals.arizona.edu/AZMET/data/0620rd.txt")
    print(df1)

    df2 = df1.
    print(df2)

def main():
    getData()

if __name__ == '__main__':
    main()