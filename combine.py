import pandas
import os
import sys

def main():

    cvs_files = sys.argv[1:]
    res_df = pandas.concat([pandas.read_csv(line).assign(filename=os.path.basename(line)) for line in cvs_files])
    print (res_df)
    # convert DataFrame to .csv
    res_df.to_csv("master_list.csv", index=False)

if __name__ == '__main__':
    main()
