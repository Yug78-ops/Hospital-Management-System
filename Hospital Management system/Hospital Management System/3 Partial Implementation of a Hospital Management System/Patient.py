from inheritance import person

class Patient(person):

    def __init__(self, first_name, surname, age, mobile, postcode, symptoms='Not recorded',doctor="None"):
        
        super().__init__(first_name,surname)
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__symptoms = symptoms
        self.__doctor = doctor
    
    def get_doctor(self) :
        return self.__doctor
    
    def set_doctor(self,doctor):
        self.__doctor = doctor

    def link(self, doctor):
        self.__doctor = doctor

    def print_symptoms(self):
        print (self.__symptoms)

    def get_symptoms(self):
        return self.__symptoms
    
    def set_symptoms(self,symptoms):
        self.__symptoms = symptoms

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
    

    def patient_info(self):
        return f"{self.get_first_name()},{self.get_surname()},{self.__age},{self.__mobile},{self.__postcode},{self.__symptoms},{self.__doctor}"
