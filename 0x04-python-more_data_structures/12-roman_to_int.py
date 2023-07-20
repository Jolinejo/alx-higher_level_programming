#!/usr/bin/python3
def roman_to_int(roman_string):
    key = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    u = "IV"
    t = "XL"
    h = "CD"
    th = "M"
    units, tens, hunds, thous = 0, 0, 0, 0
    for let in roman_string:
        if let in u:
            if key[let] > units:
                units = key[let] - units
            else:
                units = units + key[let]
        elif let in t:
            if units == 0:
                if key[let] > tens:
                    tens = key[let] - tens
                else:
                    tens = tens + key[let]
            else:
                units = key[let] - units
        elif let in h:
            if tens == 0:
                if key[let] > hunds:
                    hunds = key[let] - hunds
                else:
                    hunds = key[let] + hunds
            else:
                tens = key[let] - tens
        else:
            if hunds == 0:
                thous = thous + key[let]
            else:
                hunds = key[let] - hunds
    return (thous+hunds+tens+units)
