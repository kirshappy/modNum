  # General settings
  
  library("ggplot2")
  library("scales")
  library("readxl")
  library("reshape2")
  library("hrbrthemes")

setwd("/home/myriam/modNum/result")

#Data to be used in plot for Mallet Topic Modelling 20
#Create one column with all cluster to replace matrix
#Still have cluster weight information per document and year
#Remove all cluster weight value below 0.10 to avoid noise on plot
mallet20<-read_excel("allengr3Commission_compostion.xls")
longmallet20<-melt(mallet20,id.vars = c("Id","Year"),variable.name = "Clusters",value.name = "Cluster_Weight")
lmallet20NoZero<-subset(longmallet20,Cluster_Weight>=0.10)

gmallet20<-ggplot(lmallet20NoZero,aes(x=Clusters,y=Id,color=Cluster_Weight))+geom_jitter(size=1)+scale_colour_gradient2(low="white",mid="yellow",high="green",midpoint =0.5,limit=c(0,1))
gmallet200<-gmallet20 +ggtitle("Document distribution per cluster")
#gmallet200
gmallet20_fgrid<-gmallet20+facet_grid(Year ~., scales = "free_y")+ggtitle("Document distribution per cluster with a special attention to year")
#gmallet20_fgrid

#Data to be used in plot for Mallet Topic Modelling Optimize20
#Create one column with all cluster to replace matrix
#Still have cluster weight information per document and year
#Remove all cluster weight value below 0.10 to avoid noise on plot

malletOpt20<-read_excel("allengr3CommissionOpt20_composition.xls")
longmalletOpt20<-melt(malletOpt20,id.vars = c("Id","Year"),variable.name = "Clusters",value.name = "Cluster_Weight")
lmalletOpt20NoZero<-subset(longmalletOpt20,Cluster_Weight>=0.10)
#head(lmalletOpt20NoZero)
#summary(lmalletOpt20NoZero)
gmalletOpt20<-ggplot(lmalletOpt20NoZero,aes(x=Clusters,y=Id,color=Cluster_Weight))+geom_jitter(size=1)+scale_colour_gradient2(low="white",mid="yellow",high="green",midpoint =0.5,limit=c(0,1))
gmalletOpt200<-gmalletOpt20 +ggtitle("Optimize Document distribution per cluster")
#gmalletOpt200
gmalletOpt20_fgrid<-gmallet20+facet_grid(Year ~., scales = "free_y")+ggtitle("Optimize Document distribution per cluster with a special attention to year")
gmalletOpt20_fgrid
