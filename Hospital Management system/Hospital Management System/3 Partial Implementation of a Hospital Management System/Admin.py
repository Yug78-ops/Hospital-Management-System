from Doctor import Doctor
from Patient import Patient
import datetime
import matplotlib.pyplot as plt


class Admin:
    def __init__(self, username, password, address = ''):
        

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        
        print("-----Admin Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        try:
            if username == self.__username and password == self.__password: 
                print('Login successful.')
                return True
        
            else:
                raise Exception("")
                
        except Exception as e:
            print(e)

    
    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        return self.__first_name, self.__surname, self.__speciality
    

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')
        op = input("Input: ")
        

        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctors details:')
            first_name = input('First name: ')
            surname = input ('Surname: ')
            speciality = input('Speciality: ')

            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    name_exists = True

             
            if name_exists == False:
                doctors.append(Doctor(first_name, surname, speciality))
                print('Doctor registered.')

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            print('ID |          Full Name           |  Speciality')
            (self.view(self,doctors))

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(self,doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(self,index,doctors)
                    if doctor_index!=False:
                
                        break
                        
                    else:
                        print("Doctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = int(input('Input: ')) # make the user input lowercase
            if op == 1:
                first_name = input('Enter the new first name: ')
                doctors[index].set_first_name(first_name)

            elif op == 2:
                surname = input('Enter the new surname: ')
                doctors[index].set_surname(surname)
            
            elif op == 3: 
                speciality = input('Enter the new speciality: ')
                doctors[index].set_speciality(speciality)

            print("Doctor's Detail Successfully Updated!")

            

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(self,doctors)

            doctor_index = int(input('Enter the ID of the doctor to be deleted: '))
            if doctor_index <= len(doctors):
                doctors.pop(doctor_index-1)
                print('Doctor Sucessfullt deleted!')
            else:
                print('Invalid ID!')

    
        else:
            print('Invalid operation choosen. Check your spelling!')


    def view_patient(self, patients):
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(self, patients)

       
    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(self,patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures
        if patients[patient_index].get_symptoms()=='Not recorded':
            a = input("The symptoms of this patient is not in records. First plz enter the symptoms:\n==>")
            patients[patient_index].set_symptoms(a)


        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(self,doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(self,doctor_index,doctors):
                
                    
                # link the patients to the doctor and vice versa
                patients[patient_index].link(doctors[doctor_index].full_name())
                doctors[doctor_index].add_patient(patients[patient_index].full_name())
                doctors[doctor_index].add_appointment(patients[patient_index].full_name())
                print('The patient is now assigned to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")

        condition = True
        while condition:
            self.view(self,patients)
            patient_index = int(input('Please enter the patient ID: ')) - 1
            if patient_index in  range(len (patients)):
                    op = input(f'Do you really want to discharge a patient {patients[patient_index].get_first_name()} (Y/N):').lower()
                    if op.lower() == 'y':
                        print(f"{patients[patient_index].get_first_name()} is now discharged")
                        discharge_patients.append(patients.pop(patient_index))
                        break
                    elif op.lower() == 'n':
                        print("Operation Cancelled!")
                        condition = False
                        break
                    else:
                        print("Please answer by Yes or No.")

            else:
                print("Invalid ID. Try Again!")

            
    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(self,discharged_patients)


    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """
        
        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            user_name = input("Enter the new username: ")
            self.__username = user_name
        

        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password

        elif op == 3:
            address = input("Enter the new address: ")
            self.__address = address
            

        else:
            print("Invalid Input!")



    def view_family(self,patients):
        a = input("Input a surname: ")
        family = []
        for patient in patients:
                surname = patient.get_surname()
                if surname == a:
                    family.append(patient)

        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ') 
        self.view(self,family)  


    def add_patient(self,patients):
        print("Enter Details:")
        first_name = input("Enter the first name: ")
        surname = input("Enter the surname: ")
        age = input("Enter the age: ")
        mobile = input("Enter the mobile no: ")
        postcode = input("Enter the postcode: ")
        symptoms = input("Enter the symptoms: ")
        doctor = 'None'
        name_exists = False
        for patient in patients:
                if first_name == patient.get_first_name() and surname == patient.get_surname():
                    print('Name already exists.')
                    name_exists = True

             
        if name_exists == False:
            patients.append(Patient(first_name, surname, age, mobile, postcode, symptoms))
            print('Patient registered.')



    def management_report(self,patients, doctors):
        d_count = 0
        for i in doctors:
            d_count += 1
        print("-------Management Report---------")
        user = input("Input:\na- Total Number of doctors in the system\nb- Ratio of patient per doctor\nc- Total number of appointment per doctor per month\nd- List of patient on the basis of symptoms\n==>").lower()
        
        if user == "a":
            print(f"Total Number of doctors in the system: {d_count}.")
            self.plot_bar_chart(self, x_values=['Doctors'], y_values=[d_count], title="Total Number of Doctors", xlabel="Category", ylabel="Count")

        elif user == "b":
            print(f"--------Patient per doctor-------------")
            doctors_list = []
            patients_count = []
            for i in doctors:
                print(f"Dr.{i.full_name()} =  {len(i.get_patient())} patients")
                doctors_list.append(i.full_name())
                patients_count.append(len(i.get_patient()))
            self.plot_bar_chart(self, x_values=doctors_list, y_values=patients_count, title='Total patients per doctor', xlabel='Name of doctors', ylabel='Number of patients')

        elif user == "c":
            print(f"--------Patient per doctor-------------")
            doctors_list = []
            patients_count = []
            for i in doctors:
                print(f"Dr.{i.full_name()} =  {len(i.get_patient())} patients")
                doctors_list.append(i.full_name())
                patients_count.append(len(i.get_patient()))
            self.plot_bar_chart(self, x_values=doctors_list, y_values=patients_count, title='Total patients per doctor', xlabel='Name of doctors', ylabel='Number of patients')

        elif user == "d":
            symptoms = []
            for i in patients:
                symptoms.append(i.print_symptoms())

            print()
            for sym in set(symptoms):
                print(f'{sym}= {symptoms.count(sym)}')

            unique_symptoms = list(set(symptoms))
            counts = [symptoms.count(sym) for sym in unique_symptoms]
            
            plt.figure(figsize=(8, 5))
            plt.pie(counts, labels=unique_symptoms, autopct='%1.1f%%', 
            colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
            plt.title("Distribution of Patients per Illness Type", fontsize=15)
            plt.show()

        else:
            print("Invalid Input!")


    
    def relocate_patient(self, patients, doctors):
        """
        Allow the admin to re-assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Relocate-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(self, patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                self.store_patients(self, patients=patients)
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms()
        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(self, doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1
            current_doctor = patients[patient_index].get_doctor()
            # check if the id is in the list of doctors
            if current_doctor != 'None':
                for i in doctors:
                    if i.full_name() == current_doctor:
                        if patients[patient_index].full_name() in i.get_patient():
                            i.get_patient().remove(patients[patient_index].full_name())
                            i.get_appointment().remove(patients[patient_index].full_name())
                            
                if self.find_index(self, doctor_index, doctors):
                    patients[patient_index].link(doctors[doctor_index].full_name())
                    doctors[doctor_index].add_patient(patients[patient_index].full_name())
                    doctors[doctor_index].add_appointment(patients[patient_index].full_name())
                    print()
                    print('The patient is relocated to another doctor.')

                else:
                    print('The id entered was not found.')

            else:
                print('This patient has not been assigned to any doctor.')
                print('Please Assign A Doctor First To Be Relocated!!')
                print()

        except ValueError:
            print('The id entered is incorrect')

            
    def store_in_file(self,patients):
        with open("database.txt","w") as w:
            w.write('first_name,last_name, age,ph. no,postcode,symptoms,doctor assigned\n')
            for i in patients:
             w.write(i.patient_info() + "\n")


    def load_from_file(self):
        with open("database.txt","r") as f:
            print("\n")
            for line in f:
                print(line.strip())

    def plot_bar_chart(self,x_values, y_values, title, xlabel, ylabel):
    #   plt.figure(figsize=(8, 5))
      plt.bar(x_values, y_values, width= 0.5,color='pink', edgecolor = 'black')
      plt.xlabel(xlabel,fontsize = 15)
      plt.ylabel(ylabel,fontsize = 15)
      plt.title(title,fontsize = 20)
    #   plt.style.use('seaborn-pastel')
      plt.show()

            
        


    

        



   
    
       
                  
       



        

