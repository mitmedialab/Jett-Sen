import matplotlib
matplotlib.use('GTK3Agg')

import matplotlib.pyplot as plt
import seaborn as sns; sns.set()  # for plot styling
import numpy as np
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec
from sklearn import preprocessing

current_data = np.genfromtxt('/home/andres/panasonic_intelligence/Bike_data.txt', delimiter = ',',  dtype='str')
time_label = np.zeros(current_data.shape[0])

torque = current_data[:,[8]] #Minus one for Yasushi Data File
torque = torque.astype(np.float)
torque = ((torque - np.amin(torque)) / (np.amax(torque) - np.amin(torque)))

x_accel = current_data[:,[20]]
x_accel = x_accel.astype(np.float)
x_accel = ((x_accel - np.amin(x_accel)) / (np.amax(x_accel) - np.amin(x_accel)))

y_accel = current_data[:,[21]]
y_accel = y_accel.astype(np.float)
y_accel = ((y_accel - np.amin(y_accel)) / (np.amax(y_accel) - np.amin(y_accel)))


z_accel = current_data[:,[22]]
z_accel = z_accel.astype(np.float)
z_accel = ((z_accel - np.amin(z_accel)) / (np.amax(z_accel) - np.amin(z_accel)))

speed = current_data[:,[18]]
speed = speed.astype(np.float)
speed = ((speed - np.amin(speed)) / (np.amax(speed) - np.amin(speed)))

temp = current_data[:,[23]]
temp = temp.astype(np.float)
temp = ((temp - np.amin(temp)) / (np.amax(temp) - np.amin(temp)))

light = current_data[:,[24]]
light = light.astype(np.float)
light = ((light - np.amin(light)) / (np.amax(light) - np.amin(light)))

hum = current_data[:,[25]]
hum = hum.astype(np.float)
hum = ((hum - np.amin(hum)) / (np.amax(hum) - np.amin(hum)))

pressure = current_data[:,[27]]
pressure = pressure.astype(np.float)
pressure = ((pressure - np.amin(pressure)) / (np.amax(pressure) - np.amin(pressure)))

number = 0
for numbers in range(current_data.shape[0]):
    time_label[numbers] = number
    number = number + 1

#print (time_label)

X = np.hstack((x_accel,y_accel))
X = np.hstack((X,z_accel))
X = np.hstack((X,torque))
X = np.hstack((X,speed))
X = np.hstack((X,temp))
X = np.hstack((X,light))
X = np.hstack((X,hum))
X = np.hstack((X,pressure))

print(X)

sse = []
list_k = list(range(1, 50))

for k in list_k:
    km = KMeans(n_clusters=k)
    km.fit(X)
    sse.append(km.inertia_)

# Plot sse against k

plt.style.use('dark_background')

plt.figure(figsize=(6, 6))
plt.plot(list_k, sse, '-o')
plt.xlabel(r'Number of clusters *k*')
plt.ylabel('Sum of squared distance');

plt.show()