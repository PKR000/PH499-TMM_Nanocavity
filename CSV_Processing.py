

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def read_csv(file_number):
    file_path = f'csv{file_number}.csv'
    data = pd.read_csv(file_path)       #read in csv as dataframe
    data = data.to_numpy(float)  #change to numpy array
    return data

def read_mat(material):
    file_path = f'{material} for sensitivity.csv'
    test_mat = pd.read_csv(file_path)      
    test_mat = test_mat.to_numpy(float)
    return test_mat

#function to find the highest and lowest row and column within a threshold
#data must be a 2D array
def find_hi_lo(data):
    rmin, rmax = 790,0
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

#returns the bounds of each csv as a single array
def find_bounds():
    bounds = []
    for i in range(1,82):
        data = read_csv(i)
        lims = find_hi_lo(data)
        bounds.append(lims)
    return bounds

def plot_matrix(data):
    plt.imshow(data, cmap='viridis', interpolation='nearest')
    plt.colorbar()
    plt.title('N and K range for given data')
    plt.show()

def main():

    #data = find_bounds()
    #the data takes a solid 40 seconds to produce, faster to paste it in from a previous run.
    #can comment out this block and use find_bounds() to verify data
    data =[[49, 0, 528, 600], [71, 0, 481, 566], [93, 0, 440, 537], [114, 3, 403, 514],
      [134, 11, 371, 495], [155, 19, 341, 479], [175, 26, 315, 466], [195, 33, 291, 456], 
      [215, 41, 270, 447], [234, 49, 251, 441], [234, 56, 235, 436], [221, 64, 222, 432], 
      [209, 72, 210, 430], [200, 80, 201, 429], [193, 88, 193, 429], [188, 96, 187, 430], 
      [186, 103, 183, 432], [186, 111, 180, 434], [187, 118, 177, 437], [189, 124, 176, 441], 
      [191, 131, 175, 445], [194, 137, 174, 449], [197, 142, 175, 454], [200, 147, 175, 458], 
      [203, 152, 176, 464], [206, 157, 177, 469], [209, 161, 178, 474], [212, 165, 180, 480], 
      [215, 168, 182, 485], [218, 171, 184, 490], [221, 174, 186, 496], [224, 177, 188, 501], 
      [227, 179, 190, 507], [229, 181, 192, 512], [232, 183, 194, 517], [234, 185, 196, 522], 
      [236, 186, 199, 527], [238, 188, 201, 532], [240, 189, 203, 537], [242, 190, 205, 541], 
      [244, 190, 208, 545], [246, 191, 210, 550], [248, 192, 212, 554], [249, 192, 214, 557], 
      [251, 192, 216, 561], [252, 193, 218, 564], [253, 193, 219, 568], [254, 193, 221, 571], 
      [255, 193, 223, 574], [256, 193, 225, 576], [257, 193, 226, 579], [258, 192, 228, 581], 
      [259, 192, 229, 584], [260, 192, 230, 586], [261, 192, 231, 588], [261, 191, 233, 589], 
      [262, 191, 234, 591], [262, 191, 235, 593], [263, 190, 236, 594], [263, 190, 236, 595], 
      [264, 190, 237, 596], [264, 189, 238, 597], [264, 189, 239, 598], [264, 188, 239, 599], 
      [264, 188, 240, 599], [264, 187, 240, 600], [264, 187, 240, 600], [264, 187, 240, 601], 
      [264, 186, 241, 601], [264, 186, 241, 601], [264, 185, 241, 601], [264, 185, 241, 601], 
      [264, 184, 241, 601], [264, 184, 241, 601], [263, 184, 240, 601], [263, 183, 240, 601], 
      [263, 183, 240, 600], [262, 182, 239, 600], [262, 182, 239, 600], [261, 181, 239, 599], 
      [261, 181, 238, 599]]

    N_lower_lim = []
    N_upper_lim = []
    K_lower_lim = []
    K_upper_lim = []

    for i in range(1,82): #math for converting index number to N and K values
        N_lower_lim.append(0.01*(data[i-1][0])+.09)
        N_upper_lim.append(0.01*(data[i-1][1])+.09)
        K_lower_lim.append(0.01*(data[i-1][2])+.09)
        K_upper_lim.append(0.01*(data[i-1][3])+.09)

    mat1 = read_mat('Ti')
    mat2 = read_mat('Cr')
    mat3 = read_mat('nInSb')
    mat4 = read_mat('nInAs')
    
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






