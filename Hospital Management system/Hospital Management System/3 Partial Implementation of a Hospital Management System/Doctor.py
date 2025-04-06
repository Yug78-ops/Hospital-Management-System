from inheritance import person


class Doctor(person):

    def __init__(self, first_name, surname, speciality):
        super().__init__(first_name,surname)
        self.__speciality = speciality
        self.__patients = []  
        self.__appointments = []
    
    def get_speciality(self) :
        return self.__speciality

    def set_speciality(self, new_speciality):
        self.__speciality = new_speciality

    def add_patient(self, patient):
        self.__patients.append(patient)


    def __str__(self) :
        return f'{self.full_name():^30}|{self.__speciality:^15}'
    
    def get_patient(self):
        return self.__patients
    
    def get_appointment(self):
        return self.__appointments
    
    def add_appointment(self,patient):
        self.__appointments.append(patient)

    def patient_count(self):
        return len(self.__patients)


    def doctor_info(self):
        return f'{self.get_first_name()} {self.get_surname()}'
        
