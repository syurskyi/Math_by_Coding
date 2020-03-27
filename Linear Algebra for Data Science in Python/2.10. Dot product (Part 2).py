# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ## Import the relevant libraries

# %%
import numpy as np

# %% [markdown]
# ## Vector * Vector

# %%
x = np.array([2,8,-4])
y = np.array([1,-7,3])


# %%
np.dot(x,y)


# %%
u = np.array([0,2,5,8])
v = np.array([20,3,4,-1])


# %%
np.dot(u,v)

# %% [markdown]
# ## Scalar * Scalar

# %%
np.dot(5,6)


# %%
np.dot(10,-2)

# %% [markdown]
# ## Scalar * Vector

# %%
5*x

# %% [markdown]
# ## Scalar * Matrix

# %%
A = np.array([[5,12,6],[-3,0,14]])
A


# %%
3*A

# %% [markdown]
# ## Matrix * Matrix
# %% [markdown]
# ### Example 1

# %%
B = np.array([[2,-1],[8,0],[3,0]])
B


# %%
np.dot(A,B)

# %% [markdown]
# ### Example 2

# %%
C = np.array([[-12,5,-5,1,6],[6,-2,0,0,-3],[10,2,0,8,0],[9,-4,8,3,-6]])
C


# %%
D = np.array([[6,-1],[8,-4],[2,-2],[7,4],[-6,-9]])
D


# %%
np.dot(C,D)

