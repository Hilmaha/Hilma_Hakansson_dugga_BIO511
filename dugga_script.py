
#part 1

numbers = [15, -5, -12, 7, 10, -7, 3, -10, 4]

# a)
nums_above_10 = [] #empty list
for num in numbers:
    if abs(num) >= 10:
        nums_above_10.append(num) #if the absolute value of the number is above 10, add it to the list
print("sum of absolute values of numbers >= 10:", sum(abs(n) for n in nums_above_10)) #sum of the absolute values of the numbers in the list (since the numbers in the list are not the absolute numbers)


#b)
cubes = [] #empty list
for num in numbers:
    if num < 0:
        cubes.append(num ** 3) #if the numbers are negative, cube them and add them to the list
print("cubes of negative numbers:", cubes)

#c)
seen = []
for num in numbers:
    if abs(num) in seen:
        print("First repeated absolute value:", abs(num)) #if the absolute value of the number is already in the list, print its absolute value
        break #break after first repeated absolute value
    seen.append(abs(num)) #each absolute value that is not already in the list, will be added
else:
    print("No repeats") #if no repeats: all numbers will be added to the list without triggering the if statement


#part 2
import csv
import sys
import pandas as pd
import matplotlib.pyplot as plt

#2.1

input_file = sys.argv[1] #so that the user can input any file when running the script (python dugga_script.py <input_file>)

df = pd.read_csv(input_file, delimiter=',') #read the input file as a csv file into a dataframe


#2.2.1 + #2.2.3

def histogram(): #function to create and save a histogram of the column 'fpkm_log2' in the dataframe
    plt.hist(df['fpkm_log2'])
    plt.title('Distribution of of gene expression')
    plt.xlabel('Expression')
    plt.ylabel('Number of genes')
    plt.savefig('fpkm_distribution.png', dpi=300) #saves the histogram as a png file called 'fpkm_distribution.png'
    print("Histogram saved as 'fpkm_distribution.png'")

#2.2.2

print("made and saved histogram", histogram()) #calls the histogram function and prints that it was made and saved




