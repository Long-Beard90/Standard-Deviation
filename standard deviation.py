# importing pandas (test only 55.)
import pandas as pd
# given list
given_list = [1,2,3,4]
# converting the given_list to DataFrame
dataList = pd.DataFrame(given_list)
# calculating the  standard devaition using std() function
standarddevList = dataList.std()
# print the given list and standard deviation
print("The given list of numbers : ")
for i in given_list:
    print(i, end=" ")
# printing new empty line
print()
# printing the standard deviation of the given list of numbers
print("Standard deviation of the given list =", standarddevList)
