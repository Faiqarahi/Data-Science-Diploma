e_quakes<-datasets::quakes
head(e_quakes,10)
tail(e_quakes,10)

#accessing the column
e_quakes$depth

###########Summary of the data#########
summary(e_quakes$lat)
summary(e_quakes$long)
summary(e_quakes$mag)

plot(e_quakes$lat)
plot(e_quakes$long,e_quakes$long,type="p")
plot(e_quakes)

#####################
# points and lines 
plot(e_quakes$depth, type= "p") # p: points, l: lines,b: both
plot(e_quakes$mag, ylab = 'depth Concentration', 
     xlab = 'No of Instances', main = 'depth of earth quake',
     col = 'blue')
# Horizontal bar plot
barplot(e_quakes$lat, main = 'earth_quake',
        ylab = 'Depth', col= 'blue',horiz = T,axes=T)
#Histogram
hist(e_quakes$depth)
hist(e_quakes$long.R,
     main = 'depth of earthquake',
     xlab = 'depth eartherquake', col='blue')

#Single box plot
boxplot(e_quakes$lat,main="Temp_Boxplot")
# Multiple box plots
boxplot(e_quakes,main='Multiple')
#margin of the grid(mar), 
#no of rows and columns(mfrow), 
#whether a border is to be included(bty) 
#and position of the 
#labels(las: 1 for horizontal, las: 0 for vertical)
#bty - box around the plot
par(mfrow=c(3,3),mar=c(2,5,2,1),  las=0, bty="o")

plot(e_quakes$lat)
plot(e_quakes$lat, e_quakes$long)
plot(e_quakes$lat, type= "l")
plot(e_quakes$lat, type= "l")
plot(e_quakes$lat, type= "l")
barplot(e_quakes$lat, main = 'Earthquake',
        xlab = 'Earthquake levels', col='green',horiz = TRUE)
hist(e_quakes$lat.R)
boxplot(e_quakes$lat.R)
boxplot(e_quakes[,0:4], main='Multiple Box plots')

skewness(e_quakes)
kurtosis(e_quakes)
var(e_quakes)
sd(e_quakes)
