# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).
import random

states = {'Alabama':'Montgomery', 'Alaska':'Juneau', 'Arizona':'Phoenix', 'Arkansas':'Little Rock', 'California':'Sacramento', 'Colorado':'Denver',
          'Connecticut':'Hartford', 'Delaware':'Dover', 'Florida':'Tallahassee', 'Georgia':'Atlanta', 'Hawaii':'Honolulu', 'Idaho':'Boise',
          'Illinois':'Springfield', 'Indiana':'Indianapolis', 'Iowa':'Des Moines', 'Kansas':'Topeka', 'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
          'Maine':'Augusta', 'Maryland':'Annapolis', 'Massachusetts':'Boston', 'Michigan':'Lansing', 'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
          'Missouri':'Jefferson City', 'Montana':'Helena', 'Nebraska':'Lincoln', 'Nevada':'Carson City', 'New Hampshire' : 'Concord', 'New Jersey':'Trenton',
          'New Mexico' : 'Santa Fe', 'New York' : 'Albany', 'North Carolina' : 'Raleigh', 'North Dakota':'Bismarck', 'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
          'Oregon' : 'Salem', 'Pennsylvania' : 'Harrisburg', 'Rhode Island' : 'Providence', 'South Carolina' : 'Columbia', 'South Dakota' : 'Pierre',
          'Tennessee' : 'Nashville', 'Texas' : 'Austin', 'Utah' :'Salt Lake City', 'Vermont' : 'Montpelier', 'Virginia' : 'Richmond', 'Washington' : 'Olympia',
          'West Virginia' : 'Charleston', 'Wisconsin' : 'Madison', 'Wyoming' : 'Cheyenne'}


def main():

    loop = 'y'
    score = 0
    while loop == 'y':

        state = random.choice(list(states))
        print(state)
        answer = str(input('what is the capital of this state: '))
        if answer == states[state]:
            print('That is correct!')

            score += 1
            loop = input('Do you want another question?')
        else:
            print(f'That is incorrect, The correct answer was {states[state]}')
            loop = input('Do you want another question?')


    print(f'Your score was {score}')





main()