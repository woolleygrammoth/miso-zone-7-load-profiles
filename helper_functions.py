import numpy as np
from datetime import datetime
def make_timestamp(year, month, day, hour): 
    """
    Take the Month, Day, and Hour columns and express it as a single timestamp column. For example: 
    Month-4, Day-15, Hour-11 becomes 2019-04-15 10:00 (we are considering HE 11 to be stamped at 10am)
    """
    return datetime.strptime(f'{month}/{day}/{year} {hour - 1}', '%m/%d/%Y %H')

def hour_from_timestamp(timestamp): 
    """
    Given a Datetime object, returns the hour of the year (from 1 to 8760), i.e. 1/3/2019 00:00:00 --> 49
    """
    day = datetime.strftime(timestamp, '%j')
    hour = timestamp.hour + 1
    return (int(day) - 1) * 24 + hour

def convert_energy_number_to_int(string): 
    """
    Converts the text from an element of the energy (kWh or MWh) column to an integer
    """
    if '-' in string:
        return np.nan
    else: 
        return float(string.replace(',', ''))