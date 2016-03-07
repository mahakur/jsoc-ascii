import matplotlib.pyplot as plt
import seaborn
import matplotlib
matplotlib.rcParams['figure.figsize'] = (15, 8)
import numpy as np
import pandas as pd
from glob import glob

columns = ['n', 'l', 'k', 'nu', 'd_nu', 'ux', 'd_ux', 'uy', 'd_uy', 'fit', 'amp', 'd_amp', 'bg',
           'd_bg', 'fwhm', 'd_fwhm', 'delnu', 'd_nu', 'k_bin', 'nfe', 'min_func', 'rdchi']

files = glob("./data/*.out")

fig = plt.figure()
fig.suptitle('JSOC Data Plot', fontsize=20, fontweight='bold')
ax = fig.add_subplot(111)
ax.set_xlabel(r'${\ell}$', fontsize=18)
ax.set_ylabel(r'${\nu}$', fontsize=16) 
total_points = 0

for f in files:
    # print "Plotting :", f
    df = pd.read_csv(f,
                     delimiter=" ", skipinitialspace=True,
                     skiprows=10, 
                     names=columns, usecols=['l','nu'] )

    ax.scatter(df['l'],df['nu'], color='red', marker='o', s=4)
    total_points += len(df)

ax.set_title('Tiles:' + str(len(files)) + ' Observations:' + str(total_points), fontsize=12)
fig.savefig("output.png")
plt.close()
