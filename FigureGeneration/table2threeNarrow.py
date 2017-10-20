import numpy as np
import matplotlib.pyplot as plt
import pandas

data = pandas.read_csv(r"C:\Users\stepa\Data\PaperData\JurkatTrypsin\Calibrated\twoPointFiveAroundZero\Task1-SearchTask\aggregatePSMs_2.5daltonsAroundZero.psmtsv", sep='\t')

data['Mass Diff (Da)'] = pandas.to_numeric(data['Mass Diff (Da)'], errors='coerce')
data_sorted = data.sort_values(['Mass Diff (Da)'], ascending=True)
massDiffs=data_sorted['Mass Diff (Da)'].values


B=data_sorted['Decoy/Contaminant/Target'].values
C=data_sorted['QValue Notch'].values

len1 = len(massDiffs[C<0.01])

data = pandas.read_csv(r"C:\Users\stepa\Data\PaperData\JurkatTrypsin\Calibrated\2mm5ppm\Task1-SearchTask\aggregatePSMs_1mm.psmtsv", sep='\t')


data['Mass Diff (Da)'] = pandas.to_numeric(data['Mass Diff (Da)'], errors='coerce')
data_sorted = data.sort_values(['Mass Diff (Da)'], ascending=True)
massDiffs=data_sorted['Mass Diff (Da)'].values


B=data_sorted['Decoy/Contaminant/Target'].values
C=data_sorted['QValue Notch'].values


len2 = len(massDiffs[C<0.01])

data = pandas.read_csv(r"C:\Users\stepa\Data\PaperData\JurkatTrypsin\Calibrated\exact5ppm\Task1-SearchTask\aggregatePSMs_5ppmAroundZero.psmtsv", sep='\t')




data['Mass Diff (Da)'] = pandas.to_numeric(data['Mass Diff (Da)'], errors='coerce')
data_sorted = data.sort_values(['Mass Diff (Da)'], ascending=True)
massDiffs=data_sorted['Mass Diff (Da)'].values


B=data_sorted['Decoy/Contaminant/Target'].values
C=data_sorted['QValue Notch'].values

len3 = len(massDiffs[C<0.01])

print(len3)
print(len1) 
print(len2)
