import numpy as np

#data create
data=np.random.randint(0,100,size=(100,3))

#normalize feature
normalize=(data - np.min(data,axis=0) / np.max(data, axis=0) - np.min(data,axis=0))

#splitting 
train=normalize[:70]
test=normalize[70:]

# print("data",data)
print("\n\nNormalized data:", normalize)

print("\n\nTrain shape:", train)
print("\n\nTest shape:", test)
