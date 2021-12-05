#importing
import pandas as pd
import csv
data = []
with open('Day3\input.txt', newline = '') as csvfile:
    inputlist = csv.reader(csvfile)
    for [item] in inputlist: data.append(item)


#part 1

head = [] #create header for dataframe
for n in range(1,len(data[0])+1): head.append('d'+str(n)) #name the columns in dataframe, not really important


df = pd.DataFrame(columns = head) #create blank dataframe with column header

for num in data:
    list = [] #create empty list, will be filled and appended to dataframe
    for char in num: #separates each digit in entry, puts in own entry in list
        list.append(char)
    df = df.append(pd.DataFrame([list], columns = head), ignore_index=True) #creates mini-dataframe and appends to large dataframe

modes = df.mode(axis=0).loc[0] #find modes of each column (the .loc[0] returns a series)

gamma = 0 #initialize gamma as 0
i = len(modes)-1 #set initial power for converting from binary to decimal
for num in modes: #binary conversion
    num = int(num)
    gamma += num*2**i
    i-=1

epsilon = 0
i = len(modes)-1
for num in modes:
    if int(num) == 1: num = 0 #flips 1's to 0's
    elif int(num) == 0: num = 1#flips 0's to 1's
    epsilon += num*2**i
    i-=1

print(gamma*epsilon)


#part 2

head = [] #create header for dataframe
for n in range(1,1+len(data[0])): head.append('d'+str(n)) #name the columns in dataframe, not really important


df = pd.DataFrame(columns = head) #create blank dataframe with column header

for num in data:
    list = [] #create empty list, will be filled and appended to dataframe
    for char in num: #separates each digit in entry, puts in own entry in list
        list.append(char)
    df = df.append(pd.DataFrame([list], columns = head), ignore_index=True) #creates mini-dataframe and appends to large dataframe


oxydf = df #copy dataframe to be modified for oxygen rating
for col in oxydf: #loop through each column
    zeroes = (oxydf[col] == '0').sum() #count zeroes
    ones = (oxydf[col] == '1').sum() #count ones
    if ones >= zeroes: mode = '1' #assigns mode with tie going to ones
    elif zeroes > ones: mode= '0'
    oxydf = oxydf[oxydf[col] == mode] #trims dataframe where digit in question matches mode
    if len(oxydf) == 1: oxybi = oxydf.iloc[0].to_list() #asigns binary number when one row is left


oxy = 0 #initialize oxygen rating to zero for binary conversion
i = len(oxybi)-1 #binary conversion
for num in oxybi:
    num = int(num)
    oxy += num*2**i
    i -= 1

codf = df #copy dataframe to be modified for oxygen rating
for col in codf: #loop through each column
    zeroes = (codf[col] == '0').sum() #count zeroes
    ones = (codf[col] == '1').sum() #count ones
    if ones < zeroes: mode = '1' #reverse mode with tie going to zeroes
    elif zeroes <= ones: mode= '0'
    codf = codf[codf[col] == mode] #trims dataframe where digit in question matches mode
    if len(codf) == 1: cobi = codf.iloc[0].to_list() #assigns binary number when one row is left

co = 0 #initializes co2 rating
i = len(cobi)-1 #binary conversion
for num in cobi:
    num = int(num)
    co += num*2**i
    i -= 1

lsr = oxy*co #life suppoort rating
print(lsr) #print answer


