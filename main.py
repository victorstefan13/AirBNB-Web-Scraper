import web_scrape as ws
import web_scraper_helpers as wsh


def run_web_scrape(url: str, property_unique_id: list) -> dict:
    properties = {}

    for unique_id in property_unique_id:
        current_property = ws.scrape_page(url+unique_id)

        if current_property[0] != 'Undefined':
            property_type = ws.find_data_in_soup(current_property[1], 'div', '_1qsawv5')
            property_details = wsh.split_str(ws.find_data_in_soup(current_property[1], 'ol', '_194e2vt2'))
            property_details = wsh.remove_white_space(property_details)

            amenities = ws.find_amenities("//*[@class='_gw4xx4']")
            amenities = wsh.tidy_string(amenities)
            amenities, unavailable_amenities = wsh.split_list(amenities)

            properties[current_property[0]] = {}
            properties[current_property[0]]['url'] = url+unique_id
            properties[current_property[0]]['property_type'] = property_type
            properties[current_property[0]]['Number of Guests'] = property_details[0]
            properties[current_property[0]]['Number of Bedrooms'] = property_details[1]
            properties[current_property[0]]['Number of Beds'] = property_details[2]
            properties[current_property[0]]['Number of Bathrooms'] = property_details[3]
            properties[current_property[0]]['Available Amenities'] = amenities
            properties[current_property[0]]['Unavailable Amenities'] = unavailable_amenities
        else:
            properties[current_property[0]] = {}
            properties[current_property[0]]['url'] = url+unique_id
    
    ws.kill_window()

    return properties

if __name__ == "__main__":

    url = 'https://www.airbnb.co.uk/rooms/'
    property_unique_id = ['33571268', '20669368', '50633275']

    result = run_web_scrape(url, property_unique_id)

    print(result)