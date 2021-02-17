# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille',
         'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September',
          'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977,
         1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160,
                       175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], [
    'Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M',
           'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']


# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11,
          2068, 269, 318, 107, 65, 19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]


""" Variables """


# dictionary of hurricanes: key = name, value = dictionaries of hurricane data
hurricanes = {}
hurricanes_by_year = {}  # dictionary of hurricanes keyed by year
updated_damages = []  # list to hold damages converted from string to float
hurricane_count_by_area = {}  # dictionary of affected areas by count
most_affected_area = ""  # stores most affected area
most_affected_count = 0  # stores count of most affected area


""" Function to convert damages from string to float type"""


def update_damages(toChange):

    conversionFactor = {"M": 1000000, "B": 1000000000}
    updated_damages = []
    # For each item, take the string minus M or B and multiply by the conversion factor
    # Save/append to updated_damages
    for item in toChange:
        if ("M" in item):
            updated_damages.append(
                float(item[0:item.find("M")]) * conversionFactor["M"])

        elif ("B" in item):

            updated_damages.append(
                float(item[0:item.find("B")]) * conversionFactor["B"])

        else:
            updated_damages.append("Damages not recorded.")

    return updated_damages


""" Function to create a dictionary of hurricane data key = name, value = data """


def create_hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurricanes = {}
    for storm in range(len(names)):
        hurricanes[names[storm]] = {
            "Name": names[storm],
            "Month": months[storm],
            "Year": years[storm],
            "Max Sustained Wind": max_sustained_winds[storm],
            "Areas Affected": areas_affected[storm],
            "Damage Caused": damages[storm],
            "Deaths": deaths[storm]
        }

    return hurricanes


""" Function to key hurricanes dictionary year  """


def convert_hurricanes_to_year_key(hurricanes):
    hurricanes_by_year = {}
    for storm in hurricanes:
        """ Takes hurricane position storm and key "Year" as current year.
        Then compares it against current keys, if not match, add, if match, append"""
        current_year = hurricanes[storm]["Year"]
        current_hurricane = hurricanes[storm]

        if current_year not in hurricanes_by_year:
            hurricanes_by_year[current_year] = [current_hurricane]
        else:
            hurricanes_by_year[current_year].append(current_hurricane)

    return hurricanes_by_year


""" Function to count how many areas are affected """


def count_areas(hurricanes):
    area_list = {}
    for hurricane in hurricanes:
        for area in hurricanes[hurricane]["Areas Affected"]:
            if area not in area_list:
                area_list[area] = 1
            else:
                area_list[area] += 1
    return area_list


""" Function to find most affected area """


def find_most_affected_area(hurricane_area_count):

    most_affected_area = ""
    most_affected_count = 0

    for area in hurricane_area_count:
        if hurricane_area_count[area] > most_affected_count:
            most_affected_area = area
            most_affected_count = hurricane_area_count[area]

    return most_affected_area, most_affected_count

# write your find most affected area function here:


# write your greatest number of deaths function here:


# write your catgeorize by mortality function here:


# write your greatest damage function here:


# write your catgeorize by damage function here:


updated_damages = update_damages(damages)
hurricanes = create_hurricane_dictionary(
    names, months, years, max_sustained_winds, areas_affected, damages, deaths)
hurricanes_by_year = convert_hurricanes_to_year_key(hurricanes)
hurricane_area_count = count_areas(hurricanes)
most_affected_area, most_affected_count = find_most_affected_area(
    hurricane_area_count)
