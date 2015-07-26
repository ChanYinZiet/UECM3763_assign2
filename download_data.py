from pandas.io.data import DataReader as DR
from datetime import datetime as dt
import pylab as p
import numpy as np

# Download Stock Data from Yahoo Finance as @ 1 July 2011 - 30 June 2014 
start = dt(2011,7, 1);
end = dt(2014, 6,30);
HL_data = DR("5819.KL", 'yahoo', start, end);
# 5819 is the Stock Code of Hong Leong Bank

#Put HL_data into array, and use only the last price
HL_array = p.array(HL_data);
HL_last_price = HL_array[:,-1];
Total_HLLP = HL_last_price.cumsum();

#Calculate 5-days Moving Average
n=5;
matrix = np.zeros((2,(len(Total_HLLP)-n+1)));
matrix[0,:] = Total_HLLP[(n-1):];
matrix[1,1:] = Total_HLLP[:-(n)];
mvg_avg = (matrix[0] - matrix[1]) / n;

#Plot the 5-days Moving Average and Labelling
p.plot(mvg_avg);
p.xlabel('Days'); 
p.ylabel('5-days Average');
p.title('5-days Moving Average of Hong Leong Bank \n [1 July 2011 - 30 June 2014] ' );
p.show();   

# Downlaod and Combining KLSE data with HL_data within the same period
Combine_data = ["5819.KL","^KLSE"]; 
HL_KLSE_data = DR(Combine_data,'yahoo',start,end)['Adj Close'];
#Adj Close is the Adjusted Close Price

# Put HL_KLSE_data into array
HL_KLSE_array = p.array(HL_KLSE_data );

# Calcualte Correlation for both Hong Leong Bank and KLSE
Correlation = HL_KLSE_data.corr();
print('Correlation of Hong Leong Bank and FTSEKLCI \n',Correlation);