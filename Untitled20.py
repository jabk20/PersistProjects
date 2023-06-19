#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install trimesh


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import trimesh


# In[18]:


# Load the 2D image (grayscale)
image_path = "C:\\Users\\asuwi\\Downloads\\images.jpg"  # Add the path to your image
image = plt.imread(image_path)
gray_image = np.mean(image, axis=2)  # Convert to grayscale


# In[19]:


# Define the height map
height_map = gray_image / np.max(gray_image)  # Normalize to [0, 1]


# In[20]:


# Create mesh grid
height, width = height_map.shape
x = np.linspace(0, width - 1, width)
y = np.linspace(0, height - 1, height)
X, Y = np.meshgrid(x, y)


# In[21]:


# Create 3D vertices
Z = height_map * 10  # Scale the height
vertices = np.column_stack((X.flatten(), Y.flatten(), Z.flatten()))


# In[22]:


# Generate random vertex colors
num_vertices = len(vertices)
vertex_colors = np.random.rand(num_vertices, 3)


# In[23]:


# Define faces (e.g., for a grid mesh)
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


# In[24]:


# Create a Trimesh object
mesh = trimesh.Trimesh(vertices, faces, vertex_colors=vertex_colors)


# In[25]:


# Visualize the 3D model
mesh.show()


# In[ ]:




