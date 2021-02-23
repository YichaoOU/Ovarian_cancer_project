import numpy as np
from scipy import stats
# selected_genes = ["SLC7A2","BBS12","RPL7A","HES2","RPS12","RPL12","PIFO","RPS15","AFF2","CRABP2","MAFB"]
selected_genes = ["CHST15","TSPAN1","PPP1R14C","ECE1","CLIC1","CA12","TMEM30B","ENPP4","ANK1","SYNPO","GCLC","NQO1","PGK1","PDGFC","SERPINE2","ZDHHC7","DNAJB9"]
out = open("PSO2_PSO3_selected_gene_expression_table_in_GSE9891.csv","wb")
for gene in selected_genes:
	lines = open(gene+".data").readlines()[1:]
	my_dict  = {}
	for line in lines:
		line = line.strip().split()
		key = line[0]
		status = line[3]
		if my_dict.has_key(key):
			my_dict[key][status].append(float(line[1]))
		else:
			my_dict[key] = {}
			my_dict[key]["LMP"] = []
			my_dict[key]["Malignant"] = []
			my_dict[key][status].append(float(line[1]))
	for key in my_dict:
		LMP_median = np.median(my_dict[key]["LMP"])
		Malignant_median = np.median(my_dict[key]["Malignant"])
		LMP_std = np.std(my_dict[key]["LMP"])
		Malignant_std = np.std(my_dict[key]["Malignant"])
		LMP_mean = np.mean(my_dict[key]["LMP"])
		Malignant_mean = np.mean(my_dict[key]["Malignant"])
		fc = LMP_median/Malignant_median
		p_value = stats.ttest_ind(my_dict[key]["LMP"], my_dict[key]["Malignant"], equal_var = False)[1]
		print >>out,",".join([gene,key,str(LMP_median),str(LMP_std),str(Malignant_median),str(Malignant_std),str(fc),str(p_value)])		









