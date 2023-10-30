

import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import tmm
import tmm.examples
import matplotlib.pyplot as plt

#index of refraction; we would like to have some continuous function describing the complex nk values.
#if not possible, import data bases

inf = "inf"

#basic read-in function to grab material properties (but I dont like pandas DataFrames so convert to np arrays)
#the CSV files have the form lambda(.001nm), N, iK
try:
    SiO2_data = pd.read_csv("SiO2 for sensitivity.csv")
    Ag_data = pd.read_csv("Ag for sensitivity.csv")
except FileNotFoundError:
    print("File not found.")

SiO2_data = SiO2_data.to_numpy(float)
Ag_data = Ag_data.to_numpy(float)
print(SiO2_data)
print(Ag_data)


#main function
def Calculate():
    
    d_top = 35 #nm, top layer thickness
    d_mid = 125 #nm, test number

    #index of refraction of material: wavelength in nm versus index. This is for read-in files.
    #interpolates data into continuous function.
    material_nk_mid = SiO2_data    #test array
    material_nk_fn_mid = interp1d((material_nk_mid[:,0]*1000),
                              material_nk_mid[:,1] + material_nk_mid[:,2]*1j, kind='quadratic')

    material_nk_top = Ag_data    #test array
    material_nk_fn_top = interp1d((material_nk_mid[:,0]*1000),
                              material_nk_mid[:,1] + material_nk_top[:,2]*1j, kind='quadratic')

    #d_list is thickness of materials, lambda_list is 
    d_list = [inf,d_top, d_mid, inf] #in nm
    lambda_list = np.linspace(380, 800, 400) #in nm, this returns array of z evenly spaced numbers from x to y.
    T_list = []
    
    for lambda_vac in lambda_list:
        n_list = [1,material_nk_fn_top(lambda_vac) , material_nk_fn_mid(lambda_vac), 1]  #for each wavelength, solve material function and add to an N list
        T_list.append(tmm.coh_tmm('s', n_list, d_list, 0, lambda_vac)['R'])
    
    plt.figure()
    plt.plot(lambda_list, T_list)
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Fraction of power reflected')
    plt.title('Reflectivity at normal incidence')
    plt.show()

Calculate()

#_______________notes below______________________

#--To simulate a Fabry-Perot Nanocavity(FPN) analytically using Transfer Matrix Method(TMM)--
 
#assuming some structure of X interfaces and mediums we can collapse all the interactions into one transfer matrix describing energy in and out from either side of the surface.
#simplifying the TMM results in equations:

#eq.1:  E_in = M[0,0] * E_trans
#eq.2:  E_refl = M[1,0] * E_trans

#eq.1 yields the total transmission of our structure written as E_trans/E_in = 1/M[0,0]

#we can plug this into eq.2 to get a relation of the reflected wave and input wave
#E_refl = M[1,0] * E_in * 1/M[0,0]

#which can simplify to 
#eq.3:  R = E_refl/E_in = M[0,0]/M[1,0]

#This is our reflectivity.


#we will assume a constant material for base and middle layers of FPN, namely SiO and Al.
#variable k is defined as the wave number, or spacial frequency.

#for a P(propogation) matrix the resulting terms are:
#P_n[0,0] = exp(j*k_1*L_1)
#P_n[1,1] = exp(-j*k_1*L_1)

#for a D_nm(transmission) matrix applying fresnels equations, the terms are:



#the Matrix M is formulated by multiplying all of the matrices that describe the interactions through mediums and interfaces.

#M[] = D01[] * P1[] * D12[] * P2[] * D23[] * P3[]