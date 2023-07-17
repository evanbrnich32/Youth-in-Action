# Youth In Action
# A Python Program by XYZ Youth

###############################
# Imports
###############################

import math
import random

###############################
# Variables
###############################

# Creating Variables
age_range = (18, 25)
number_of_participants = 30

###############################
# Functions
###############################

# Function to check age eligibility
def age_check(age):
    if age >= age_range[0] and age <= age_range[1]:
        return True
    else:
        return False

# Function to generate list of participants
def generate_participants(num_of_participants):
    participants = []
    for i in range(num_of_participants):
        age = random.randint(age_range[0], age_range[1])
        participants.append(age)
    return participants

# Function to check participation eligibility
def check_eligible_participants(participants):
    eligible_participants = []
    for participant in participants:
        is_eligible = age_check(participant)
        if is_eligible:
            eligible_participants.append(participant)
    return eligible_participants

###############################
# Main Program
###############################

# Generate list of participants
participants = generate_participants(number_of_participants)

# Check eligibilty of participants
eligible_participants = check_eligible_participants(participants)

# Print eligible participants
print("Eligible Participants: ", eligible_participants)

# Print number of eligible participants
print("Number of Eligible Participants: ", len(eligible_participants))