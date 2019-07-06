# Forecasting Crime with FB Prophet

Data/ contains csv files with number of offenses.
The zip file contains number of offenses grouped by each category, e.g. Theft, Assault, etc.
The R scripts pulled and cleaned the data from OpenBR's API, allowing us to remove unnecessary data and then convert the data we wanted into a csv format. Our Python code imported the pandas and fbprohpet modules to let us interpret our data to give a time-based graph using fbprophets additive regression model. We then split each piece of data up to give individualized graph so we could better interpret our data and give as accurate predictions as possible.
You will need to run our Python code in a Jupyter Notebook. To run Fbprophet you will need to visit https://facebook.github.io/prophet/docs/installation.html#python and follow the installation steps for Python.
For the R scripts, you will need to download RStudio which you can download free here: https://www.rstudio.com/products/rstudio/download/.
