import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt

N_data = 10
dim = 2


x = np.random.random(N_data*dim)
x_reshaped = x.reshape(N_data,dim)
X = (x_reshaped-0.5)**3


y = np.random.random(N_data*dim)
y_reshaped = y.reshape(N_data,dim)
Y = (y_reshaped-0.5)**3+0.15


X =  np.concatenate((X,Y))
out = open("output.txt", "w")
for n in range(N_data) :
    s = ""
    for i in range(dim) :
        s = s + str(X[n,i]) + "\t"
    s = s + "\n"
    out.writelines(s)


plt.scatter(X[:,0],X[:,1],marker='o',s=10,color='r')
