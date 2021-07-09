import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as go
import statistics

df=pd.read_csv("StudentsPerformance.csv")
data_list=df["reading score"].to_list()

mean=statistics.mean(data_list)
median=statistics.median(data_list)
mode=statistics.mode(data_list)
std_deviation=statistics.stdev(data_list)

print("Mean of the data is {}".format(mean))
print("Median of the data is {}".format(median))
print("Mode of the data is {}".format(mode))
print("Standard deviation of the data is {}".format(std_deviation))

first_std_deviation_start, first_std_deviation_end= mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end= mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end= mean-(3*std_deviation), mean+(3*std_deviation)

list_of_data_within_one_std_deviation=[result for result in data_list if result>first_std_deviation_start and result<first_std_deviation_end]
list_of_data_within_two_std_deviation=[result for result in data_list if result>second_std_deviation_start and result<second_std_deviation_end]
list_of_data_within_three_std_deviation=[result for result in data_list if result>third_std_deviation_start and result<third_std_deviation_end]

print("{}% of data lie within 1 standard deviation".format(len(list_of_data_within_one_std_deviation)*100.0/len(data_list)))
print("{}% of data lie within 2 standard deviation".format(len(list_of_data_within_two_std_deviation)*100.0/len(data_list)))
print("{}% of data lie within 3 standard deviation".format(len(list_of_data_within_three_std_deviation)*100.0/len(data_list)))