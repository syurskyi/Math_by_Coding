# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Import the relevant libraries

# %%
import numpy as np

# %% [markdown]
# ## Transposing matrices

# %%
A = np.array([[5,12,6],[-3,0,14]])
A


# %%
A.T


# %%
B = np.array([[5,3],[-2,4]])
B


# %%
B.T


# %%
C = np.array([[4,-5],[8,12],[-2,-3],[19,0]])
C


# %%
C.T

# %% [markdown]
# ## Transposing scalars

# %%
s = np.array([5])


# %%
s.T

# %% [markdown]
# ## Transposing vectors

# %%
x = np.array([1,2,3])
x


# %%
x.T


# %%
x.shape


# %%
x_reshaped = x.reshape(1,3)
x_reshaped


# %%
x_reshaped.T

