class Person:
    #setting variables with initial values 
    _eye_color = ""
    _height = 0
    _favorite_jokes = []
    #getting eye color
    def get_eye_color(self):
        #returns current instance of eye color 
        return self._eye_color
    #getting height 
    def get_height(self):
        #returns current instance of height 
        return self._height
    #getting favorite jokes
    def get_favorite_jokes(self):
        #returns current instance of favorite jokes
        return self._favorite_jokes
    #setting eye color
    def set_eye_color(self, eye_color):
        #if user enters in a blank string print that input is invalid 
        if not eye_color:
            print("eye color invalid")
        #if users enters a valid response set eye color 
        else:
            #sets current instance of eye color
            self._eye_color = eye_color 
    #setting height 
    def set_height(self, height): 
        try:
            #converting height to an integer 
            height_as_int = int(height)
        except ValueError:
            #if height is not an integer this gets printed
            print("height must be a number")
            return 
            #stops if height is not in proper form so height does not get assigned      
        #setting current instance of height
        self._height = height_as_int        
    #setting favorite jokes
    def set_favorite_jokes(self, favorite_jokes):
        #seperating each joke by splitting on the "|" character
        parsed_favorite_jokes = favorite_jokes.split("|")
        #checking to ensure multiple jokes were inputted
        if len(parsed_favorite_jokes) < 2:
            print("must have at least 2 jokes")
        else:
            #setting current instance of favorite_jokes
            self._favorite_jokes = parsed_favorite_jokes
    #printing current instances of all variable
    def print_attributes(self):
        print(f"Eye color: {self._eye_color}")  
        print(f"Height: {self._height}")
        print(f"Favorite jokes: {self._favorite_jokes}")

    



