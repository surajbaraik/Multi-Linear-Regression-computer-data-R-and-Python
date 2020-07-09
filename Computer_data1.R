


ComputerData <-read.csv(file.choose())
Computer_data <- ComputerData[,-1]
View(Computer_data)
class(Computer_data)


library(plyr)
Computer_data1 <- Computer_data
Computer_data1$cd <- as.numeric(revalue(Computer_data1$cd,c("yes"=1, "no"=0)))
Computer_data1$multi <- as.numeric(revalue(Computer_data1$multi,c("yes"=1, "no"=0)))
Computer_data1$premium <- as.numeric(revalue(Computer_data1$premium,c("yes"=1, "no"=0)))
View(Computer_data1)
class(Computer_data1)

attach(Computer_data1)
summary(Computer_data1) 

plot(speed, price)
plot(hd, price)
plot(ram, price)
plot(screen, price)
plot(cd, price)
plot(multi, price)
plot(premium, price)
plot(ads, price)
plot(trend, price)
windows()


pairs(Computer_data1)
cor(Computer_data1)


Model.Computer_data1 <- lm(price~speed+hd+ram+screen+cd+multi+premium+ads+trend)
summary(Model.Computer_data1)

