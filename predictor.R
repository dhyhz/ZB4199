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

hits_by_length_new = c()
for (m in c(4)){ #0:20
hits =c()
for (q in 1:200){ #1:200
  hits = c(hits, 0)
}
for (j in 1:20) { #20 files
  a = c()
  b = c()
  c = c()
  for (i in 14:14){ #1:200
    #print(i)
    matrix_df2 = read.csv(sprintf("C:/Users/DHYHZ/Desktop/nbtrial/predictionsv5/%s/%s.csv", j, i), row.names = 1)
    names(matrix_df2)
    rownames(matrix_df2)
    names(matrix_df2)[1] = "2-Aminoethanol"
    
    info = read.csv(sprintf("C:/Users/DHYHZ/Desktop/nbtrial/predictionsv5/Test_info/info_%s.csv", j), row.names = 1)
    for (k in 1:3){
      index = info[k,1] # 1,2,3
      
      test2 = matrix_df2[index,]
      #test1
      arr = c(names(sort(head(test2), decreasing = TRUE))[1:(counts[index]+m)])
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
hits_by_length_new = c(hits_by_length_new, hits)
}

#hits_by_length[4001:4200] - hits_by_length[1:200]

x_new = hits_by_length_new
hits_by_threshold_new = matrix(x_new, nrow=1, ncol=200, byrow=T)
write.csv(hits_by_threshold_new, file="C:/Users/DHYHZ/Desktop/nbtrial/predictionsv4_test/hits_by_threshold_new.csv")

for (ii in 1:1){ #dont run again
  for (vv in 1:200){
    hits_by_threshold_new[ii,vv] = hits_by_threshold_new[ii,vv]/60
  }
}

write.csv(hits_by_threshold_new, file="C:/Users/DHYHZ/Desktop/nbtrial/predictionsv4_test/hits_by_threshold_new.csv")

plot(hits_by_threshold_new[1,], type = "l", lwd=3, col = "purple", xlab="K", ylab="Correct predictions", main="", xlim=c(0,200),ylim=c(0,1))
par(new=T)
plot(hits_by_threshold_new[2,], type = "l",lwd=3, col = "black", xlab="K", ylab="Correct predictions", xlim=c(0,200),ylim=c(0,1))
par(new=T)
plot(hits_by_threshold_new[3,], type = "l",lwd=3, col = "cyan", xlab="K", ylab="Correct predictions", xlim=c(0,200),ylim=c(0,1))
par(new=T)
plot(hits_by_threshold_new[4,], type = "l",lwd=3, col = "green", xlab="K", ylab="Correct predictions", xlim=c(0,200),ylim=c(0,1))
par(new=T)
plot(hits_by_threshold_new[1,1:50], type = "l",lwd=3, col = "blue", xlab="K", ylab="Correct predictions",main="Proportion of correct predictions (Test dataset)", xlim=c(0,50),ylim=c(0,1))
par(new=T)
plot(hits_by_threshold_new[6,], type = "l",lwd=3, col = "red", xlab="K", ylab="Correct predictions", xlim=c(0,200),ylim=c(0,1))

barplot(hits_by_threshold_new[1,c(3,4,10,12,13,14)], main="Proportion of correct predictions", horiz=TRUE, 
        names.arg=c("3", "4", "10", "12", "13", "14"), xlim=c(0,1), ylab="K", xlab="Correct predictions")

new = c()
for (m in c(4)){ #0:20
  hits =c()
  for (q in 1:5){ #1:200
    hits = c(hits, 0)
  }
  for (j in 1:5) { #20 files
    a = c()
    b = c()
    c = c()
    for (i in 5:6){ #1:200
      #print(i)
      matrix_df4 = read.csv(sprintf("C:/Users/DHYHZ/Desktop/nbtrial/predictionsv5/%s/%s.csv", j, i), row.names = 1)
      names(matrix_df4)
      rownames(matrix_df4)
      names(matrix_df4)[1] = "2-Aminoethanol"
      
      info = read.csv(sprintf("C:/Users/DHYHZ/Desktop/nbtrial/predictionsv5/Test_info/info_%s.csv", j), row.names = 1)
      for (k in 1:1){
        index = info[k,1] # 1,2,3
        
        test4 = matrix_df4[index,]
        #test1
        arr = c(names(sort(head(test4), decreasing = TRUE))[1:(counts[index]+m)])
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
        print(arr)
        print(" ")
      }
    }
    #a
    hits = hits + a + b +c
    
  }
  print(m)
  print(hits)
  new = c(new, hits)
}
