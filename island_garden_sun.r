#Project to Help 'Youth in Action'

#Set Working Directory
setwd("C:/Documents/YouthInActionProject")

#Install Packages
install.packages("tidyverse")

#Load Packages
library(tidyverse)

#Read in Data
yia_data <- read_csv("YouthInActionData.csv")

#Explore Data
glimpse(yia_data)

#Include additional columns
yia_data$Income <- NA
yia_data$IncomeLevel <- NA

#Create additional columns for income levels
yia_data <-
  mutate(yia_data, IncomeLevel = 
             case_when(Income < 15000 ~ "Low Income",
                       Income >= 15000 & Income < 25000 ~ "Medium Income", 
                       Income > 25000 ~ "High Income"))

#Visualize Data 
ggplot(data=yia_data) +
  aes(x=Ethnicity, y=Income) +
  geom_bar(aes(fill=IncomeLevel), position="dodge", stat="identity")

#Summarize Data
yia_data %>% 
  group_by(IncomeLevel) %>% 
  summarise(Count=n())

#Create Word Cloud 
library(wordcloud)
library(RColorBrewer)

#Extract words from column 
words <- yia_data$Interests

#Create Colormap
cmap <- brewer.pal(8, "Dark2")

#Create Word Cloud
wordcloud(words, 
          min.freq=2,
          max.words=50,
          random.order=FALSE,
          rot.per=0.25,
          colors=cmap)
          
#Create Final Report
library(knitr)

#Create Report
kable(yia_data)

#Convert to HTML
knit2html("YouthInActionFinalReport.Rmd")