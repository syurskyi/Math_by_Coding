# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Import the relevant libraries

# %%
import numpy as np

# %% [markdown]
# ## Addition

# %%
m1 = np.array([[5,12,6],[-3,0,14]])
m1


# %%
m2 = np.array([[9,8,7],[1,3,-5]])
m2


# %%
m1 + m2

# %% [markdown]
# ## Difference
# %% [markdown]
# ### Example 1

# %%
m3 = np.array([[5,3],[-2,4]])
m4 = np.array([[7,-5],[3,8]])


# %%
m3


# %%
m4


# %%
m3 - m4

# %% [markdown]
# ### Example 2

# %%
m5 = np.array([[22.33,-4.73],[-203.14,1200.02],[4.22,234.1]])
m5


# %%
m6 = np.array([[131.13,448.29],[-340.21,1.06],[30.41,424.99]])
m6


# %%
m5 - m6

# %% [markdown]
# ## Adding vectors together

# %%
v1 = np.array([1,2,3,4,5])
v2 = np.array([5,4,3,2,1])


# %%
v1 + v2


# %%
v1 - v2

