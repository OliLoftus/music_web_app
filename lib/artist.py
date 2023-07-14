class Artist:
    def __init__(self, id, name, genre):
        self.id = id
        self.name = name
        self.genre = genre

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"{self.name}, genre: {self.genre}"
    
    def is_valid(self):
        if self.title == None or self.title == "":
            return False
        if self.release_year == None or self.release_year == "":
            return False
        if self.artist_id == None or self.artist_id == "":
            return False
        return True
    
    def generate_errors(self):
        errors = []
        if self.title == None or self.title == "":
            errors.append("Title can't be blank")
        if self.release_year == None or self.release_year == "":
            errors.append("Release year can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)