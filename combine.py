import pandas
import os
import sys





def main():

    cvs_files = sys.argv[1:]

    # for inputs with a path
    #cvs_files = glob.glob('/pathname/*.csv', recursive=True)

    # to increase the number of print lines to stdout
    pandas.options.display.max_rows = 99999999

    res_df = pandas.concat([pandas.read_csv(line).assign(filename=os.path.basename(line)) for line in cvs_files])
    print (res_df)

    # to direct the output to a csv file
    #res_df.to_csv("Result CSV.CSV", index=False)

    # to print only headers
    #print(res_df.head(0))

if __name__ == '__main__':
    main()
