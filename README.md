# Midterm Project Report
## Overview
The goal of our project is to examine the relationship between the price of hotels in Austin and their distance from downtown, the rating scores and whether it is on holiday. 
## Data
### Datasets Sources
Our data sets consist of the name, distance from downtown, price and rating scores of hotels in Austin. The three separate datasets are from Thanksgiving holiday, Christmas holiday and non-holiday, which are the same period of three months: November 21-27, 2022, December 21-27, 2022 and January 21-27, 2023. All our data is from https://www.booking.com/.
### Collection Methods
We scrape the data from the website using BeautifulSoup and requests. We can find the name，score and distance from city center of each hotel by positioning the div in the HTML. Then we do the same thing to the price. We can use the dollar sign ($) to help us find the position when the price element cannot be found. And then we can convert the price from a string to a float. Finally, we extract the data of November, December and January and save them into csv files.

### Rerun instructions
* 1. select "Use this template" and create a repository with the name "Midterm-project".
* 2. clone the repo, running `cd Midterm-project` to open the repository
* 3. run `python scrape/scrape.py`, you will see a new file named “dataset” in the "Midterm-project" folder.
* 4. launch Jupyter notebook on terminal, click on November.ipyn
* 5. Run the code
* 6. Go to Jupyter Home Page, open NovemberPlot.ipyn, run all the code.
* 7. Go to Jupyter Home Page, open NovemberFiltered.ipyn, run all the code.
* 


### Data Limitations 
One issue that must be confronted here is that there is a certain incompleteness in our data due to the display mechanism of the website. When a hotel's available room types are all sold out, it will not be shown in the search list, which will inevitably lead to some inaccuracy. Another limitation is that considering the difficulty of quantifying, our data do not include the information of room type such as bed size and only use two adults to one room as a control variable condition. 
### Data Extensions
We could consider to include the availability of specific popular amenities such as gyms, swimming pools, parking lots and free WiFi as binary variables in the regression analysis to see the relationship between them and the price or rating scores.
We could quantify the room type such as the bed size, to see whether a different bed size will lead to different prices or rating scores. 
However, because the room types and amenities of different hotels or apartments are named very differently, it is difficult to identify and integrate the data. 
