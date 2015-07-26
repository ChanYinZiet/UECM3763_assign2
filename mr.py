import pylab as p 
import numpy as np

# Setup Parameters Given
alpha = 1;
theta = 0.064;
sigma = 0.27;
R0 = 3 ;
T = 1 ;
n_path = 1000; # total number of simulations  
n = n_partitions = 1000; # number of partitions within the interval 

# Create Brownian Paths 
t = p.linspace (0,T,n+1)[:-1]; 
dt = t/n;
dB = p.randn(n_path,n+1) / p.sqrt(n);
dB[:,0] = 0; 
B=dB.cumsum(axis=1);

# Generate R 
R = p.zeros_like(B);
R[:,0] = R0;
for col in range(n):
    R[:,col+1] = R[:,col] + (theta-R[:,col])*dt + sigma*R[:,col]*dB[:,col+1]

# Plot the 5 (Given) realizations and labelling
R_plot= R[0:5,:-1];
p.plot(t,R_plot.transpose());
p.xlabel('Time, $t$');
p.ylabel('R(t)');
p.title('5 Realizations of the Mean Reversal Process');
p.show();

# Calculate the Expected Value of R(1)
R1 = p.array(R[:,-1]);
E_R1 = np.mean(R1);
print('E[R(1)]   = ' ,E_R1);

# Calculate P[R(1)>2]
x = R1 > 2; # x is the number of R1 > 2
P_x= sum(x)/len(x);  #P_x is probability of x
print('P[R(1)>2] = ' ,P_x);
