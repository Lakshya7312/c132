import csv
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("star_with_gravity.csv")

mass = df["Mass"].tolist()
radius = df["Radius"].tolist()
gravity = df["Gravity"].tolist()

mass.sort()
radius.sort()
gravity.sort()

plt.plot(radius, mass)
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.title("Radius and Mass of Stars")
plt.show()

plt.plot(mass, gravity)
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.title("Mass and gravity of stars")
plt.show()

plt.scatter(radius, mass)
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.title("Scatter plot of radius and mass")
plt.show()