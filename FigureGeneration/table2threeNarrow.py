import numpy as np
import matplotlib.pyplot as plt
import pandas



print('Loading orig...')

#5ppm search
#data = pandas.read_csv(r"C:\Users\stepa\Data\PaperData\JurkatTrypsin\Calibrated\exact5ppm\Task1-SearchTask\aggregatePSMs_5ppmAroundZero.psmtsv", sep='\t')

#2.5 da search
#data = pandas.read_csv(r"C:\Users\stepa\Data\PaperData\JurkatTrypsin\Calibrated\twoPointFiveAroundZero\Task1-SearchTask\aggregatePSMs_2.5daltonsAroundZero.psmtsv", sep='\t')

#notch search
data = pandas.read_csv(r"C:\Users\stepa\Data\PaperData\JurkatTrypsin\Calibrated\2mm5ppm\Task1-SearchTask\aggregatePSMs_1mm.psmtsv", sep='\t')

print('Loading final...')

dataFinal = pandas.read_csv(r"C:\Users\stepa\Data\PaperData\JurkatTrypsin\Calibrated\2017-10-20-16-43-18-final\Task1-SearchTask\aggregatePSMs_1mm.psmtsv", sep='\t')

print('Starting loop...')


with open('workfile.tsv', 'w') as f:
  for index, row in data.iterrows():
    final = dataFinal.loc[(dataFinal['File Name'] == row['File Name']) & (dataFinal['Scan Number'] == row['Scan Number']) & (dataFinal['Precursor MZ'] == row['Precursor MZ'])]
    initScore = row['Score']
    if(len(final['Score']) == 0):
      continue
    finalScore = final['Score'].iat[0]
    if(int(initScore)<int(finalScore) and 'Phospho' not in row['Full Sequence'] and final['Notch'].iat[0] =="0"):
      if(row['QValue Notch'] >= 0.01):
        break
      toWrite = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(index, row['QValue Notch'], finalScore, initScore, final['Full Sequence'].iat[0].split(" or ")[0], row['Full Sequence'].split(" or ")[0], final['Peptide Monoisotopic Mass'].iat[0], row['Peptide Monoisotopic Mass'])
      print(toWrite)
      f.write(toWrite)
      f.write('\n')





















data = pandas.read_csv(r"C:\Users\stepa\Data\PaperData\JurkatTrypsin\Calibrated\exact5ppm\Task1-SearchTask\aggregatePSMs_5ppmAroundZero.psmtsv", sep='\t')

data['Mass Diff (Da)'] = pandas.to_numeric(data['Mass Diff (Da)'], errors='coerce')
data_sorted = data.sort_values(['Mass Diff (Da)'], ascending=True)



massDiffs=data_sorted['Mass Diff (Da)'].values


B=data_sorted['Decoy/Contaminant/Target'].values
C=data_sorted['QValue Notch'].values

len1 = len(massDiffs[C<0.01])

data = pandas.read_csv(r"C:\Users\stepa\Data\PaperData\JurkatTrypsin\Calibrated\twoPointFiveAroundZero\Task1-SearchTask\aggregatePSMs_2.5daltonsAroundZero.psmtsv", sep='\t')

data['Mass Diff (Da)'] = pandas.to_numeric(data['Mass Diff (Da)'], errors='coerce')
data_sorted = data.sort_values(['Mass Diff (Da)'], ascending=True)
massDiffs=data_sorted['Mass Diff (Da)'].values


B=data_sorted['Decoy/Contaminant/Target'].values
C=data_sorted['QValue Notch'].values

len2 = len(massDiffs[C<0.01])

data = pandas.read_csv(r"C:\Users\stepa\Data\PaperData\JurkatTrypsin\Calibrated\2mm5ppm\Task1-SearchTask\aggregatePSMs_1mm.psmtsv", sep='\t')


data['Mass Diff (Da)'] = pandas.to_numeric(data['Mass Diff (Da)'], errors='coerce')
data_sorted = data.sort_values(['Mass Diff (Da)'], ascending=True)
massDiffs=data_sorted['Mass Diff (Da)'].values


B=data_sorted['Decoy/Contaminant/Target'].values
C=data_sorted['QValue Notch'].values


len3 = len(massDiffs[C<0.01])
print(len1) 
print(len2)
print(len3)
