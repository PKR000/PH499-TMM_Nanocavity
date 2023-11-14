

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


def read_csv(file_path):  #Function to read a csv file in and convert it to a numpy array    
    data = pd.read_csv(file_path)
    data = data.to_numpy(float)
    return data


#function to find the highest and lowest row and column whose value is within the threshold
def find_hi_lo(data):
    rmin, rmax = 790,0 #defaults to nonsensical values for error catching.
    cmin, cmax = 790,0
    max_val = 0.1

    for i in range(len(data)):
        for j in range (len(data[i])):
            if data[i][j] < max_val:
                if i < cmin:
                    rmin = i
                if i > cmax:
                    rmax = i
                if j < cmin:
                    cmin = j
                if j > cmax:
                    cmax = j 

    return [rmin, rmax, cmin, cmax]


#returns the bounds of each csv in a dataset as a single array
#IMPORTANT: the csv files are assumed to follow the naming convention "csv{i}.csv"
#they will not be read otherwise.
def find_bounds(dataset_folder):
    bounds = []
    directory = os.path.join(os.getcwd(),dataset_folder)
    num_files = len(os.listdir(directory))
    
    for i in range(1,num_files+1):
        file_name = f'csv{i}.csv'
        file_path = os.path.join(directory,file_name)
        data = read_csv(file_path)
        lims = find_hi_lo(data)
        bounds.append(lims)
    
    return bounds


#This imports all the test materials in the TestMaterials folder.
#IMPORTANT: the materials are assumed to follow the naming convention "____ for sensitivity.csv"
#they will not be read in otherwise.
def import_materials():
    directory = os.path.join(os.getcwd(),'TestMaterials')
    files = os.listdir(directory)
    filtered_files = [file for file in files if file.endswith(" for sensitivity.csv")]

    material_dict = {}
    for file in filtered_files:
        material_name = file.split(" for sensitivity.csv")[0]
        file_path = os.path.join(directory, file)
        material_data = read_csv(file_path)

        material_dict[material_name] = material_data
    
    return material_dict


#Attempting to make a loop to iterate over the materials dictionary and graph 3 at a time.
def test_materials():
    material_dict = import_materials()
    for i, (key, value) in enumerate(material_dict.items()):
        
        real = [row[1] for row in value]
        imag = [row[2] for row in value]



def main():

    data = find_bounds('CSVset2')
    materials_dict = import_materials()
    material_count = len(materials_dict)
    
    N_lower_lim = []
    N_upper_lim = []
    K_lower_lim = []
    K_upper_lim = []

    for i in range(1,82): #math for converting array index number to N and K values
        N_lower_lim.append(0.01*(data[i-1][0])+.09)
        N_upper_lim.append(0.01*(data[i-1][1])+.09)
        K_lower_lim.append(0.01*(data[i-1][2])+.09)
        K_upper_lim.append(0.01*(data[i-1][3])+.09)

    mat1 = materials_dict['Ti']
    mat2 = materials_dict['Cr']
    mat3 = materials_dict['nInSb']
    mat4 = materials_dict['nInAs']
    
    mat_prop_real1 = []
    mat_prop_real2 = []
    mat_prop_real3 = []
    mat_prop_real4 = []

    mat_prop_imag1 = []
    mat_prop_imag2 = []
    mat_prop_imag3 = []
    mat_prop_imag4 = []

    for i in range(11,92):
        mat_prop_real1.append(mat1[i,1])
        mat_prop_imag1.append(mat1[i,2])
    for i in range(11,92):
        mat_prop_real2.append(mat2[i,1])
        mat_prop_imag2.append(mat2[i,2])
    for i in range(11,92):
        mat_prop_real3.append(mat3[i,1])
        mat_prop_imag3.append(mat3[i,2])
    for i in range(11,92):
        mat_prop_real4.append(mat4[i,1])
        mat_prop_imag4.append(mat4[i,2])
    
    fig, (ax1, ax2) = plt.subplots(1,2,figsize=(13,5))
    x = np.linspace(400,800,81)

    #graphing for N values
    ax1.plot(x, mat_prop_real1, label='Ti')
    ax1.plot(x, mat_prop_real2, label='Cr')
    ax1.plot(x, mat_prop_real3, label='nInSb')
    ax1.plot(x, mat_prop_real4, label='nInAs')

    ax1.fill_between(x, N_lower_lim, N_upper_lim, alpha=.4, color='green',label='ideal N values')
    ax1.set_title('Range of optimal N values for an ideal material')
    ax1.set_ylim(.01,8)
    ax1.set_xlabel('Wavelength (nm)')
    ax1.set_ylabel('index of refraction (N)')
    ax1.legend()


    #graphing for K values
    ax2.plot(x, mat_prop_imag1, label='Ti')
    ax2.plot(x, mat_prop_imag2, label='Cr')
    ax2.plot(x, mat_prop_imag3, label='nInSb')
    ax2.plot(x, mat_prop_imag4, label='nInAs')

    ax2.fill_between(x, K_lower_lim, K_upper_lim, alpha=.4, color='teal',label='ideal K values')
    ax2.set_title('Range of optimal K values for an ideal material')
    ax2.set_ylim(.01,8)
    ax2.set_xlabel('Wavelength (nm)')
    ax2.set_ylabel('extinction coefficient (K)')
    plt.legend()

    plt.show()

main()






