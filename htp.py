import pandas as pd 

def getData():

    # Reading the data from the AZMET website.
    df1 = pd.read_csv("https://cals.arizona.edu/AZMET/data/0620rd.txt")
    print(df1)

    # df2 = df1.filter(df1.index[1])
    # print(df2)

def main():
    getData()

if __name__ == '__main__':
    main()