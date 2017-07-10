import numpy as np
import matplotlib.pyplot as plt
import pandas

height = 3
width = 7
plt.figure(figsize=(width, height))


offset = 200

#data = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-05-05-18-28-01\Task2Calibrate\2017-07-06-17-29-30\Task1Search\aggregatePSMs_OpenSearch.psmtsv", sep='\t')
data = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Jurkat\2017-05-05-18-29-43\Task2Calibrate\2017-07-07-13-19-26\Task1Search\aggregatePSMs_OpenSearch.psmtsv", sep='\t')


data_sorted = data.sort_values(['Mass Diff (Da)'], ascending=True)

A=data_sorted['Mass Diff (Da)'].values
B=data_sorted['Decoy/Contaminant/Target'].values
C=data_sorted['QValue Notch'].values

print(A[0])
print(A[-1])

AhighConf = A[C<0.01]
BhighConf = B[C<0.01]

print(AhighConf[0])
print(AhighConf[-1])

print(BhighConf[0])
print(BhighConf[1])
print(BhighConf[2])
print(BhighConf[3])
print(BhighConf[4])

totalCount = len(AhighConf)
   
forward = [0]
forwardDiv = []
forwardInd= []
for i in range(totalCount):
    forward.append(forward[-1]+1 if BhighConf[i]=='D' else forward[-1])
    forwardDiv.append(forward[-1]/(i+1))
    forwardInd.append(AhighConf[i])

print(forwardDiv[0])
print(forwardDiv[1])
print(forwardDiv[2])
print(forwardDiv[3])
print(forwardDiv[4])
print(forwardDiv[5])
print(forwardDiv[6])
print(forwardDiv[7])
print(forwardDiv[8])

ok = plt.subplot(121)

plt.scatter(forwardInd[offset:totalCount-offset:100], forwardDiv[offset:totalCount-offset:100])
plt.xscale('symlog')
plt.xticks([-1e4, -1e3, -1e2, -1e1, 0,1e1, 1e2, 1e3, 1e4])
plt.ylabel("FDR")
plt.xlabel("Mass Diff")
plt.title("Limit From Above")


backward = [0]
backwardDiv= []
backwardInd= []
for i in range(totalCount-1,-1,-1):
    backward.append(backward[-1]+1 if BhighConf[i]=='D' else backward[-1])
    backwardDiv.append(backward[-1]/(totalCount - i))
    backwardInd.append(AhighConf[i])

print("len(backwardInd)", len(backwardInd))
print("len(backwardDiv)", len(backwardDiv))
    
print(backwardDiv[0])
print(backwardDiv[1])
print(backwardDiv[2])
print(backwardDiv[3])
print(backwardDiv[4])
print(backwardDiv[5])
print(backwardDiv[6])
print(backwardDiv[7])


plt.tick_params(axis='both', which='major', labelsize=8)

ok = plt.subplot(122)

plt.scatter(backwardInd[offset:totalCount-offset:100], backwardDiv[offset:totalCount-offset:100])

plt.xscale('symlog')
plt.xticks([-1e4, -1e3, -1e2, -1e1, 0,1e1, 1e2, 1e3, 1e4])
plt.ylabel("FDR")
plt.xlabel("Mass Diff")
plt.title("Limit From Below")

plt.tick_params(axis='both', which='major', labelsize=8)

plt.tight_layout() 
 

plt.savefig('fig4-limitsOnOpenSearch.eps', format='eps', dpi=1200)
plt.savefig('fig4-limitsOnOpenSearch.png', format='png', dpi=1200)


plt.show()
