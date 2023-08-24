import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

MaxT = 10000
Tstep = 500

filename = 'result.csv'

sns.set_style('darkgrid')

df = pd.read_csv(filename)
# print(df.columns)
new = df.loc[df['Testing'] == True]
# new['acrosstimeRa'] = []
# print(df['acrosstimeRa'])

# Showing location of cluster in pmRA pmDE plot
fig1 = plt.figure()
ax1 = fig1.add_subplot(1,1,1)
fig2 = plt.figure()
ax2 = fig2.add_subplot(1,1,1)
# ax1 = fig1.subplots(1)
ax1.plot(df['pmRA'], df['pmDE'], 'r.', label='Other Stars')
ax1.plot(new['pmRA'], new['pmDE'], 'b.', label='Hyades Cluster Stars')
ax1.set_xlabel('pmRA (mas/yr)')
ax1.set_ylabel('pmDE (mas/yr)')
ax1.legend()

# Getting the Convergent Point
for hip, pmra, pmdec, ra, dec in zip(new['HIP'], new['pmRA'], new['pmDE'], new['RArad'], new['DErad']):
    factor = 180/np.pi
    RAovertime = [ra * factor]
    DEovertime = [dec * factor]
    for t in range(MaxT):
        RAovertime.append(t * pmra * Tstep * 0.000277778 * 10**-3 + RAovertime[0])
        DEovertime.append(t * pmdec * Tstep * 0.000277778 * 10**-3 + DEovertime[0])
    ax2.plot(RAovertime, DEovertime, '--')
    ax2.set_xlabel('Right Ascension (deg)')
    ax2.set_ylabel('Declination (deg)')
    ax2.set_title('Extrapolating RA, DE coordinates using Proper Motion')

print(new['HIP'])
    # ax2.legend()
# RAtime = []
# DEtime = []
# for t in range(MaxT):
#     RAtime.append(t * Tstep)

# plt.show()