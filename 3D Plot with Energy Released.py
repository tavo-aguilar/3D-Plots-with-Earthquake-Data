import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

eq_data = pd.read_csv("/Users/gustavoaguilar/Downloads/Datasets for Python Earth/EarthquakeLocations/last5Years.csv",skiprows=1)

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

ax2 = fig.add_subplot(122, projection='3d') # so we can do this.

ax2.scatter(x,y,z,c='r',marker='o')
ax2.set_xlabel('Longitude')
ax2.set_ylabel('Latitude')
ax2.set_zlabel('Depth (km)');


# Rotate or twirl the plot
elev = 30  # Set the elevation angle in degrees
azim = 60  # Set the azimuthal angle in degrees
ax2.view_init(elev=elev, azim=azim)   # default valeus for elev is 30 and tha for azim is -60.

#Mplot 3D subduction zones

#geographic box around the Marianas Trench
lat_min, lat_max = -35, -15
lon_min, lon_max = 175, 190

#earthquakes in the box
box = eq_data[
    (eq_data.longitude.values % 360 >= lon_min) &
    (eq_data.longitude.values % 360 < lon_max) &
    (eq_data.latitude.values >= lat_min) &
    (eq_data.latitude.values < lat_max)
]

#inspecting the filtered data
print("Columns in filtered DataFrame:")
print(box.columns.tolist())
print(f"\nNumber of earthquakes in box: {len(box)}")

#finding max and min magnitude
max_mag = box['mag'].max()
min_mag = box['mag'].min()
print(f"Largest earthquake magnitude: {max_mag}")
print(f"Smallest earthquake magnitude: {min_mag}")

#coordinates
x = box.longitude.values % 360           # Longitude (0–360)
y = box.latitude.values                   # Latitude
z = -box.depth.values                     # Depth (negative = downward)

# Create size array proportional to energy released
# Energy ∝ 10^(1.5 * mag) ≈ 32^mag  (since 10^1.5 ≈ 31.6)
mag = box['mag'].values
sizes_raw = 32 ** mag

#normalize by mean and scale to reasonable plot sizes
sizes = (sizes_raw / sizes_raw.mean()) * 10

#3D figure
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

#scatter plot
sc = ax.scatter(x, y, z,
                c='blue',
                s=sizes,
                alpha=0.7,           # transparency
                edgecolors='navy',
                linewidth=0.5,
                depthshade=True)

#labels and title
ax.set_xlabel('Longitude (°E)', fontsize=12, labelpad=15)
ax.set_ylabel('Latitude (°N)', fontsize=12, labelpad=15)
ax.set_zlabel('Depth (km)', fontsize=12, labelpad=15)
ax.set_title('Earthquakes near Marianas Trench (Last 5 Years)\n'
             'Marker size ∝ Energy Released (32^mag)',
             fontsize=14, pad=20)

#viewing angle to see the trench structure
ax.view_init(elev=25, azim=50)

ax.grid(True)

#plot
plt.tight_layout()
plt.show()