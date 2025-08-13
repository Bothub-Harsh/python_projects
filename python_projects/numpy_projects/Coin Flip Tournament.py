import numpy as np

"""1=head, 2=tail, 3=middle"""
stuff=np.array([1,2,3])
coin1_store=[]
coin2_store=[]
coin3_store=[]
  
coin1=np.random.choice(stuff, size=100)
coin1_store.append(coin1)
coin2=np.random.choice(stuff, size=100)
coin2_store.append(coin2)
coin3=np.random.choice(stuff, size=100)
coin3_store.append(coin3)

#convert to np array
coin1_store=np.array(coin1_store)
coin2_store=np.array(coin2_store)
coin3_store=np.array(coin3_store)

total=coin1_store + coin2_store + coin3_store
print(total)

# probabilty
for i in range(3,10):
  count=np.count_nonzero(total==i)
  probablity=(count/len(total)) * 100
  print(f"\ncoin 1 {i}: {count} times probablity:{probablity:.2f}")
  print(f"coin 2 {i}: {count} times probablity:{probablity:.2f}")
  print(f"coin 3 {i}: {count} times probablity:{probablity:.2f}")
    