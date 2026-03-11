"""""
Given a list of grades:
14, 15, 10, 12, 8, 16, 11, 14, 19
Display a report in the following format:

Number of grades = 9
Grade 1 = 14/20 (Very good)
Grade 2 = 15/20 (Very good)
Grade 3 = 10/20 (Fair)
Grade 4 = 12/20 (Good)
Grade 5 = 08/20 (Unsatisfactory)
Grade 6 = 16/20 (Excellent)
Grade 7 = 11/20 (Fair)
Grade 8 = 14/20 (Very good)
Grade 9 = 19/20 (Excellent)
Minimum grade = 8
Maximum grade = 19
Average = 13.2 (Good)
Delta = 11

Notes:

Delta:
This is the difference between the minimum and maximum scores.

Grades:
16 - 20   = Excellent
14 - 15.9 = Very good
12 - 13.9 = Good
10 - 11.9 = Fair
00 - 9.9  = Insufficient

"""""

### ---- VARIABLES ---- ###
notes = [14, 15, 10, 12, 8, 16, 11, 14, 19]



### ---- FUNCTIONS  ---- ###

#Function to return the total number of notes: argument list -> must output as str
def total(i : list) -> str:
    for i in notes:
        result = len(notes)
        return result



#Function to return mentions: int argument -> must output str
#Preconditions
def mention(i : int | float) -> str:
    if i < 0:
        raise Exception("The note cannot be less than 0.")
    if i > 20:
        raise Exception("The note cannot be more than 20.")
#Logique
    if i >= 16:
        return "(excellent)"
    elif i >= 14:
        return "(very good)"
    elif i >= 12:
        return "(good))"
    elif i>= 10:
        return "(fair)"
    else:
        return "(insufficient)"



#Function for receive minimum note
def get_minimum_note(notes: list) -> int:
    minimal_note = 20
    for note in notes:
        if note < minimal_note:
            minimal_note = note
    return minimal_note


#Function for receive maximum note
def get_maximum_note(notes: list) -> int:
    maximum_note = 0
    for note in notes:
        if note > maximum_note:
            maximum_note = note
    return maximum_note



#Function for calculate the total of notes
def sum_notes(notes: list) -> int:
    sum = 0
    for i in notes:
        sum = sum + i
    return sum


#Function for calculate average note
def average_note(notes: list) -> float:
    return sum_notes(notes) / total(notes)



#Function for calculate the delta (difference between minimal and maximal note)
def delta(notes: list) -> int:
    return get_maximum_note(notes) - get_minimum_note(notes)



################            ################            ################            ################
                ############                ###########                  ###########

### --- VISUEL --- ###
print("------------------------------------------")
print(f"Number total of grades = {total(notes)}")
print("------------------------------------------")
index = 1
for i in notes:
    print(f"Note {index} = {i}/20 {mention(i)}")

print("*******************************************")
print(f"Minimal grade = {get_minimum_note(notes)} ")
print("*******************************************")
print(f"Maximal grade = {get_maximum_note(notes)}")
print("*******************************************")
print(f"Average grade = {average_note(notes)}")
print("*******************************************")
print(f"Delta = {delta(notes)}")
print("*******************************************")

################            ################            ################            ################
                ############                ###########                  ###########
