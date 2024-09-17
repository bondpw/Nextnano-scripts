import nextnanopy as nn
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


nn.config

nn.config.get('nextnano++','exe')
nn.config.get_options('nextnano++')
nn.config.fullpath

my_input = nn.InputFile(r'C:\Users\bondpw\Documents\nextnano\input_files\InAs-InAsSb_infiniteSL.in')
my_input.set_variable('VBO_InAs',-0.72)
my_input.set_variable('VBO_InSb',1.18)
my_input.set_variable('bowpar',0.6)
my_input.set_variable('valbowpar',-0.9)

my_input.set_variable('tInAs',2.46)
my_input.set_variable('tInAsSb',13)
my_input.set_variable('xInAsSb',0.106)
my_input.set_variable('num_h',5)

my_input.save(overwrite=True)
my_input.config
my_input.execute()

datafile = nn.DataFile(r'C:\Users\bondpw\Documents\nextnano\nextnanopy\output\InAs-InAsSb_infiniteSL\bias_00000\Quantum\wf_amplitudes_shift_quantum_region_kp8_0000_SXYZ.dat', product = 'nextnano++')
datafilens = nn.DataFile(r'C:\Users\bondpw\Documents\nextnano\nextnanopy\output\InAs-InAsSb_infiniteSL\bias_00000\Quantum\wf_amplitudes_quantum_region_kp8_0000_SXYZ.dat', product = 'nextnano++')
datafileC = nn.DataFile(r'C:\Users\bondpw\Documents\nextnano\nextnanopy\output\InAs-InAsSb_infiniteSL\bias_00000\bandedges.dat', product = 'nextnano++')
'''
PEa = abs(datafilens.variables['Psi_4_s2_imag'].value)
PEmin = min(PEa)
PEu = PEa - PEmin

Phha = abs(datafilens.variables['Psi_1_z2_real'].value)
Phhmin = min(Phha)
Phh = Phha - Phhmin

Plha = abs(datafilens.variables['Psi_2_z2_real'].value)
Plhmin = min(Plha)
Plhu = Plha - Plhmin
'''

Ehh2 = datafile.variables['E_1'].value
Elh = datafile.variables['E_2'].value
Ehh = datafile.variables['E_4'].value
EE = datafile.variables['E_6'].value
'''
Plh = (-Plha)+Elh
Phh = (-Phha)+Ehh
PE = PEa + EE
'''
Bhh = datafileC.variables['HH'].value
Blh = datafileC.variables['LH'].value
BE = datafileC.variables['Gamma'].value
pos = datafile.coords['x'].value
posC = datafileC.coords['x'].value

#print("E-hh = "+str(EE[0]-Ehh[0]))
#print("E-lh = "+str(EE[0]-Elh[0]))


plt.rcParams.update({'font.size': 15})
f, ax = plt.subplots()
ax.plot(posC[0:-1],BE[0:-1],color = "Blue",label = "Gamma")
ax.plot(posC[0:-1],Blh[0:-1],color = "red",label = "Light-hole")
ax.plot(posC[0:-1],Bhh[0:-1],color = "green",label = "Heavy-hole")
#ax.plot(pos,Phh,color = "green",label = "$\Psi_{HH}$",linestyle="dashed")
#ax.plot(pos,Plh,color = "red",label = "$\Psi_{LH}$",linestyle="dashed")

#ax.plot(pos,PE,color = "Blue",label = "$\Psi_{e}$",linestyle="dashed")
#ax.plot(pos,Plhu, color = "red", label = "$\Psi_{lh}$",linestyle="dashed")
#ax.plot(pos,Phh, color = "green", label = "$\Psi_{hh}$",linestyle="dashed")
ax.plot(pos,Ehh2,color = "orange", linestyle = "dotted", label = "$E_{hh_{2}}$")
ax.plot(pos,Ehh,color = "green",linestyle = "dotted", label = "$E_{hh_{1}}$")
ax.plot(pos,Elh,color = "red",linestyle = "dotted", label = "$E_{lh_{1}}$")
ax.plot(pos,EE,color = "blue",linestyle = "dotted", label = "$E_{\Gamma}$")
#ax.axvspan(0,2.46, color = "red",alpha = 0.3)
#ax.axvspan(2.46,11.03, color = "orange",alpha = 0.3)
#ax.axvspan(11.03,13.49, color = "red",alpha = 0.3)
ax.legend(prop={'size': 10})
ax.set_ylabel("Energy (eV)")
ax.set_xlabel("Growth direction (nm)")
#ax.axvspan(13.49,22.06, color = "orange",alpha = 0.5)

plt.show()





