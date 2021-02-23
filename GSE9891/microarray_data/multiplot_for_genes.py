# Multiple plot function
#
# ggplot objects can be passed in ..., or to plotlist (as a list of ggplot objects)
# - cols:   Number of columns in layout
# - layout: A matrix specifying the layout. If present, 'cols' is ignored.
#
# If the layout is something like matrix(c(1,2,3,3), nrow=2, byrow=TRUE),
# then plot 1 will go in the upper left, 2 will go in the upper right, and
# 3 will go all the way across the bottom.
#
multiplot <- function(..., plotlist=NULL, file, cols=1, layout=NULL) {
  library(grid)

  # Make a list from the ... arguments and plotlist
  plots <- c(list(...), plotlist)

  numPlots = length(plots)

  # If layout is NULL, then use 'cols' to determine layout
  if (is.null(layout)) {
    # Make the panel
    # ncol: Number of columns of plots
    # nrow: Number of rows needed, calculated from # of cols
    layout <- matrix(seq(1, cols * ceiling(numPlots/cols)),
                    ncol = cols, nrow = ceiling(numPlots/cols))
  }

 if (numPlots==1) {
    print(plots[[1]])

  } else {
    # Set up the page
    grid.newpage()
    pushViewport(viewport(layout = grid.layout(nrow(layout), ncol(layout))))

    # Make each plot, in the correct location
    for (i in 1:numPlots) {
      # Get the i,j matrix positions of the regions that contain this subplot
      matchidx <- as.data.frame(which(layout == i, arr.ind = TRUE))

      print(plots[[i]], vp = viewport(layout.pos.row = matchidx$row,
                                      layout.pos.col = matchidx$col))
    }
  }
}




# genes = c("CA12.data","DNAJB9.data","ANK1.data","GCLC.data","PPP1R14C.data","SYNPO.data","PGK1.data","SYNPO.data","CHST15.data","DNAJB9.data","DNAJB9.data","GCLC.data","ZDHHC7.data","ECE1.data","NQO1.data","NQO1.data","TMEM30B.data","PDGFC.data","NQO1.data","TSPAN1.data","SERPINE2.data","HES2.data","HES2.data","AFF2.data","HES2.data","PIFO.data","CRABP2.data","MAFB.data","BBS12.data","RPS15.data","RPS12.data","SLC7A2.data","RPL7A.data","MAFB.data","RPL7A.data","RPL12.data","RPL12.data","RPL12.data")
# probes = c("203963_at","202843_at","205390_s_at","1555330_at","226907_at","235914_at","227068_at","202796_at","203066_at","202842_s_at","1554462_a_at","202923_s_at","218606_at","201749_at","201468_s_at","210519_s_at","213285_at","218718_at","201467_s_at","209114_at","212190_at","214521_at","216674_at","206105_at","231928_at","228100_at","202575_at","218559_s_at","229603_at","200819_s_at","213377_x_at","225516_at","224930_x_at","222670_s_at","217740_x_at","200088_x_at","200809_x_at","214271_x_at")

# plots <- list()  # new empty list
# for (i in 1:38) {
#     gene = genes[i]
#     probe = probes[i]
#     df=read.table(gene,sep="\t",header=T)
#     a=ggplot(aes(y = Values, x = probe, fill = Type), data = df) + geom_boxplot()
#     a=a+xlab(gsub(".data","",gene))+ylab("Gene-EXP")+theme(legend.position="none")
#     plots[[i]] <- a  # add each plot into plot list
# }
# b = multiplot(plotlist = plots, cols = 5)

# ggsave(filename = "selected_gene_box_plot.png",plot=b,limitsize = FALSE,dpi=300)



plots <- list()  # new empty list


df=read.table("SLC7A2.data",sep="\t",header=T)
a=ggplot(aes(y = Values, x = factor(Type), fill = factor(Type)), data = subset(df, Probe == "225516_at")) + geom_boxplot() # + geom_dotplot(alpha = 0.8,binaxis='y', stackdir='center', dotsize=0.5)
a=a+xlab("SLC7A2")+ylab("Probe-225516_at-EXP")+theme(legend.position="none")

plots[[1]] <- a

df=read.table("BBS12.data",sep="\t",header=T)
a=ggplot(aes(y = Values, x = factor(Type), fill = factor(Type)), data = subset(df, Probe == "229603_at")) + geom_boxplot() # + geom_dotplot(alpha = 0.8,binaxis='y', stackdir='center', dotsize=0.5)
a=a+xlab("BBS12")+ylab("Probe-229603_at-EXP")+theme(legend.position="none")

plots[[2]] <- a

df=read.table("RPL7A.data",sep="\t",header=T)
a=ggplot(aes(y = Values, x = factor(Type), fill = factor(Type)), data = subset(df, Probe == "217740_x_at")) + geom_boxplot() # + geom_dotplot(alpha = 0.8,binaxis='y', stackdir='center', dotsize=0.5)
a=a+xlab("RPL7A")+ylab("Probe-217740_x_at-EXP")+theme(legend.position="none")

plots[[3]] <- a

df=read.table("RPL7A.data",sep="\t",header=T)
a=ggplot(aes(y = Values, x = factor(Type), fill = factor(Type)), data = subset(df, Probe == "224930_x_at")) + geom_boxplot() # + geom_dotplot(alpha = 0.8,binaxis='y', stackdir='center', dotsize=0.5)
a=a+xlab("RPL7A")+ylab("Probe-224930_x_at-EXP")+theme(legend.position="none")

plots[[4]] <- a

df=read.table("HES2.data",sep="\t",header=T)
a=ggplot(aes(y = Values, x = factor(Type), fill = factor(Type)), data = subset(df, Probe == "231928_at")) + geom_boxplot() # + geom_dotplot(alpha = 0.8,binaxis='y', stackdir='center', dotsize=0.5)
a=a+xlab("HES2")+ylab("Probe-231928_at-EXP")+theme(legend.position="none")

plots[[5]] <- a

df=read.table("RPS12.data",sep="\t",header=T)
a=ggplot(aes(y = Values, x = factor(Type), fill = factor(Type)), data = subset(df, Probe == "213377_x_at")) + geom_boxplot() # + geom_dotplot(alpha = 0.8,binaxis='y', stackdir='center', dotsize=0.5)
a=a+xlab("RPS12")+ylab("Probe-213377_x_at-EXP")+theme(legend.position="none")

plots[[6]] <- a

df=read.table("RPL12.data",sep="\t",header=T)
a=ggplot(aes(y = Values, x = factor(Type), fill = factor(Type)), data = subset(df, Probe == "200088_x_at")) + geom_boxplot() # + geom_dotplot(alpha = 0.8,binaxis='y', stackdir='center', dotsize=0.5)
a=a+xlab("RPL12")+ylab("Probe-200088_x_at-EXP")+theme(legend.position="none")

plots[[7]] <- a

df=read.table("RPL12.data",sep="\t",header=T)
a=ggplot(aes(y = Values, x = factor(Type), fill = factor(Type)), data = subset(df, Probe == "214271_x_at")) + geom_boxplot() # + geom_dotplot(alpha = 0.8,binaxis='y', stackdir='center', dotsize=0.5)
a=a+xlab("RPL12")+ylab("Probe-214271_x_at-EXP")+theme(legend.position="none")

plots[[8]] <- a

df=read.table("RPL12.data",sep="\t",header=T)
a=ggplot(aes(y = Values, x = factor(Type), fill = factor(Type)), data = subset(df, Probe == "200809_x_at")) + geom_boxplot() # + geom_dotplot(alpha = 0.8,binaxis='y', stackdir='center', dotsize=0.5)
a=a+xlab("RPL12")+ylab("Probe-200809_x_at-EXP")+theme(legend.position="none")

plots[[9]] <- a

df=read.table("PIFO.data",sep="\t",header=T)
a=ggplot(aes(y = Values, x = factor(Type), fill = factor(Type)), data = subset(df, Probe == "228100_at")) + geom_boxplot() # + geom_dotplot(alpha = 0.8,binaxis='y', stackdir='center', dotsize=0.5)
a=a+xlab("PIFO")+ylab("Probe-228100_at-EXP")+theme(legend.position="none")

plots[[10]] <- a

df=read.table("RPS15.data",sep="\t",header=T)
a=ggplot(aes(y = Values, x = factor(Type), fill = factor(Type)), data = subset(df, Probe == "200819_s_at")) + geom_boxplot() # + geom_dotplot(alpha = 0.8,binaxis='y', stackdir='center', dotsize=0.5)
a=a+xlab("RPS15")+ylab("Probe-200819_s_at-EXP")+theme(legend.position="none")

plots[[11]] <- a

df=read.table("CRABP2.data",sep="\t",header=T)
a=ggplot(aes(y = Values, x = factor(Type), fill = factor(Type)), data = subset(df, Probe == "202575_at")) + geom_boxplot() # + geom_dotplot(alpha = 0.8,binaxis='y', stackdir='center', dotsize=0.5)
a=a+xlab("CRABP2")+ylab("Probe-202575_at-EXP")+theme(legend.position="none")

plots[[12]] <- a

df=read.table("MAFB.data",sep="\t",header=T)
a=ggplot(aes(y = Values, x = factor(Type), fill = factor(Type)), data = subset(df, Probe == "222670_s_at")) + geom_boxplot() # + geom_dotplot(alpha = 0.8,binaxis='y', stackdir='center', dotsize=0.5)
a=a+xlab("MAFB")+ylab("Probe-222670_s_at-EXP")+theme(legend.position="none")

plots[[13]] <- a

df=read.table("MAFB.data",sep="\t",header=T)
a=ggplot(aes(y = Values, x = factor(Type), fill = factor(Type)), data = subset(df, Probe == "218559_s_at")) + geom_boxplot() # + geom_dotplot(alpha = 0.8,binaxis='y', stackdir='center', dotsize=0.5)
a=a+xlab("MAFB")+ylab("Probe-218559_s_at-EXP")+theme(legend.position="none")

plots[[14]] <- a


# df=read.table("GCLC.data",sep="\t",header=T)
# a=ggplot(aes(y = Values, x = factor(Type), fill = factor(Type)), data = subset(df, Probe == "202923_s_at")) + geom_boxplot() # + geom_dotplot(alpha = 0.8,binaxis='y', stackdir='center', dotsize=0.5)
# a=a+xlab("GCLC")+ylab("Probe-202923_s_at-EXP")+theme(legend.position="none")

# plots[[1]] <- a

# df=read.table("ZDHHC7.data",sep="\t",header=T)
# a=ggplot(aes(y = Values, x = factor(Type), fill = factor(Type)), data = subset(df, Probe == "218606_at")) + geom_boxplot() # + geom_dotplot(alpha = 0.8,binaxis='y', stackdir='center', dotsize=0.5)
# a=a+xlab("ZDHHC7")+ylab("Probe-218606_at-EXP")+theme(legend.position="none")

# plots[[2]] <- a

# df=read.table("ECE1.data",sep="\t",header=T)
# a=ggplot(aes(y = Values, x = factor(Type), fill = factor(Type)), data = subset(df, Probe == "201749_at")) + geom_boxplot() # + geom_dotplot(alpha = 0.8,binaxis='y', stackdir='center', dotsize=0.5)
# a=a+xlab("ECE1")+ylab("Probe-201749_at-EXP")+theme(legend.position="none")

# plots[[3]] <- a

# df=read.table("TMEM30B.data",sep="\t",header=T)
# a=ggplot(aes(y = Values, x = factor(Type), fill = factor(Type)), data = subset(df, Probe == "213285_at")) + geom_boxplot() # + geom_dotplot(alpha = 0.8,binaxis='y', stackdir='center', dotsize=0.5)
# a=a+xlab("TMEM30B")+ylab("Probe-213285_at-EXP")+theme(legend.position="none")

# plots[[4]] <- a

# df=read.table("PDGFC.data",sep="\t",header=T)
# a=ggplot(aes(y = Values, x = factor(Type), fill = factor(Type)), data = subset(df, Probe == "218718_at")) + geom_boxplot() # + geom_dotplot(alpha = 0.8,binaxis='y', stackdir='center', dotsize=0.5)
# a=a+xlab("PDGFC")+ylab("Probe-218718_at-EXP")+theme(legend.position="none")

# plots[[5]] <- a

# df=read.table("NQO1.data",sep="\t",header=T)
# a=ggplot(aes(y = Values, x = factor(Type), fill = factor(Type)), data = subset(df, Probe == "201467_s_at")) + geom_boxplot() # + geom_dotplot(alpha = 0.8,binaxis='y', stackdir='center', dotsize=0.5)
# a=a+xlab("NQO1")+ylab("Probe-201467_s_at-EXP")+theme(legend.position="none")

# plots[[6]] <- a

# df=read.table("TSPAN1.data",sep="\t",header=T)
# a=ggplot(aes(y = Values, x = factor(Type), fill = factor(Type)), data = subset(df, Probe == "209114_at")) + geom_boxplot() # + geom_dotplot(alpha = 0.8,binaxis='y', stackdir='center', dotsize=0.5)
# a=a+xlab("TSPAN1")+ylab("Probe-209114_at-EXP")+theme(legend.position="none")

# plots[[7]] <- a

# df=read.table("SERPINE2.data",sep="\t",header=T)
# a=ggplot(aes(y = Values, x = factor(Type), fill = factor(Type)), data = subset(df, Probe == "212190_at")) + geom_boxplot() # + geom_dotplot(alpha = 0.8,binaxis='y', stackdir='center', dotsize=0.5)
# a=a+xlab("SERPINE2")+ylab("Probe-212190_at-EXP")+theme(legend.position="none")

# plots[[8]] <- a

b = multiplot(plotlist = plots, cols = 5)

ggsave(filename = "PSO2_PSO3_selected_gene_box_plot.png",plot=b,limitsize = FALSE,dpi=300)

