
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"MS_expression.tsv", sep='\t', header=0)
data = pd.DataFrame(data)
data = data.set_index('SYMBOL')


data_ms_gene1 = data.loc[('IGHG1'),data.columns.str.startswith('ms')]
data_ms_gene1 = pd.DataFrame(data_ms_gene1)
data_control_gene1 = data.loc[('IGHG1'),data.columns.str.startswith('control')]
data_control_gene1 = pd.DataFrame(data_control_gene1)


data_ms_gene1['Control_IGHG1'] = data_ms_gene1
data_control_gene1['Patients_IGHG1'] = data_control_gene1


data_ms_gene2 = data.loc[('MMRN1'),data.columns.str.startswith('ms')]
data_ms_gene2 = pd.DataFrame(data_ms_gene2)
data_control_gene2 = data.loc[('MMRN1'),data.columns.str.startswith('control')]
data_control_gene2 = pd.DataFrame(data_control_gene2)
data_ms_gene2['Control_MMRN1'] = data_ms_gene2
data_control_gene2['Patients_MMRN1'] = data_control_gene2


data_gene_1 = pd.concat([data_ms_gene1,data_control_gene1],ignore_index=True, sort=False)

data_gene_2 = pd.concat([data_ms_gene2,data_control_gene2],ignore_index=True, sort=False)


data_gene_1[["Control_IGHG1","Patients_IGHG1"]].plot.bar()
plt.title("Comparion of IGHG1 gene expression")
plt.ylabel("Gene Expression")
plt.xlabel("Samples")

data_gene_2[["Control_MMRN1","Patients_MMRN1"]].plot.bar()
plt.title("Comparion of MMRN1 gene expression")
plt.ylabel("Gene Expression")
plt.xlabel("Samples")
plt.show()










