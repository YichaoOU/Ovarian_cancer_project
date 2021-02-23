
import sys
selected_gene_probe_file = sys.argv[1]
gene_matrix_file = sys.argv[2]
sample_id_class_file = sys.argv[3]
# probe_list = []
probe_dict = {}
my_sample_id_dict = {}
def gene_probe_dict(file):
	my_dict = {}
	with open(file) as f:
		for line in f:
			# print line
			line = line.strip().split()
			# print line
			gene = line[0]
			probe = line[1]
			# probe_list.append(probe)
			probe_dict[probe] = []
			if my_dict.has_key(gene):
				my_dict[gene].append(probe)
			else:
				my_dict[gene] = []
				my_dict[gene].append(probe)
	return my_dict

def sample_id_class(file):
	lines = open(file).readlines()[1:]
	for line in lines:
		line = line.strip().split(",")
		id = line[0]
		# print id
		Class = line[1:]
		my_sample_id_dict[id]=Class
	return 1


my_dict = gene_probe_dict(selected_gene_probe_file)
sample_id_class(sample_id_class_file)
my_sample_id_list = []
with open(gene_matrix_file) as f:
	for line in f:
		line = line.strip().split()
		if len(line) <= 1:
			continue
		if line[0] == "!Sample_title":
			for i in range(1,len(line)):
				sample_id = line[i].replace('"','')
				my_sample_id_list.append(sample_id)

		# print line
		try:
			probe_id = line[0].replace('"','')
			gene_exp = line[1:]
		except:
			continue
		if probe_dict.has_key(probe_id):
			probe_dict[probe_id] = gene_exp




for gene in my_dict:
	out = open(gene+".data","wb")
	print >>out,"Probe	Values	Primary.Site	Type	Subtype	StageCode	Consolidated.Grade"
	for p in my_dict[gene]:
		for i in range(len(probe_dict[p])):
			value = probe_dict[p][i]
			sample_id = my_sample_id_list[i]
			desc = my_sample_id_dict[sample_id]
			out_array = [p,value] + desc
			print >>out,"\t".join(out_array)
	out.close()





























