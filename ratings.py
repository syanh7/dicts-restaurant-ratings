"""Restaurant rating lister."""


# put your code here
# open the file
# read the scores file - line by line and strip using : split (":")
# create a dictionary 
# enter the key and value into the dictionary 
# Key into a list to sort alphabetically in the list
# print the list /print the dictionary with an f string to include "is rated at"

def restaurant_ratings_from_file(file_name):
    #open file
    file = open(file_name)

    #goes through each line of file
    #split the line by ':' and unpack
    #into two variables
    #add key and value to dictonairy 
    for line in file:
        line = line.rstrip()
        restaurant_name, rating = line.split(':')

        restaurant_dict[restaurant_name] = rating
    
    file.close()
    
def restaurant_ratings_from_user_input():
    #get user input for resturant and rating
    restaurant_name = input("Enter the name of the restaurant: ")
    rating = input("Enter the rating of the restaurant: ")

    #add user generated resturant and rating to dict 
    restaurant_dict[restaurant_name] = rating

def print_restaurant_ratings():
    # restaurant_name_list = restaurant_dict.keys()
    # restaurant_name_list = sorted(restaurant_name_list)

    # for key in restaurant_name_list:
    #     print(f'{key} is rated at {restaurant_dict[key]}'))

    #gets a sorted list of keys from restaurant_dict
    #iterates through the list, gets value by key from restaurant dict
    for key in sorted(restaurant_dict):
        print(f'{key} is rated at {restaurant_dict[key]}')


#creates global dict restaurant_dict
restaurant_dict = {}
restaurant_ratings_from_file('scores.txt')

#loops through user input
while True:
    
    restaurant_ratings_from_user_input()
    print_restaurant_ratings()

    user_input = input("Press [q] to quit, enter to continue: ").lower()
    if user_input == 'q':
        break


