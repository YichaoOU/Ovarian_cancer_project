library(ggplot2)
df=read.table("MAFB.data",sep="\t",header=T)
probe_names=unique(df$Probe)
a=ggplot(aes(y = Values, x = "222670_s_at", fill = Type), data = df) + geom_boxplot()
a=a+xlab("Probes of gene MAFB")+ylab("Gene Expression")
print (a)
# ggsave("MAFB.png",a)




















