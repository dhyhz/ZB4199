matrix_df = read.csv("C:/Users/DHYHZ/Desktop/nbtrial/matrix_df.csv", row.names = 1)
names(matrix_df)
rownames(matrix_df)
names(matrix_df)[1] = "2-Aminoethanol"
m = data.matrix(matrix_df)
dim(m)
mt =t(m)
dim(mt)
combi = mt %*% m
dim(combi)

ingredients = row.names(combi)
ingredients
names(combi)
apply(combi, 2, mean)
apply(combi, 2, var)
pr.out=princomp(combi, cor = FALSE, scores = TRUE, covmat = NULL)
names(pr.out)
pr.out$center
pr.out$scale
pr.out$n.obs
pr.out$loadings
pr.out$sdev
pr.out$scores
pr.out$call
dim(pr.out$x)
plot(pr.out, scale=0)
biplot(pr.out, scale=0, expand=5, xlim=c(-0.50, 0.3), ylim=c(-0.7, 0.5))
biplot(pr.out, choices = 2:3, scale=1)
biplot(pr.out, scale=0, expand=5, xlim=c(-0.50, 0.3), ylim=c(-0.7, 0.5))
biplo
library(ggplot2)
install.packages('glue')
ggplot2::autoplot(pr.out)
pr.out$rotation=-pr.out$rotation
pr.out$x=-pr.out$x
biplot(pr.out, scale=0)
pr.out$sdev
pr.var=pr.out$sdev^2
pr.var
pve=pr.var/sum(pr.var)
pve
plot(pve, xlab="Principal Component", ylab="Proportion of Variance Explained", ylim=c(0,1),type='b')
plot(cumsum(pve), xlab="Principal Component", ylab="Cumulative Proportion of Variance Explained", ylim=c(0,1),type='b')
a=c(1,2,8,-3)
cumsum(a)

ematrix_df = read.csv("C:/Users/DHYHZ/Desktop/nbtrial/ematrix_df.csv", row.names = 1)
names(ematrix_df)
rownames(ematrix_df)
names(ematrix_df)[1] = "2-Aminoethanol"
em = data.matrix(ematrix_df)
dim(em)
emt =t(em)
dim(emt)
ecombi = emt %*% em
dim(ecombi)

exc = row.names(ecombi)
exc
names(ecombi)
apply(ecombi, 2, mean)
apply(ecombi, 2, var)
epr.out=princomp(ecombi, cor = FALSE, scores = TRUE, covmat = NULL)
names(epr.out)
epr.out$center
epr.out$scale
epr.out$n.obs
epr.out$loadings
epr.out$sdev
epr.out$scores
epr.out$call
dim(epr.out$x)
plot(epr.out, scale=0)
biplot(epr.out, choices = 1:2, scale=1)
biplot(epr.out, scale=0, expand=5, xlim=c(-0.50, 0.3), ylim=c(-0.7, 0.5))
biplot(epr.out, choices = 2:3, scale=1)
biplot(epr.out, scale=1,  xlim=c(-0.90, 0.7), ylim=c(-0.4, 0.6))
biplot(epr.out, choices = 3:4, scale=1)
write.csv(ecombi, file="ecombi.csv", row.names = T, col.names = F)
