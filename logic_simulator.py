'''
CALIFORNIA STATE POLYTECHNIC
UNIVERSITY, POMONA
ECE 480:
Software Engineering
Project 1: Combinational Logic Simulator with Python
Winter 2014

John Valera
Omar Ramirez
Avis Kirakosyan
Hang Zhao
Jaran Francis
'''
from collections import deque
####################################################################################################################################

inputs = [0 for _ in range(50)] #input for each letter 1-26
output = [0 for _ in range(50)] #output for each gate 1 - 50

numbers = [] #numbers from 1-50 (number of gates)
for i in range(50):
    numbers.append(str(i+1))
    
letter_input = {}

alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split() #make a list of alphabet

for i in range(len(alphabet)): # map letters 'A'- 'Z' to element 0 - 25 of an array
    letter_input[alphabet[i]] = inputs[i]
    
outputs = {}
                                       
for i in range(50): #map output of each gate into an output array. Outputs 1-50 to Elements 0 - 49
    outputs[str(i+1)] = output[i]
                                       
file_in = [] #store each line of file in this array (going to be a 2-D array)

letters = [] #store the letters in the file from 'A' - 'Z' into this array to keep track of inputs (used for controling input values)

gate_in = [[] for _ in range(50)] #store inputs letters ('A','B'...) and input numbers ('1','2'...) into this array to input into each gate (used for making gates)

out_list = [[] for _ in range(50)] #2-D array that stores the output truth table in each element (each element is the gate output of each gate)

binary_seq = [] #binary sequence of inputs ex. 000 - 111

####################################################################################################################################

def AND(inputa): #and function 
    if inputa[0] in numbers:
        l = outputs[inputa[0]]
    else:
        l = letter_input[inputa[0]]
    for i in range(1,len(inputa)):
        if inputa[i] in numbers:
            l = bool(l) & bool(outputs[inputa[i]])
        else:
            l = bool(l) & bool(letter_input[inputa[i]])
    return int(l)

def NAND(inputa): #nand function 
    if inputa[0] in numbers:
        l = outputs[inputa[0]]
    else:
        l = letter_input[inputa[0]]
    for i in range(1,len(inputa)):
        if inputa[i] in numbers:
            l = bool(l) & bool(outputs[inputa[i]])
        else:
            l = bool(l) & bool(letter_input[inputa[i]])
    return int(not l)

def OR(inputa): #or function
    if inputa[0] in numbers:
        l = outputs[inputa[0]]
    else:
        l = letter_input[inputa[0]]
    for i in range(1,len(inputa)):
        if inputa[i] in numbers:
            l = bool(l) | bool(outputs[inputa[i]])
        else:
            l = bool(l) | bool(letter_input[inputa[i]])
    return int(l)

def NOR(inputa): #nor function 
    if inputa[0] in numbers:
        l = outputs[inputa[0]]
    else:
        l = letter_input[inputa[0]]
    for i in range(1,len(inputa)):
        if inputa[i] in numbers:
            l = bool(l) | bool(outputs[inputa[i]])
        else:
            l = bool(l) | bool(letter_input[inputa[i]])
    return int(not l)

def XOR(inputa): #xor function 
    if inputa[0] in numbers:
        l = outputs[inputa[0]]
    else:
        l = letter_input[inputa[0]]
    for i in range(1,len(inputa)):
        if inputa[i] in numbers:
            l = bool(l) ^ bool(outputs[inputa[i]])
        else:
            l = bool(l) ^ bool(letter_input[inputa[i]])
    return int(l)

def XNOR(inputa): #xnor function 
    if inputa[0] in numbers:
        l = outputs[inputa[0]]
    else:
        l = letter_input[inputa[0]]
    for i in range(1,len(inputa)):
        if inputa[i] in numbers:
            l = bool(l) ^ bool(outputs[inputa[i]])
        else:
            l = bool(l) ^ bool(letter_input[inputa[i]])
    return int(not l)

def NOT(inputa): #not function 
    if inputa[0] in numbers:
        return int(not outputs[inputa[0]])
    else:
        return int(not letter_input[inputa[0]])

####################################################################################################################################
    
gate = {'AND': AND, 'NAND': NAND, 'OR': OR, 'NOR': NOR, 'XOR': XOR, 'XNOR': XNOR, 'NOT':NOT} #tie gates to each function

####################################################################################################################################

filename = input("Enter a filename: ").strip()

if filename[-4:len(filename)] != '.txt': #if you leave out .txt it adds it in
    filename = filename + '.txt'
    
try:
    file = open(filename, "r") # (textfile, read)
except IOError:
    print('FILE DOES NOT EXIST')

lines = [line.upper() for line in file if line.strip()] #nevermind the white space

file.close() 
lines.sort()

#----------------------------------------------
def int2bin(intvalue, digit): #turns an integer into a binary string (used to make input sequence for 'A'-'Z'
    binstr = ''; val = intvalue
    while val>0:
        if val % 2 == 0:
            binstr = '0' + binstr
        else:
            binstr = '1' + binstr
        val = val >> 1
    if len(binstr)<digit:
        binstr = '0'*(digit-len(binstr)) + binstr
    return binstr

def transpose(m): #transposes a matrix
    m1length=len(m)
    temp=[x for elem in m for x in elem] #flatten matrix
    m2length=len(temp)
    num = m2length//m1length #number of rows
    trans_m = [[x[i] for x in m] for i in range(num)] #transpose matrix
    return trans_m

#-----------------------------------------------
file_in = [line.split() for line in lines] #tokenize each line and put it in a 2-D array



gate_num = [None for _ in range(len(file_in))] #initialize array length of gate_num with the amount of lines in file
gate_name = [None for _ in range(len(file_in))] #initialize array length of gate_name with the amount of lines in file
gate_type = [None for _ in range(len(file_in))] #initialize array length of gate_type with the amount of lines in file

for i in range(len(file_in)): #populate letters, gate_num, gate_name,gate_in,gate_type lists
    for j in range(3,len(file_in[i])):
        gate_in[i].append(file_in[i][j])
        if file_in[i][j] not in letters:
            if file_in[i][j] not in numbers:
                letters.append(file_in[i][j])
    gate_num[i] = file_in[i][0] 
    gate_name[i] = file_in[i][1]
    gate_type[i] = file_in[i][2]



bin_seq = [list(tuple(int2bin(i, len(letters)))) for i in range(2**len(letters))] # conversion integer --> binary string --> tuple --> list
bi_seq=[x for elem in bin_seq for x in elem] #flatten the list

bi_seq = deque(bi_seq) #turn flattened list into a double ended queue
bi_seqt = deque(bi_seq) #turn flattened list into a double ended queue

truth_in = [[] for _ in range(len(letters))] #make a 2-D list to store input sequence per input


user_out = {}
for i in range(2**len(letters)):
    for k in range(len(letters)):
        truth_in[k].append(int(bi_seqt.popleft())) #pop inputs to the input sequence 2-D list
        letter_input[letters[k]] = int(bi_seq.popleft()) #change input values in each gate, changing outputs
    for m in range(len(file_in)):
        outputs[gate_num[m]]=gate[gate_type[m]](gate_in[m]) #create each gate
        out_list[m].append(outputs[str(m+1)]) #create a 2-D list to store output sequence per output
        user_out[gate_name[m]] = out_list[m] #tie in gate_name with that gate's output



print('---------Circuit Listing--------')
for w in lines:
    print(w,end='')
print()

########## USER INPUT #########
user_input = input('Enter the outputs you want to track seperated by a comma: ') 
print()
tracked_out = []

user_input = user_input.upper().strip() #strip the user input and uppercase it
temp1 = user_input.split(',') #split the string based on commas and put it in the temp1 list
tracked_out = [i.strip() for i in temp1 if i.strip() in gate_name] #check if the user_inputs are valid


truth_matrix = truth_in #initialize truth_matrix list with the truth_in list

for i in tracked_out: #add each tracked output to the truth_matrix 2-D list
    truth_matrix = truth_matrix + [user_out[i]] #combine lists 


in_out = letters + tracked_out #labels for the truth table



######## TRUTH TABLE ########
for i in in_out:
    print("%10s" %i, end='')
print()
print()




transposed = transpose(truth_matrix)
for i in range(len(transposed)):
    for j in transposed[i]:
        print('%10s' %j,end='')
    print()

#------------------WRITING TO OUTPUT FILE------------

file = open("Output.txt", "w") #(new_textfile, write)

file.writelines('---------Circuit Listing--------\n')
for w in lines:
    file.writelines(w)

file.writelines('\n')

for i in in_out:
    file.writelines("%10s" %i)
    file.writelines(' ')
file.writelines('\n\n')

for i in range(len(transposed)):
    for j in transposed[i]:
        file.writelines('%10s ' %j)
    file.writelines('\n')

file.close()
