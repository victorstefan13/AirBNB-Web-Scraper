"""
    Python file for helper functions which could potentially be re-used thoroughout the exercise.
    Mainly for string manipulation
"""

def split_str(single_str: str) -> list:
    """Function used to split the single string for
        the property data (no of bedrooms, bathrooms etc.)"""
    return single_str.split("·")

def tidy_string(str_list: list) -> list:
    """Removes anything after the \n within a string.
        This is mainly to tidy the unavailable amenities
        i.e 'Unavailable :Wifi\nUnavailable :Wifi' -> 'Unavailable :Wifi'
    """
    return [string.split("\n", 1)[0] for string in str_list]

def remove_white_space(str_list: list) -> list:
    """Removes any leading / tailing white space"""
    return [string.strip() for string in str_list]

def split_list(amenities: list) -> list:
    """Splits the list of amenities into two lists:
        -available amenities 
        -unavailable amenities
    """
    unavailable_amenities, new_amenities = [], []

    for amenity in amenities:
        if "Unavailable:" in amenity:
            unavailable_amenities.append(amenity)
            continue
        new_amenities.append(amenity)

    return new_amenities, unavailable_amenities
