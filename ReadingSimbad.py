import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

MaxT = 10000
Tstep = 500

# These values are obtained from the plots
ra_c = 98  # 90 - 106
dec_c = 7.5  # 5 - 13

filename = 'Hyades Data/result (2).csv'
filename = 'Pleiades Data/result.csv'

sns.set_style('darkgrid')

df = pd.read_csv(filename)
print(df.columns)
df['Hyades'] = np.where((17.5 <= df['pmra']) & (df['pmra'] <= 22.5) & ((-50 <= df['pmdec']) & (df['pmdec'] <= -40)), True, False)
# print(df['Radial velocity'])
# df['test'] =
# print(df)
# print(df.columns)D
df['theta'] = np.arccos(np.sin(np.deg2rad(df['dec']))*np.sin(np.deg2rad(dec_c)) +
          np.cos(np.deg2rad(df['dec']))*np.cos(np.deg2rad(dec_c))*np.cos(np.deg2rad(df['ra']-ra_c)))
df['pm'] = (df['pmra']**2 + df['pmdec']**2)**0.5
df['distance'] = (df['Radial velocity'] * 1000 * np.tan(df['theta']))/(4.74047 * df['pm'])

new = df.loc[df['Hyades'] == True]
# new['acrosstimeRa'] = []
# print(df['acrosstimeRa'])

# Showing location of cluster in pmRA pmDE plot
fig1 = plt.figure()
ax1 = fig1.add_subplot(1,1,1)
fig2 = plt.figure()
ax2 = fig2.add_subplot(1,1,1)
# ax1 = fig1.subplots(1)
ax1.plot(df['pmra'], df['pmdec'], 'r.', label='Other Stars')
ax1.plot(new['pmra'], new['pmdec'], 'b.', label='Hyades Cluster Stars')
ax1.set_xlabel('pmra (mas/yr)')
ax1.set_ylabel('pmdec (mas/yr)')
ax1.set_xlim(-50, 200)
ax1.set_ylim(-400, 200)
ax1.legend()

# Getting the Convergent Point
for hip, pmra, pmdec, ra, dec in zip(new['oid'], new['pmra'], new['pmdec'], new['ra'], new['dec']):
    factor = 1  # Change to 180/pi if ra, dec in radians
    RAovertime = [ra * factor]
    DEovertime = [dec * factor]
    for t in range(MaxT):
        RAovertime.append(t * pmra * Tstep * 0.000277778 * 10**-3 + RAovertime[0])
        DEovertime.append(t * pmdec * Tstep * 0.000277778 * 10**-3 + DEovertime[0])
    ax2.plot(RAovertime, DEovertime, ',')
    ax2.set_xlabel('Right Ascension (deg)')
    ax2.set_ylabel('Declination (deg)')
    ax2.set_title('Extrapolating RA, DE coordinates using Proper Motion')
avg = sum(new['distance'])/len(new.index)
plt.show()
# print(sum(new['distance']), len(new.index), sum(new['distance'])/len(new.index))
print(f'Average Distance: {avg:.2f} pc')

# plt.show()