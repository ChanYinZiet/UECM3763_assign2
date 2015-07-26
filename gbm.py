import pylab as p
import numpy as np

# Setup Parameters Given
mu = 0.1;  
sigma = 0.26; 
S0 = 39;
T = 3;
n_path = 1000; #Number of simulations
n = n_partitions = 1000; # Number of partitions within the interval 

# Create Brownian Paths
t = p.linspace (0,T,n+1);
dB = p.randn(n_path,n+1) / p.sqrt(n);
dB[:,0] = 0; 
B = dB.cumsum(axis=1);

# Calculate Stock Prices
nu = mu - sigma*sigma/2;
S = p.zeros_like(B);
S[:,0] = S0;
S[:,1:] = S0*p.exp(nu*t[1:]+sigma*B[:,1:]);

# Plot the 5 (Given) Realizations and Labelling
S_plot= S[0:5];
p.plot(t,S_plot.transpose());
p.xlabel('Time,$t$');
p.ylabel('Stock Prices,$RM$');
p.title('Title: 5 realizations of the GBM');
p.show();

# Calculate the Expected Value and Variance of S(3)
S3 = p.array(S[:,-1]);
Expected_S3 = np.mean(S3);
print('E[S(3)]           = ',Expected_S3);
Variance_S3 = np.var(S3);
print('Var[S(3)]         = ',Variance_S3);

# Calculate P[S(3)>39]
x = S3 > 39; # x is the number of S3 > 39
P_x = sum(x) / len(x); #P_x is probability of x
print('P[S(3)>39]        = ',P_x);

# Calculate E[S(3)| S(3)>39]
E_value= sum(S3*x) / sum(x);
print('E[S(3)| S(3)>39]  = ' ,E_value);
