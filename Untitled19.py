#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[2]:


image_path = "C:\\Users\\asuwi\\Downloads\\pudgy_penguin.png"  # Add the path to your image
image = plt.imread(image_path)
gray_image = np.mean(image, axis=2)  # Convert to grayscale


# In[3]:


height_map = gray_image / np.max(gray_image)


# In[4]:


height, width = height_map.shape
x = np.linspace(0, width - 1, width)
y = np.linspace(0, height - 1, height)
X, Y = np.meshgrid(x, y)


# In[5]:


Z = height_map * 10  # Scale the height
vertices = np.column_stack((X.flatten(), Y.flatten(), Z.flatten()))


# In[6]:


faces = []
for i in range(height - 1):
    for j in range(width - 1):
        p1 = i * width + j
        p2 = (i + 1) * width + j
        p3 = i * width + (j + 1)
        p4 = (i + 1) * width + (j + 1)
        faces.append([p1, p2, p3])
        faces.append([p2, p4, p3])
faces = np.array(faces)


# In[7]:


mesh = (vertices, faces)


# In[8]:


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(mesh[0][:, 0], mesh[0][:, 1], mesh[0][:, 2], triangles=mesh[1], cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()


# In[ ]:




