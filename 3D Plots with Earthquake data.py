import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

#Load data
eq_data = pd.read_csv("last5Years.csv",skiprows=1)

# define some boundaries for our box
lat_min,lon_min,lat_max,lon_max=-35,175,-15,190

# use Pandas filtering to fish out lat/lon in this range
box=eq_data[(eq_data.longitude.values%360<lon_max)&(eq_data.longitude.values%360>=lon_min)] # '%360' simply converts longitude in (-180,180) to (0,360)
box=box[(box.latitude.values<lat_max)&(box.latitude.values>=lat_min)]

# and export them to NumPy arrays
x=box.longitude.values%360 #Makes longitudes in new range (0-360)
y=box.latitude.values
z=-box.depth.values #Negative so that deeper earthquakes appear at the bottom)

fig=plt.figure(2,(14,14)) # let's make a new one.
ax1 = fig.add_subplot(121, projection='3d') # so we can do this.

ax1.scatter(x,y,z,c='r',marker='o')
ax1.set_xlabel('Longitude')
ax1.set_ylabel('Latitude')
ax1.set_zlabel('Depth (km)');


# Rotate or twirl the plot
elev = 30  # Set the elevation angle in degrees
azim = 0  # Set the azimuthal angle in degrees
ax1.view_init(elev=elev, azim=azim)   # default valeus for elev is 30 and tha for azim is -60.

ax2 = fig.add_subplot(122, projection='3d')

ax2.scatter(x,y,z,c='r',marker='o')
ax2.set_xlabel('Longitude')
ax2.set_ylabel('Latitude')
ax2.set_zlabel('Depth (km)');


# Rotate or twirl the plot
elev = 30  # Set the elevation angle in degrees
azim = 60  # Set the azimuthal angle in degrees
ax2.view_init(elev=elev, azim=azim)   # default valeus for elev is 30 and tha for azim is -60.

plt.show()
