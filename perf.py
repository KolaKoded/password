# calculating the mean, standard deviation and variance of the students in the dataset
import pandas as pd

student_data = 'StudentsPerformance.csv'

df = pd.read_csv(student_data)

print(df.head())
print(df.columns)

# math score performance

print("Calculating Mean, Standard Deviation and Variance for Math Score...")
mean_math = df['math score '].mean()
print('Mean Value for Math Score = ' + str(mean_math)) #

sd_math = df['math score '].std()
print('Standard Deviation Value for Math Score = ' + str(sd_math))

var_math = df['math score '].var()
print('Variance Value for Math Score = ' + str(var_math))

print()

# reading score performance

print("Calculating Mean, Standard Deviation and Variance for Reading Score...")

mean_reading = df['reading score '].mean()
print('Mean Value for Reading Score = ' + str(mean_reading))

sd_reading = df['reading score '].std()
print('Standard Deviation Value for Reading Score = ' + str(sd_reading))

var_reading = df['reading score '].var()
print('Variance Value for Reading Score = ' + str(var_reading))

print()
# writing score performance

print("Calculating Mean, Standard Deviation and Variance for Writing Score...")
mean_writing = df['writing score'].mean()
print('Mean Value for Writing Score = ' + str(mean_writing))

sd_writing = df['writing score'].std()
print('Standard Deviation Value for Writing Score = ' + str(sd_writing))

var_writing = df['writing score'].var()
print('Variance Value for Writing Score = ' + str(var_writing)) 