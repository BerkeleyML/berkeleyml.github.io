import numpy as np
import matplotlib.pyplot as plt

sample_size = [5,25,125]
for k in range(4):
    n = sample_size[k]

    # generate data 
    # np.linspace, np.random.normal and np.random.uniform might be useful functions
    
    # compute likelihood
    N = 1001 
    # W0s = 
    # W1s = 
    likelihood = np.ones([N,N]) # likelihood as a function of w_1 and w_0
                        
    for i1 in range(N):
        # w_1 = W1s[i1]
        for i2 in range(N):
            # w_2 = W2s[i2]
            for i in range(n):
                # compute the likelihood here

    # plotting the likelihood
    plt.figure()                          
    # for 2D likelihood using imshow
    plt.imshow(likelihood, cmap='hot', aspect='auto',extent=[0,4,0,4])
    plt.xlabel('w0')
    plt.ylabel('w1')
    plt.show()
    print(n)