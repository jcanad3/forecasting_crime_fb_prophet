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

ggplot() +
  geom_line(data=num_offenses, aes(x=offense_date, y=num_crimes)) +
  ylab("Number of Crimes per Day") +
  xlab("Offense Date")

# different number of offenses for each crime category
num_offenses_by_category <- crimeIncidents %>% group_by(offense_date,crime) %>% summarise(num_crimes = n())
num_offenses_by_category$offense_date <- as.Date(num_offenses_by_category$offense_date)

categories <- unique(crimeIncidents$crime)

for (cat in categories) {
  data_per_cat <- num_offenses_by_category %>% filter(crime == cat)
  per_crime_cat_weather <- inner_join(weather_data, data_per_cat, by=c("year_month_day"="offense_date"))
  write.csv(per_crime_cat_weather %>% select(-crime), paste("data_by_category/",cat,".csv",sep=""), row.names= FALSE, quote=FALSE)
}
