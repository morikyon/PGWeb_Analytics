#imports
library("ggplot2")
library("ggsci")
library("dplyr")

# datasets
data <- read.csv("data/programmableweb_list.csv", header = T)
# filter > 300
summary <- data %>% group_by(Category) %>% summarise(count = n()) %>% filter(count > 300)

# plots
plots <- ggplot(summary, aes(x=Category, y=count, fill=Category)) + 
  geom_bar(stat = "identity")
plot(plots)
