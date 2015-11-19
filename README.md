# Combinational Logic Simulator
###### By: John Valera, Omar Ramirez, Avis Kirakosyan, Hang Zhao Jaran Francis

### Description

Python program used to simulate a combinational logic gate circuit. The program reads a combinational logic description file (LDF) and generates the truth table for the user-selected outputs.

### Project Specifications

* The number of primary inputs is limited to 26.
* The number of user-selected outputs is limited to 26.
* The fan-in for each gate is 8.
* The following gate types are supported: NOT, AND, OR, XOR, NAND, NOR, XNOR.
* The gate count in each circuit is limited to 50.
* Each line of the LDF is formatted like so: `<Gate Number> <Name> <Type> [<Input1>...<Input8>]`
* The gate numbers are continuous, beginning with 1.

### Project Package
**logic_simulator.py** - The main python file that holds all the logic for generating the truth tables. <br>
**input_1a.txt** - Input test file. <br>
**input_2a.txt** - Input test file. <br>
**input_3a.txt** - Input test file. <br>
**Ece480_Project1_Report.pdf** - Detailed report on logic_simulator.py <br>

### Running the program

1. Clone this repo `git clone https://github.com/jdvalera/Logic-Simulator.git`
2. Run `logic_simulator.py` (Python v3)
3. When prompted to enter a file name type one of the following test filed (input_1a, input_2a, input_3a) like so: `Enter a filename: input_1a`
4. When prompted to enter the outputs you want to track, choose any of the gate names. <br>Example:                          `Enter the outputs you want to track seperated by a comma: SUM, CARRY`
5. The output table will be printed on the shell. The program will generate an output file named `Output.txt`.
6. The output will look like this: <br> 
```
  A          B          C        SUM      CARRY 

  0          0          0          0          0 
  0          0          1          1          0 
  0          1          0          1          0 
  0          1          1          0          1 
  1          0          0          1          0 
  1          0          1          0          1 
  1          1          0          0          1 
  1          1          1          1          1 
```



