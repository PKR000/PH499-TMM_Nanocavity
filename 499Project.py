
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



import scipy as sp
import numpy as np
import colorpy as cp
import math


