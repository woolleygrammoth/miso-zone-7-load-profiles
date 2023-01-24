### Index of this directory 

env - ignore; for development purposes
raw_csv
    - hourly load data from rate cases for DTE & CE (broken down by class)
    - overall Michigan load from EIA sales report
raw_xlsx - contains the same data but in the more cumbersome xlsx format
zone-7-data 
    - 2019 load profiles for CE & DTE, total instead of broken down by customer class
    - __miso-zone-7-2019-total-load-profile.csv - CE, DTE, CE+DTE, and scaled CE+DTE(=Zone 7) load profiles__
    - miso-zone-7-total-load.txt - overall load either counting Greenskies Renewable Energy or not, and excluding either 'Energy' or 'Delivery' Service Type (the Zone 7 load profile currently counts Greenskies and excludes the Energy service type)
    - zone-7-2019-load-profile.jpg - a graphic of the results
requirements.txt - ignore; for development purposes
zone-7-load-profiles.ipynb - all the code to tranform raw data into the usable miso-zone-7-2019-total-load-profile.csv and create the graphic
