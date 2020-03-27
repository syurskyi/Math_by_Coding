# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Import the relevant libraries

# %%
import numpy as np

# %% [markdown]
# ## Addition
# %% [markdown]
# ### Addition of scalars

# %%
5 + 5


# %%
10 - 4

# %% [markdown]
# ### Addition of matrices

# %%
m1 = np.array([[5,12,6],[-3,0,14]])
m1


# %%
m3 = np.array([[5,3],[-2,4]])
m3


# %%
m1 + m3

# %% [markdown]
# ### Addition of vectors

# %%
v1 = np.array([1,2,3,4,5])
v1


# %%
v3 = np.array([1,2,3])
v3


# %%
v1+v3

# %% [markdown]
# ### Exceptions (addition with a scalar)

# %%
m1


# %%
m1 + 1


# %%
v1


# %%
v1 + 1


# %%
m1 + np.array([1])


# %%
v1 + np.array([1])

