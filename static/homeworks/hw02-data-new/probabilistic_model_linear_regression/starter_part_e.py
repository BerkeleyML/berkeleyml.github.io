import numpy as np
import matplotlib.pyplot as plt

sample_size = [5,25,125,625]
plt.figure(figsize=[12, 10])             
for k in range(4):
    n = sample_size[k]
    
    # generate data
    # np.linspace, np.random.normal and np.random.uniform might be useful functions

    
    likelihood = np.ones(N) # likelihood as a function of w

    for i1 in range(N):
        # compute likelihood

    likelihood /= sum(likelihood) # normalize the likelihood
    
    plt.figure()
    # plotting likelihood for different n
    plt.plot(W, likelihood)
    plt.xlabel('w', fontsize=10)
    plt.title(['n=' + str(n)], fontsize=14)

plt.show()