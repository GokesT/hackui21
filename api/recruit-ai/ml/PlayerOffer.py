# imports and fixed params
import numpy as np
import pandas as pd
import torch
from torchvision import transforms, utils
from torch import nn, optim
from torch.utils.data.sampler import SubsetRandomSampler
from torch.utils.data import TensorDataset, DataLoader
from torch.autograd import Variable

import tqdm
import matplotlib.pyplot as plt
from least_squares import regress

# Load and concatenate college data
college_data = pd.read_csv("data/players2014.csv").to_numpy()
for i in range(15, 21):
    college_data = np.append(college_data, pd.read_csv(
        "data/players20%d.csv" % i).to_numpy(), axis=0)
college_data = college_data[college_data[:, 1].argsort()]
print(college_data.shape)

# Load in high school data
hs_data = pd.read_csv("data/hs_data_clean.csv").to_numpy()
print(hs_data.shape)

# Do some stuff
names = college_data[:,1]
hs_indices = []
made_it_boolean = []
for i in range(hs_data.shape[0]):
    index = np.searchsorted(names, hs_data[i][0])
    if index < len(names) and names[index] == hs_data[i][0]:
        made_it_boolean.append(1)
        hs_indices.append(i)
    else:
        made_it_boolean.append(0)

hs_indices = np.array(hs_indices)
hs_data_made_it = hs_data[hs_indices,:]
hs_data_made_it = hs_data_made_it[hs_data_made_it[:, 0].argsort()]

X_data = np.array(hs_data_made_it[:,2:-1]).astype(np.float)
print(X_data.shape)

Y_data = np.array(college_data_made_it[:,5]).astype(np.float)
Y_data = np.array([Y_data]).T
print(Y_data.shape)

data = np.append(X_data, Y_data, axis=1)


print(hs_data_made_it.shape)

# Set the batch size and validation and test split
batch_size = 40
vt_split = .3

shuffle_dataset = True

# Read from csv and turn into numpy array
data = pd.read_csv('data/poolcoll2.csv')
data = data.to_numpy()
data = data[:, 1:].copy()
data = np.delete(data, 1, 1)

print(data.shape)