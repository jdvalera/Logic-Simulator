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

