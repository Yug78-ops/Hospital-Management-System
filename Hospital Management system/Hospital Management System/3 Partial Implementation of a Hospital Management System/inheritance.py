class person:
    def __init__(self,first_name,surname):
        self.__first_name = first_name
        self.__surname = surname



   
    def full_name(self) :
        return f'{self.__first_name} {self.__surname}.'
    
    def get_surname(self):
        return f'{self.__surname}'
    
    def get_first_name(self):
        return f'{self.__first_name}'
    
    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name

    def set_surname(self, surname):
        self.__last_name = surname

