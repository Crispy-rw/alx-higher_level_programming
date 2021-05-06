#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = 0
    n_rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) != str or roman_string is None:
        return 0
    for i in range(len(roman_string)):
        if i > 0 and n_rom[roman_string[i - 1]] < n_rom[roman_string[i]]:
            roman += n_rom[roman_string[i]] - (2 * n_rom[roman_string[i - 1]])
        else:
            roman += n_rom[roman_string[i]]
    return roman
