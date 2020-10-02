import pickle
import numpy as np
import pickle

data_dict = {
    "volts" : np.random.random(10),
    "currents" : np.random.random(10)
}

with open("data_pick.pkl", "wb") as data_pickle:
    pickle.dump(data_dict, data_pickle)

with open("data_pick.pkl", "rb") as data_pickle:
    new = pickle.load(data_pickle)

print(new)