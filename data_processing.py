import pandas as pd

# Create a DataFrame using the csv data
df = pd.read_csv('./rain.csv')

#remove rows with the missing values
df_clean = df.dropna()

#count all rows that contain NaN
count_nan =0
for index, row in df.iterrows():
    if any(row.isnull()):
        count_nan = count_nan + 1

#mean
print('Mean:')
print(df_clean.mean())

#median
print('Median:')
print(df_clean.median())

#standard deviation
print('Standard Deviation:')
print(df_clean.std())

#mode
print('Mode:')
print(df_clean.mode())

# print the rainfall and mean for first few months
rainfall =  df_clean['Rainfall'][0:3]
print(rainfall,'\n')
print('Mean:', rainfall.mean(),'\n')

df_temp_rain = (df_clean[['Temperature', 'Rainfall']])
print(df_temp_rain)
print("Mean: \n",df_temp_rain.mean())

index= df_clean['Month']
df_indexed = df_clean.set_index(index)

#requires a properly indexed DataFrame
print("Finds a row by value \n", df_indexed.loc['March'])

