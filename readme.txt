BIOMASS CALCULATION PROGRAM
Author: Nguyen Duc Viet
Date:	January 2022
------------------------------
Intro: The program using commonly used allometric equation to estimate individual tree biomass.

The main idea of the program is to use provided information of 
tree diameter, tree height, and tree biomass apply into predefined equations 
to generate a set of equation parameters that best fit the data. 
From determined parameters, the biomass value will be predicted. 
The predicted biomass and the actual biomass then will be compared 
by visualization and accuracy assessment.

The main program is under a while loop which only will be executed 
in case the user input is 1 or 2. The two options of input according to 
two options the program offers the users, 
which are processing the user’s data file or built-in data file, respectively. 
With the input of 1, users asked for their file path. 
On the other hand, the file path is set as “data_tree.csv” in case input of 2. 
There is also a chance to exit while loops (main program) with 0 input.

------------------------------
List of allometric equations
------------------------------
W = a + b×DBH			(1)
W = a + b×H				(2)
W = a + b×DBH + c×H		(3)
W = a + b×DBH2			(4)
W = a + b×DBH + c×DBH2	(5)
W = a + b×ln(DBH)		(6)
W = a + b×log(DBH)		(7)
W = a + b×DBH2 + c×H2	(8)
W = a + b×log(DBH2×H)	(9)
W = a×DBHb×Hc			(10)
Where: W- dry biomass, DBH - diameter at breast height, 
H - height, and a, b, c - model parameters.

------------------------------
Requirement for imported data
------------------------------
- Data file in CSV (comma-seperated) file format
- Decimals separated by dots
- Data contains at least three columns with exact names as DBH, H, AGB. 
	Column DBH, H, AGB contain data from diameter at breast height, 
	tree height and above-ground biomass, correspondingly.
- The units for the three columns DBH, H, AGB are centimeter (cm), meter (m) and kilogram (kg), respectively.

------------------------------
Metadata for 'data_tree' data:
------------------------------
DBH:	diameter at breast height (= 1.3 m above ground) in [cm] of each mapped tree
H:	height in [m] of each mapped tree
AGB:	above ground biomass of each mapped tree
