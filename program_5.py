# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.




def main():
    courses = {}       #create empty dictionary

    course_numbers = int(input('How many courses would you like to add?: '))

    for course in range(course_numbers):
        key = str(input('What is the course ID?: '))
        value = str(input('What is the course name?: '))

        courses[key] = value



    print(f'The courses with in that subject are {find_subject(courses)}')


def find_subject(dictionary):
    subjects_found = {}

    subject = input('What subject would you like to search')
    for key in dictionary:
        if subject in key:
            subjects_found[key] = dictionary[key]
    return subjects_found

main()