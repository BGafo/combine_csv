import pandas
import glob, os
import time

# time of execution
start_time = time.time()
cvs_files = glob.glob('/common/home/ey144/Random/*.csv', recursive=True)
#cvs_files = glob.glob('/common/home/ey144/Random/large_test_case/*.csv', recursive=True)
#cvs_files = glob.glob('/common/home/ey144/Random/my_test_cases/*.csv', recursive=True)
#print (files)
#['samples_for_so\\a.csv', 'samples_for_so\\b.csv', 'samples_for_so\\c.csv']


# to increase the number of print lines
pandas.options.display.max_rows = 99999999
res_df = pandas.concat([pandas.read_csv(line).assign(filename=os.path.basename(line)) for line in cvs_files])
#res_df = pd.concat([pd.read_csv(fp).assign(filename=os.path.basename(fp)) for fp in cvs_files])
print (res_df)

res_df.to_csv("Result CSV.CSV", index=False)

# to print only headers
print(res_df.head(0))

# to convert to string and print
#print(res_df.to_string()) 

# to show the max numbers showed printed lines to stdout
#print(pandas.options.display.max_rows)


print("--- %s seconds ---" % (time.time() - start_time))
