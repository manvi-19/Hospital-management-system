class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def remove_patient(self, patient):
        self.patients.remove(patient)


class Patient:
    def __init__(self, name, medical_history):
        self.name = name
        self.medical_history = medical_history
        self.doctors = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def remove_doctor(self, doctor):
        self.doctors.remove(doctor)


class Hospital:
    def __init__(self):
        self.doctors = []
        self.patients = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def remove_doctor(self, doctor):
        self.doctors.remove(doctor)

    def add_patient(self, patient):
        self.patients.append(patient)

    def remove_patient(self, patient):
        self.patients.remove(patient)


def manage_appointments():
    # Functionality to manage appointments
    class Appointment:
        def __init__(self, patient, doctor, date, time):
            self.patient = patient
            self.doctor = doctor
            self.date = date
            self.time = time

    class Hospital:
        def __init__(self):
            self.appointments = []

        def add_appointment(self, appointment):
            self.appointments.append(appointment)
            print("Appointment added successfully.")

        def remove_appointment(self, appointment):
            self.appointments.remove(appointment)
            print("Appointment removed successfully.")

        def get_appointments_by_patient(self, patient):
            patient_appointments = []
            for appointment in self.appointments:
                if appointment.patient == patient:
                    patient_appointments.append(appointment)
            return patient_appointments

        def get_appointments_by_doctor(self, doctor):
            doctor_appointments = []
            for appointment in self.appointments:
                if appointment.doctor == doctor:
                    doctor_appointments.append(appointment)
            return doctor_appointments

    def manage_appointments(hospital):
        while True:
            print("\nAppointment Management")
            print("1. Schedule an appointment")
            print("2. Cancel an appointment")
            print("3. View appointments by patient")
            print("4. View appointments by doctor")
            print("0. Go back")
            choice = input("Enter your choice: ")
            if choice == "1":
                patient = input("Enter patient's name: ")
                doctor = input("Enter doctor's name: ")
                date = input("Enter date (e.g., DD/MM/YYYY): ")
                time = input("Enter time (e.g., HH:MM AM/PM): ")
                appointment = Appointment(patient, doctor, date, time)
                hospital.add_appointment(appointment)
            elif choice == "2":
                patient = input("Enter patient's name: ")
                doctor = input("Enter doctor's name: ")
                date = input("Enter date (e.g., DD/MM/YYYY): ")
                time = input("Enter time (e.g., HH:MM AM/PM): ")
                found_appointment = None
                for appointment in hospital.appointments:
                    if (
                            appointment.patient == patient
                            and appointment.doctor == doctor
                            and appointment.date == date
                            and appointment.time == time
                    ):
                        found_appointment = appointment
                        break
                if found_appointment:
                    hospital.remove_appointment(found_appointment)
                else:
                    print("Appointment not found.")
            elif choice == "3":
                patient = input("Enter patient's name: ")
                patient_appointments = hospital.get_appointments_by_patient(patient)
                if patient_appointments:
                    print("Appointments for patient", patient)
                    for appointment in patient_appointments:
                        print("Doctor:", appointment.doctor)
                        print("Date:", appointment.date)
                        print("Time:", appointment.time)
                        print("-------------------------")
                else:
                    print("No appointments found for patient", patient)
            elif choice == "4":
                doctor = input("Enter doctor's name: ")
                doctor_appointments = hospital.get_appointments_by_doctor(doctor)
                if doctor_appointments:
                    print("Appointments for doctor", doctor)
                    for appointment in doctor_appointments:
                        print("Patient:", appointment.patient)
                        print("Date:", appointment.date)
                        print("Time:", appointment.time)
                        print("-------------------------")
                else:
                    print("No appointments found for doctor", doctor)
            elif choice == "0":
                break
            else:
                print("Invalid choice.")

    def main():
        hospital = Hospital()
        manage_appointments(hospital)

    if __name__ == "__main__":
        main()


def manage_doctors(hospital):
    # Functionality to manage doctors
    print("Managing doctors...")
    while True:
        choice = input("Enter 1 to add a doctor, 2 to remove a doctor, or 0 to go back: ")
        if choice == "1":
            name = input("Enter doctor's name: ")
            specialty = input("Enter doctor's specialty: ")
            doctor = Doctor(name, specialty)
            hospital.add_doctor(doctor)
            print("Doctor added successfully.")
        elif choice == "2":
            name = input("Enter doctor's name: ")
            for doctor in hospital.doctors:
                if doctor.name == name:
                    hospital.remove_doctor(doctor)
                    print("Doctor removed successfully.")
                    break
            else:
                print("Doctor not found.")
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


def manage_patients(hospital):
    # Functionality to manage patients
    print("Managing patients...")
    while True:
        choice = input("Enter 1 to add a patient, 2 to remove a patient, or 0 to go back: ")
        if choice == "1":
            name = input("Enter patient's name: ")
            medical_history = input("Enter patient's medical history: ")
            patient = Patient(name, medical_history)
            hospital.add_patient(patient)
            print("Patient added successfully.")
        elif choice == "2":
            name = input("Enter patient's name: ")
            for patient in hospital.patients:
                if patient.name == name:
                    hospital.remove_patient(patient)
                    print("Patient removed successfully.")
                    break
            else:
                print("Patient not found.")
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


def main():
    hospital = Hospital()
    while True:
        print("\nHospital Management System")
        print("1. Manage Appointments")
        print("2. Manage Doctors")
        print("3. Manage Patients")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            manage_appointments()
        elif choice == "2":
            manage_doctors(hospital)
        elif choice == "3":
            manage_patients(hospital)
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
