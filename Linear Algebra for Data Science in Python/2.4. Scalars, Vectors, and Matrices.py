# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Import the relevant libraries

# %%
import numpy as np

# %% [markdown]
# # Declaring scalars, vectors, and matrices
# %% [markdown]
# ## Scalars

# %%
s = 5


# %%
s

# %% [markdown]
# ## Vectors

# %%
v = np.array([5,-2,4])


# %%
v

# %% [markdown]
# ## Matrices

# %%
m = np.array([[5,12,6],[-3,0,14]])


# %%
m

# %% [markdown]
# ## Data types

# %%
type(s)


# %%
type(v)


# %%
type(m)


# %%
s_array = np.array(5)


# %%
type(s_array)

# %% [markdown]
# ## Data shapes

# %%
m.shape


# %%
v.shape


# %%
s.shape


# %%
s_array.shape

# %% [markdown]
# ## Creating a column vector

# %%
v.reshape(1,3)


# %%
v.reshape(3,1)


# %%
m+s


# %%
m+s_array


# %%
v+s


# %%
v


# %%
v+s_array


# %%
m+v


# %%


