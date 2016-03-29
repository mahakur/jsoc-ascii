import matplotlib.pyplot as plt
import seaborn
import matplotlib
matplotlib.rcParams['figure.figsize'] = (15, 8)
import numpy as np
import pandas as pd
from glob import glob

columns = ['n', 'l', 'k', 'nu', 'd_nu', 'ux', 'd_ux', 'uy', 'd_uy', 'fit', 'amp', 'd_amp', 'bg',
           'd_bg', 'fwhm', 'd_fwhm', 'delnu', 'd_nu', 'k_bin', 'nfe', 'min_func', 'rdchi']

files = glob("./15dg_test/*.out")

fig = plt.figure()

fig.suptitle('Mode Amplitude', fontsize=20, fontweight='bold')
ax = fig.add_subplot(111)
ax.set_xlabel(r'${\nu (\mu Hz)}$', fontsize=18)
ax.set_ylabel(r'${\Lambda}$', fontsize=16) 
total_points = 0

for f in files:
    # print "Plotting :", f
    df = pd.read_csv(f,
                     delimiter=" ", skipinitialspace=True,
                     skiprows=10, 
                     names=columns, usecols=['nu','amp'] )

    ax.scatter(df['nu'],df['amp'], color='red', marker='.', s=6)
    total_points += len(df)

ax.set_title('Tiles:' + str(len(files)) + ' Observations:' + str(total_points), fontsize=12)
fig.savefig("output.png")
plt.close()
