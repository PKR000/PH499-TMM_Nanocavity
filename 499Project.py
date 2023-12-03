

import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import tmm
import matplotlib.pyplot as plt
import csv
import os


def read_csv(file_path):  #Function to read a csv file in and convert it to a numpy array    
    data = pd.read_csv(file_path)
    data = data.to_numpy(float)
    return data


#basic read-in function to grab material properties
#the CSV files have the form lambda(.001nm), N, iK
try:
    SiO2_data = read_csv("SiO2 for sensitivity.csv")
    Ag_data = read_csv("Ag for sensitivity.csv")
    Al_data = read_csv("Al for sensitivity.csv")
except FileNotFoundError:
    print("File not found.")


def test_plot(file_path):
    data = read_csv(file_path)
    
    plt.plot(data)
    plt.imshow(data, cmap='viridis',origin='lower')
    plt.colorbar() 

    plt.xlabel('k value index')
    plt.ylabel('n value index')
    plt.show()


#main function
def Calculate():
    inf = "inf"
    d_top = 30 #nm, top layer thickness
    d_mid = 80 #nm, Middle layer

    #index of refraction of material
    #interpolates data into continuous function.
    material_nk_top = Ag_data    
    material_nk_fn_top = interp1d((material_nk_top[:,0]*1000), material_nk_top[:,1] + material_nk_top[:,2]*1j, kind='quadratic')

    material_nk_mid = SiO2_data    
    material_nk_fn_mid = interp1d((material_nk_mid[:,0]*1000), material_nk_mid[:,1] + material_nk_mid[:,2]*1j, kind='quadratic')

    material_nk_bot = Ag_data    
    material_nk_fn_bot = interp1d((material_nk_bot[:,0]*1000), material_nk_bot[:,1] + material_nk_bot[:,2]*1j, kind='quadratic')

    idx=1
    while idx < 82:
        with open(f'{idx}.csv',mode='w',newline='') as file:
            writer = csv.writer(file)
            
            wavelength = 400+((idx-1)/80)*400
            R_matrix = np.zeros((791,791))

            n = .1
            x = 0

            while n <= 8:
                k = .1
                y = 0

                while k <= 8:
                    n_list = (1, n+(k*1j), material_nk_fn_mid(wavelength), material_nk_fn_bot(wavelength))
                    d_list = (inf, d_top, d_mid, inf)
                    R = tmm.coh_tmm('s', n_list, d_list,0,wavelength)['R']
                    R_matrix[x,y] = R
                    k+=.01
                    y+=1

                n+=.01
                x+=1
            
            writer.writerows(R_matrix)
        idx+=1
    

def graph_reflectivity():
    inf = "inf"
    d_top = 30 #nm, top layer thickness
    d_mid = 110 #nm, Middle layer
    d_mid2 = 125
    d_mid3 = 140
    d_mid4 = 220

    #index of refraction of material
    #interpolates data into continuous function.
    material_nk_top = Ag_data    #test array 1
    material_nk_fn_top = interp1d((material_nk_top[:,0]*1000),
                              material_nk_top[:,1] + material_nk_top[:,2]*1j, kind='quadratic')

    material_nk_mid = SiO2_data    #test array 2
    material_nk_fn_mid = interp1d((material_nk_mid[:,0]*1000),
                              material_nk_mid[:,1] + material_nk_mid[:,2]*1j, kind='quadratic')

    material_nk_bot = Ag_data    #test array 3
    material_nk_fn_bot = interp1d((material_nk_bot[:,0]*1000),
                              material_nk_bot[:,1] + material_nk_bot[:,2]*1j, kind='quadratic')

    #d_list is thickness of materials
    d_list = [inf,d_top, d_mid, inf] #in nm, top and bottom must be inf
    d_list2 = [inf,d_top, d_mid2, inf]
    d_list3 = [inf,d_top, d_mid3, inf]
    d_list4 = [inf,d_top, d_mid4, inf]
    lambda_list = np.linspace(400, 800, 400) #in nm, this returns array of z evenly spaced numbers from x to y.
    T_list = []
    T_list2 = []
    T_list3 = []
    T_list4 = []
    for lambda_vac in lambda_list: #for each wavelength, solve material function and add to an N list
        n_list = [1,material_nk_fn_top(lambda_vac), material_nk_fn_mid(lambda_vac), material_nk_fn_bot(lambda_vac)]
        T_list.append(tmm.coh_tmm('s', n_list, d_list, 0, lambda_vac)['R'])
        T_list2.append(tmm.coh_tmm('s', n_list, d_list2, 0, lambda_vac)['R'])
        T_list3.append(tmm.coh_tmm('s', n_list, d_list3, 0, lambda_vac)['R'])
        T_list4.append(tmm.coh_tmm('s', n_list, d_list4, 0, lambda_vac)['R'])
    
    plt.figure()
    plt.plot(lambda_list, T_list, label='110nm')
    plt.plot(lambda_list, T_list2, label='125nm')
    plt.plot(lambda_list, T_list3, label='140nm')
   
    

    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Fraction of power reflected')
    plt.title('Reflectivity at normal incidence \n Ag, Si02, Ag')
    plt.legend()
    plt.show()

graph_reflectivity()
#Calculate()
