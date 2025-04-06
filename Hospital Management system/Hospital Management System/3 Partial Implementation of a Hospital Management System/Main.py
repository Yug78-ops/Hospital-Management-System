# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC')]
    discharged_patients = []

    # keep trying to login tell the login details are correct
    while True:
       
       if admin.login():
            running = True
             # allow the program to run
            break
       else:
            print('Incorrect username or password.')

    while running:
        Admin.store_in_file(Admin,patients)
        
        
        
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge a patient')
        print(" 3- View discharged patient's list")
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin details')
        print(" 6- View Patient's list")
        print(" 7- View Patients according to the Family name")
        print(' 8- Add a New Patient')
        print(' 9- Request Management report')
        print(' 10- Rellocate the patient')
        print(' 11- View the raw data from database')
        print(' 12- Quit the system')

        # get the option
        op = input('Option: ')

        if op == '1':
            Admin.doctor_management(Admin,doctors)

        elif op == '2':
            Admin.discharge(Admin,patients,discharged_patients)
            Admin.store_in_file(Admin,patients)

        elif op == '3':
            Admin.view_discharge(Admin,discharged_patients)

        elif op == '4':
            # 4- Assign doctor to a patient
            Admin.assign_doctor_to_patient(Admin, patients, doctors)
            Admin.store_in_file(Admin,patients)

        elif op == '5':
            # 5- Update admin detais
            admin.update_details()
            while True:
                if admin.login():
                    running = True
             # allow the program to run
                    break
            
                else:
                    print('Incorrect username or password.')
        
        elif op == '6':
            Admin.view_patient(Admin,patients)
        
        elif op == "7":
            Admin.view_family(Admin,patients)

        elif op == "8":
            Admin.add_patient(Admin,patients)
            Admin.store_in_file(Admin,patients)

        elif op == "9":
            Admin.management_report(Admin,patients,doctors)
        
        elif op == "10":
            Admin.relocate_patient(Admin,patients,doctors)

        elif op == "11":
             Admin.load_from_file(Admin)
        
        elif op == "12":
            print("You have exited the program.")
            break
        
        else:
            print('Invalid option. Try again')

   
if __name__ == '__main__':
    main()
