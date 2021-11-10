# AirBNB-Web-Scraper
Simple Airbnb Web Scraper using BeautifulSoup and Selenium

## Usage
To install requirements:
`pip3 install -r requirements.txt`

To run the code:
`python3 main.py`

The list of unique property id's is pre defined within the main.py file should you wish to change it.

## Output
The script will scrape AirBnb website for the given properties. If the link is active it will store the name of the property, the URL, property_type, number of guests, number of bedrooms, number of bathrooms, number of beds, available aminites and unavailable aminites within a dictionary. If the link is not valid it will store the name of the property as 'Undefined' along with the URL. Please see example:
```
'Undefined': {'url': 'https://www.airbnb.co.uk/rooms/33571268'},
'Tiny house hosted by Tanya': {
        'url': 'https://www.airbnb.co.uk/rooms/20669368', 
        'property_type': 'Entire home', 
        'Number of Guests': '4 guests', 
        'Number of Bedrooms': '1 bedroom', 
        'Number of Beds': '1 bed', 
        'Number of Bathrooms': '1 bathroom', 
        'Available Amenities': ['Suitable for events', 'Indoor fireplace', 'Heating', 'Smoke alarm', 'Fire extinguisher', 'First aid kit', 'Kitchen', 'Refrigerator', 'Cooking basics', 'Oven', 'Patio or balcony', 'BBQ grill', 'Free parking on premises', 'Hot tub', 'Host greets you'], 
        'Unavailable Amenities': ['Unavailable: Security cameras on property', 'Unavailable: Wifi', 'Unavailable: TV', 'Unavailable: Washing machine', 'Unavailable: Air conditioning', 'Unavailable: Hair dryer', 'Unavailable: Essentials', 'Unavailable: Carbon monoxide alarm', 'Unavailable: Shampoo', 'Unavailable: Private entrance']}
 ````
 ## Potential Improvments
Given more time I would probably add an option to pass the unique properties id's via the command line. This would imporve the the usabily as the user would not have to change the id's within the code directly but rather pass a list to the main.py file as a flag. Other possible improvments could be creating a class for the web scraper function, although this could be a bit over engineered just for this single use. 
Furthermore, I would improve the script by gathering more data, prehaps the property avaialblity for the next month and if not available for the next month the earliest available date for the user to make a booking as well as the prices. A cool feautre would be to check the location of the property and use another web scrape to show the user local sightseeing or restaturants based of highest reviews. Adding more error catching for faulty / invalide links as well would be a good idea as well.
