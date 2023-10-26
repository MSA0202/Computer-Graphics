
""" lab5 """
import numpy as np

# Define the coordinates and colors
ma = np.array([0.000, 0.000, 0.000])
md = np.array([0.000, 0.500, 0.500])
ms = np.array([0.500, 0.500, 0.500])
me = np.array([0.000, 0.000, 0.000])

la = np.array([0.000, 0.000, 0.000])
ld = np.array([0.500, 0.500, 0.000])
ls = np.array([0.500, 0.800, 0.500])

ga = np.array([0.000, 0.000, 0.000])
h = 0.25

light_position = np.array([-5.000, 0.000, 0.000])
point_P = np.array([-5.000, 2.000, 0.000])
normal_N = np.array([0.707, -0.707, 0.000])

# Calculate the vector L (direction from point P to the light source)
L = light_position - point_P
L /= np.linalg.norm(L)

# Calculate the vector V (direction from point P to the viewer, which is the negative of the point_P)
V = -point_P
V /= np.linalg.norm(V)

# Calculate the vector R (reflection vector)
R = 2 * np.dot(L, normal_N) * normal_N - L
R /= np.linalg.norm(R)

# Calculate the diffuse and specular components
diffuse = np.maximum(0, np.dot(L, normal_N)) * ld * md
specular = np.power(np.maximum(0, np.dot(V, R)), 1/h) * ls * ms

# Calculate the final intensity (I) for each color component (R, G, B)
I = me + ga + diffuse + specular

# Print the results
print("Vector L:", L)
print("Vector R:", R)
print("Vector V:", V)
print("Intensity (R, G, B):", I)


""" 2021 test1 """
""" Yes all correct """
""" import numpy as np

# Define the updated values
ma = np.array([0.000, 0.000, 0.000])
md = np.array([0.300, 0.000, 0.500])
ms = np.array([0.200, 0.100, 0.300])
me = np.array([0.000, 0.000, 0.000])

la = np.array([0.000, 0.000, 0.000])
ld = np.array([0.500, 0.500, 0.000])
ls = np.array([0.900, 0.900, 0.800])

ga = np.array([0.000, 0.000, 0.000])
h = 0.75

light_position = np.array([-5.000, 0.000, 0.000])
point_P = np.array([-6.000, 2.000, 0.000])
normal_N = np.array([0.894, -0.447, 0.000])

# Calculate the vector L (direction from point P to the light source)
L = light_position - point_P
L /= np.linalg.norm(L)

# Calculate the vector V (direction from point P to the viewer, which is the negative of the point_P)
V = -point_P
V /= np.linalg.norm(V)

# Calculate the vector R (reflection vector)
R = 2 * np.dot(L, normal_N) * normal_N - L
R /= np.linalg.norm(R)

# Calculate the diffuse and specular components
diffuse = np.maximum(0, np.dot(L, normal_N)) * ld * md
specular = np.power(np.maximum(0, np.dot(V, R)), 1/h) * ls * ms

# Calculate the final intensity (I) for each color component (R, G, B)
I = me + ga + diffuse + specular

# Print the results
print("Vector L:", L)
print("Vector R:", R)
print("Vector V:", V)
print("Intensity (R, G, B):", I) """
