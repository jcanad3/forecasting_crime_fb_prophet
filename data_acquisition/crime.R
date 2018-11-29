# Jude Canady
# assignment 5
library(RSocrata)
library(here)
library(tidyverse)
source(here('tokensocrata.R'))
library(ggmap)

# police incidents endpoint
crimeIncidents <- 'https://data.brla.gov/resource/5rji-ddnu.csv?'
query <- "$where=offense_date between '2011-01-01' and '2018-11-21'"

crimeIncidents <-read.socrata(paste0(crimeIncidents, query), app_token = token[['app']])
crimeIncidents <- as_tibble(crimeIncidents)

crimeIncidents <- crimeIncidents %>% 
  mutate(geolocation = str_extract_all(geolocation, '[-,.,0-9]+')) %>% 
  mutate(long = map_chr(geolocation, 1), lat = map_chr(geolocation, 2)) %>% 
  mutate_at(vars(long, lat), as.double)

#all ofenses by day
num_offenses <- crimeIncidents %>% group_by(offense_date) %>% summarise(num_crimes = n())
num_offenses$offense_date <- as.Date(num_offenses$offense_date)
write.csv(num_offenses, row.names=FALSE,quote=FALSE) 

ggplot() +
  geom_line(data=num_offenses, aes(x=offense_date, y=num_crimes)) +
  ylab("Number of Crimes per Day") +
  xlab("Offense Date")
