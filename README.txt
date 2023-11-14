

To use CSV Processing:

Ensure that the folder containing the python script also contains at least two folders;
one folder should be named TestMaterials while the other can be named anything else. In the code
the input folders are temporarily named CSVset1. Any naming convention will work.

The TestMaterials folder should contain your CSV files describing the complex index of refraction 
of that material. The CSV format is assumed to have 3 columns:
the first is the wavelength in micrometers, with a range from .35 to 1 and a step of .005
the second column is the real component of the index of refraction at that wavelength
the third column is the imaginary component at that wavelength.

The input folder must contain CSV files using the naming convention "csv1.csv", from 1 to 81.
The CSV contains the reflectivity of a simulated material stack at a given wavelength, where the 
columns are incrementing the real portion of the refractive index, and the rows increment the 
imaginary.

The program will run for roughly 10 to 45 seconds depending on your computer, after which it 
will return a set of graphs. These will show the ideal range of N and K values for a material 
stack.


