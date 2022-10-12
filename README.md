# Midterm Project Report
## Overview
Hotel plays an important role in people’s traveling life. Being in a competitive hotel industry, different hotels have various pricing strategy. Setting the background in ATX, we’re interested in analyzing the data scraped from Booking.com to find whether some specified factor has obvious influence on a hotel’s price and examine the seasonality in pricing. 
## Data
### Datasets Sources
Our data sets consist of the name, distance from downtown, price and rating scores of hotels in Austin. The three separate datasets are from Thanksgiving holiday, Christmas holiday and non-holiday, which are the same period of three months: November 21-27, 2022, December 21-27, 2022 and January 21-27, 2023. All our data is from https://www.booking.com/.
### Collection Methods
We scrape the data from the website using BeautifulSoup and requests. We can find the name，score and distance from city center of each hotel by positioning the div in the HTML. Then we do the same thing to the price. We can use the dollar sign ($) to help us find the position when the price element cannot be found. And then we can convert the price from a string to a float. Finally, we extract the data of November, December and January and save them into csv files.

### Rerun instructions
* 1. select "Use this template" and create a repository with the name "Midterm-project".
* 2. clone the repo, running `cd Midterm-project` to open the repository
* 3. run `python scrape/scrape.py`, you will see a new file named “dataset” in the "Midterm-project" folder.
* 4. 
* 5. Launch Jupyter notebook on terminal, click on November.ipyn, run the code
* 6. Go to Jupyter Home Page, open November_Plot.ipyn, run all the code.
* 7. Go to Jupyter Home Page, open Nov_Dis.ipyn, run all the code.
* 8. Go to Jupyter Home Page, open November_Filtered.ipyn, run all the code.
* 9. Go to Jupyter Home Page, open Filtered_Plot.ipyn, run all the code.
* 

### Findings
<img width="355" alt="image" src="https://user-images.githubusercontent.com/112193353/195422407-0db8ea63-2b4c-49e6-a530-4e4a1ef824ca.png">

 
The effects of these two variables met our expectation in terms of the directions, but the undesired low R square indicated the low efficiency of the model. Apparently, the data we have is limited (I’ll further address this issue in the Limitation Section), and there are numbers of unobserved factors that are affecting the price. Nevertheless, we tried to improve our model. 
By separating the high price hotel(price>1000) from the low, we built a distribution scatter plot (here we used matplotlib.) 

<img width="240" alt="image" src="https://user-images.githubusercontent.com/112193353/195422261-d600e00e-8313-4984-80c0-069c26f294ab.png">
 
 The plot showed that the majority of high price hotels were distributing around the top left corner, close distance with high score. This resulted in low sample size for high price hotel across the rest of the area. 

<img width="328" alt="image" src="https://user-images.githubusercontent.com/112193353/195422461-047a85f6-ba66-489a-9566-f72a5b910a1a.png">

         
By filtering out these clustered data, we rerun the regression.

<img width="299" alt="image" src="https://user-images.githubusercontent.com/112193353/195422515-2ec4342e-d5e7-4fe4-8203-8eb8512673bf.png">
                
The model now has a comparably stronger explanatory ability as the R square increased to 0.51. It’s worth noticing that the score has now a much lower effect on prices, with lower SE. This is a more statistically significant estimate for sthe partial effect core among the normal price hotels. The graph below is the visualization of the regression using matplotlib for 3D.

<img width="468" alt="image" src="https://user-images.githubusercontent.com/112193353/195422764-15dfd932-9990-4f48-92b7-47f4e9f5e87a.png">

 


### Data Limitations 
One issue that must be confronted here is that there is a certain incompleteness in our data due to the display mechanism of the website. When a hotel's available room types are all sold out, it will not be shown in the search list, which will inevitably lead to some inaccuracy. Another limitation is that considering the difficulty of quantifying, our data do not include the information of room type such as bed size and only use two adults to one room as a control variable condition. 
### Data Extensions
We could consider to include the availability of specific popular amenities such as gyms, swimming pools, parking lots and free WiFi as binary variables in the regression analysis to see the relationship between them and the price or rating scores.
We could quantify the room type such as the bed size, to see whether a different bed size will lead to different prices or rating scores. 
However, because the room types and amenities of different hotels or apartments are named very differently, it is difficult to identify and integrate the data. 
