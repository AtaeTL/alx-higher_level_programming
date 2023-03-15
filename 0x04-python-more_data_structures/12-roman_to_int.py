#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_int = 0
    roman_numeral_map = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                         'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    i = 0
    while i < len(roman_string):
        if i + 1 < len(roman_string) and roman_numeral_map.get(roman_string[i]) < roman_numeral_map.get(
                roman_string[i + 1]):
            roman_int += roman_numeral_map[roman_string[i + 1]] - roman_numeral_map[roman_string[i]]
            i += 2
        else:
            roman_int += roman_numeral_map[roman_string[i]]
            i += 1
    return roman_int
