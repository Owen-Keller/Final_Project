# Final_Project
Library of babbel, Create books that are 100million chars long each randomly generated using sqrt(prime) results
this project uses Hero's method or babylonian Method depending on name preference. to aproximate the square root of an integer.
The returned irrational number is then sliced and converted into asscci characters.

first check if the first 3 characters are greater than 126 if they are then split them in half
EXAMPLE: 144 is split into 14 and 44
if one half is greater than or equal to 32 then it converts to a character else it skips to the next three integers
if the starting character is less than 126 but greater than 32 then it will convert to character anyways.

this solves for integers between 99 - 126 range

if the above fail which will never happen, it will skip those 3 integers.

it then writes all the output to a file to be read later.

within the main.py hardcoded is a list of over 30 different primes. each larger than the last.
it then creates a file and tells you when the txt file is created.


