len = read.csv("C:/Users/DHYHZ/Desktop/nbtrial/matrix_clean_df.csv", row.names = 1)
counts = c()
for (i in 1:815){
  count = 0
  for (j in 1:length(len[i,])){
    count = count + len[i,j]
  }
  counts = c(counts, count)
}
counts

hits_coatings = c()
for (m in c(4)){ #20){
hits =c()
for (q in 1:200){
  hits = c(hits, 0)
}
for (j in c(14,15)) { #change for drug type
  a = c()
  b = c()
  c = c()
  for (i in 1:200){ #change for testing
    #print(i)
    matrix_df3 = read.csv(sprintf("C:/Users/DHYHZ/Desktop/nbtrial/predictionsv4/%s/%s.csv", j, i), row.names = 1)
    names(matrix_df3)
    rownames(matrix_df3)
    names(matrix_df3)[1] = "2-Aminoethanol"
    
    info = read.csv(sprintf("C:/Users/DHYHZ/Desktop/nbtrial/predictionsv4/Training_info/info_%s.csv", j), row.names = 1)
    for (k in 1:3){
      index = info[k,1] # 1,2,3
      
      test3 = matrix_df3[index,]
      #test1
      arr = c(names(sort(head(test3), decreasing = TRUE))[1:(counts[index]+m)])
      if (k == 1){
        if(info[k,3] %in% arr){
          a = c(a, 1)
        }
        else{
          a = c(a, 0)
        }
      }
      if (k == 2){
        if(info[k,3] %in% arr){
          b = c(b, 1)
        }
        else{
          b = c(b, 0)
        }
      }
      if (k == 3){
        if(info[k,3] %in% arr){
          c = c(c, 1)
        }
        else{
          c = c(c, 0)
        }
      }
    }
  }
  #a
  hits = hits + a + b +c

}
print(m)
print(hits)
hits_coatings = c(hits_coatings, hits)
}

 #hits_by_length[4001:4200] - hits_by_length[1:200]

x_new = hits_tablets
hits_tablets_new = matrix(x_new, nrow=1, ncol=200, byrow=T)
write.csv(hits_sols_new, file="C:/Users/DHYHZ/Desktop/nbtrial/predictionsv4_test/hits_tablets_new.csv")

for (ii in 1:200){ #dont run again
  for (jj in 1:1){
    hits_sols_new[jj,ii] = hits_sols_new[jj,ii]/24
  }
}

for (ii in 1:200){ #dont run again
  for (jj in 1:1){
    hits_gels_new[jj,ii] = hits_gels_new[jj,ii]/9
  }
}

for (ii in 1:200){ #dont run again
  for (jj in 1:1){
    hits_tablets_new[jj,ii] = hits_tablets_new[jj,ii]/15
  }
}

for (ii in 1:200){ #dont run again
  for (jj in 1:1){
    hits_granules_new[jj,ii] = hits_granules_new[jj,ii]/6
  }
}

for (ii in 1:200){ #dont run again
  for (jj in 1:1){
    hits_coatings_new[jj,ii] = hits_coatings_new[jj,ii]/6
  }
}

write.csv(hits_sols_new, file="C:/Users/DHYHZ/Desktop/nbtrial/predictionsv4_test/hits_sols_new.csv")
write.csv(hits_gels_new, file="C:/Users/DHYHZ/Desktop/nbtrial/predictionsv4_test/hits_gels_new.csv")
write.csv(hits_tablets_new, file="C:/Users/DHYHZ/Desktop/nbtrial/predictionsv4_test/hits_tablets_new.csv")
write.csv(hits_granules_new, file="C:/Users/DHYHZ/Desktop/nbtrial/predictionsv4_test/hits_granules_new.csv")
write.csv(hits_coatings_new, file="C:/Users/DHYHZ/Desktop/nbtrial/predictionsv4_test/hits_coatings_new.csv")

#plot(hits_sols_new[1,], type = "l", lwd=3, col = "purple", xlab="K", ylab="Correct predictions", main="", xlim=c(0,200),ylim=c(0,1))
#par(new=T)
plot(hits_sols_new[1,], type = "l",lwd=3, col = "red", xlab="K", ylab="Correct predictions", main="Proportion of correct predictions (Solutions/Suspensions)", xlim=c(0,200),ylim=c(0,1))
par(new=T)
plot(hits_coatings_new[1,], type = "l",lwd=3, col = "purple", xlab="K", ylab="Correct predictions",main="Proportion of correct predictions (Coatings) (Test dataset)", xlim=c(0,200),ylim=c(0,1))
par(new=T)
plot(hits_granules_new[1,], type = "l",lwd=3, col = "green", xlab="K", ylab="Correct predictions", main="Proportion of correct predictions (Granules)", xlim=c(0,200),ylim=c(0,1))
par(new=T)
plot(hits_gels_new[1,], type = "l",lwd=3, col = "blue", xlab="K", ylab="Correct predictions", main="Proportion of correct predictions (Semi-solids)", xlim=c(0,200),ylim=c(0,1))
par(new=T)
plot(hits_tablets_new[1,], type = "l",lwd=3, col = "black", xlab="K", ylab="Correct predictions", main="Proportion of correct predictions (Tablets)", xlim=c(0,200),ylim=c(0,1))

barplot(hits_sols_new[1,c(12,14,33,34,35,38,39)], main="Proportion of correct predictions (Solutions/Suspensions)", horiz=TRUE, 
        names.arg=c("12",'14','33','34','35','38','39'), xlim=c(0,1), ylab="K", xlab="Correct predictions") #, space=c(1,1), width=c(1,1))
