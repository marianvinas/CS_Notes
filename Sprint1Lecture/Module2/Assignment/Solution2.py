# Sprint 1 Module 2 Project

"""
csWhereIsBob
You can either manually iterate through the array or juse use the .index operation

def csWhereIsBob(names):
    try:
        return names.index("Bob")
    except:
        return -1


csSchoolYearsAndGroups
Just use a double for loop to generate all years and groups. Join them with a
comma and space in the end.

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def csSchoolYearsAndGroups(years, groups):
    res = []
    for year in range(years):
        for group in range(groups):
            res.append(f"{str(year + 1)}{str(letters[group])}")
    return ', '.join(res)


csMakeItJazzy
Iterate through the entire array and add a ‘7’ if the last character
of the chord is not ‘7’

def csMakeItJazzy(chords):
    for index, chord in enumerate(chords):
        if chord[-1] != '7':
            chords[index] = chords[index] + '7'
    return chords


csShortestWord
Transform the input string into an array using the split() API (you can also do
this manually). Iterate through the list and keep track of the shortest word.

def csShortestWord(input_str):
    words = input_str.split()
    shortestFound = float("inf")
    for word in words:
        wordLen = len(word)
        if wordLen < shortestFound:
            shortestFound = len(word)
    return shortestFound


csSumOfPositive
Iterate through all numbers and add up all numbers that are > 0

def csSumOfPositive(input_arr):
    res = 0
    for num in input_arr:
        if num > 0:
            res += num
    return res


csAnythingButFive
Iterate through all numbers between the range. Check if the number contains a 5
and count it if it’s not. You can cast the number to a string to see if a 5
is in the number.

def csAnythingButFive(start, end):
    res = 0
    for num in range(start, end + 1):
        strNum = str(num)
        if '5' not in strNum:
            res += 1
    return res

"""