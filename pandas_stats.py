import pandas as pd
import statistics

data = pd.read_csv("MS_expression.tsv", sep='\t', header=0)
data.head()
data = pd.DataFrame(data) #reading csv file into pandas dataframe


data_patient=data.loc[:,data.columns.str.startswith('ms')]
data_control=data.loc[:,data.columns.str.startswith('control')] 

#calculating the mean and std for ms=patient & control
data_patient_mean = data_patient.mean(axis=1) 
data_patient_std = data_patient.std(axis=1)

data_control_mean = data_control.mean(axis=1) 
data_control_std = data_control.std(axis=1)

#Adding new columns to the dataframe
data['mean_control']=data_control_mean 
data['std_control']=data_control_std
data['mean_patient']=data_patient_mean
data['std_patient']=data_patient_std
data.head() #checking if the new columns are added

new_data = data[['SYMBOL','mean_patient','std_patient','mean_control','std_control']].copy() 
new_data.rename(columns={new_data.columns[0]:"GENE ID"},inplace=True) 
                
new_data.to_csv('gene_exp.txt', sep='\t') 

