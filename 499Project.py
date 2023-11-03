

import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import tmm
import matplotlib.pyplot as plt


#basic read-in function to grab material properties
#the CSV files have the form lambda(.001nm), N, iK
try:
    SiO2_data = pd.read_csv("SiO2 for sensitivity.csv")
    Ag_data = pd.read_csv("Ag for sensitivity.csv")
    Al_data = pd.read_csv("Al for sensitivity.csv")
except FileNotFoundError:
    print("File not found.")

#converting pandas DataFrame to numpy array of floats
SiO2_data = SiO2_data.to_numpy(float)
Ag_data = Ag_data.to_numpy(float)
Al_data = Al_data.to_numpy(float)
print(SiO2_data)  #testing to check data, can remove later
print(Ag_data)
print(Al_data)


#main function
def Calculate():
    inf = "inf"
    d_top = 40 #nm, top layer thickness
    d_mid = 150 #nm, Middle layer

    #index of refraction of material
    #interpolates data into continuous function.

    material_nk_top = Ag_data    #test array 1
    material_nk_fn_top = interp1d((material_nk_top[:,0]*1000),
                              material_nk_top[:,1] + material_nk_top[:,2]*1j, kind='quadratic')

    material_nk_mid = SiO2_data    #test array 2
    material_nk_fn_mid = interp1d((material_nk_mid[:,0]*1000),
                              material_nk_mid[:,1] + material_nk_mid[:,2]*1j, kind='quadratic')

    material_nk_bot = Al_data    #test array 3
    material_nk_fn_bot = interp1d((material_nk_bot[:,0]*1000),
                              material_nk_bot[:,1] + material_nk_bot[:,2]*1j, kind='quadratic')

    #d_list is thickness of materials
    d_list = [inf,d_top, d_mid, inf] #in nm, top and bottom must be inf
    lambda_list = np.linspace(400, 800, 400) #in nm, this returns array of z evenly spaced numbers from x to y.
    T_list = []
    
    for lambda_vac in lambda_list: #for each wavelength, solve material function and add to an N list
        n_list = [1,material_nk_fn_top(lambda_vac), material_nk_fn_mid(lambda_vac), material_nk_fn_bot(lambda_vac)]
        T_list.append(tmm.coh_tmm('s', n_list, d_list, 0, lambda_vac)['R'])
    
    plt.figure()
    plt.plot(lambda_list, T_list)
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Fraction of power reflected')
    plt.title('Reflectivity at normal incidence')
    plt.show()

Calculate()

