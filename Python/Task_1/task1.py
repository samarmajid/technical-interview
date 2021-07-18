#importing person classs
from person import Person 

#creating a person object 
user = Person()
#keep checking eye color until it gets set 
#would be repeated if user enters in an empty string
while not user.get_eye_color():
    user.set_eye_color(input("what is your eye color?\n"))
    #setting the eye color to the input 

#keep checking height until it gets set 
while not user.get_height():
    #setting height to user input 
    user.set_height(input("what is your height in inches?\n"))

#keep checking favorite jokes until it gets set 
while not user.get_favorite_jokes():
    user.set_favorite_jokes(input("what are your favorite jokes? Seperate them with | \n"))

#print all user input 
user.print_attributes()

