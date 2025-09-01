class User:
    def __init__(self, username, password, role="nurse"):
        self.username = username
        self.password = password  # Storing password as plain text for simplicity
        self.role = role  # Role can be 'doctor' or 'nurse'

    def verify_password(self, password):
        return self.password == password  # Simple password comparison

class Patient:
    def __init__(self, patient_id, name, age, gender, diagnosis):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis

    def to_string(self):
        """Return patient details as a string for easy saving to a file."""
        return f"{self.patient_id}:{self.name}:{self.age}:{self.gender}:{self.diagnosis}"

class EHealthSystem:
    def __init__(self):
        self.users = {}  # Dictionary to store users by username
        self.patients = {}  # Dictionary to store patients by patient_id
        self.logged_in_user = None
        self.load_users()
        self.load_patients()

    def load_users(self):
        """Load users from a text file."""
        try:
            with open("users.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(":")
                    if len(parts) == 3:
                        username, password, role = parts
                    elif len(parts) == 2:
                        username, password = parts
                        role = "nurse"  # default role if missing
                    else:
                        continue  # skip malformed lines
                    self.users[username] = User(username, password, role)
        except FileNotFoundError:
            pass  # If the file doesn't exist, start with an empty user list

    def save_users(self):
        """Save users to a text file."""
        with open("users.txt", "w") as file:
            for user in self.users.values():
                file.write(f"{user.username}:{user.password}:{user.role}\n")

    def load_patients(self):
        """Load patients from a text file."""
        try:
            with open("patients.txt", "r") as file:
                for line in file:
                    patient_id, name, age, gender, diagnosis = line.strip().split(":")
                    self.patients[int(patient_id)] = Patient(
                        int(patient_id), name, int(age), gender, diagnosis
                    )
        except FileNotFoundError:
            pass  # If the file doesn't exist, start with an empty patient list

    def save_patients(self):
        """Save patients to a text file."""
        with open("patients.txt", "w") as file:
            for patient in self.patients.values():
                file.write(f"{patient.to_string()}\n")

    def signup(self, username, password, role):
        """Sign up a new user (stores in text file)."""
        if username in self.users:
            print("Username already exists. Try a different one.")
        else:
            self.users[username] = User(username, password, role)
            self.save_users()
            print(f"User {username} signed up successfully as {role}!")

    def login(self, username, password, role):
        """Log in an existing user (checks data in memory)."""
        user = self.users.get(username)
        if user and user.verify_password(password) and user.role == role:
            self.logged_in_user = user
            print(f"Login successful! Welcome, {username} ({role}).")
        else:
            print("Invalid username, password, or role.")

    def add_patient(self, name, age, gender, diagnosis):
        patient_id = len(self.patients) + 1
        patient = Patient(patient_id, name, age, gender, diagnosis)
        self.patients[patient_id] = patient
        self.save_patients()
        print(f"Patient {name} added successfully with ID {patient_id}.")

    def view_patients(self):
        if not self.patients:
            print("No patients available.")
        else:
            for patient in self.patients.values():
                print(f"ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}, Gender: {patient.gender}, Diagnosis: {patient.diagnosis}")

    def search_patient_by_id(self, patient_id):
        patient = self.patients.get(patient_id)
        if patient:
            print(f"Patient Found: ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}, Gender: {patient.gender}, Diagnosis: {patient.diagnosis}")
        else:
            print(f"Patient with ID {patient_id} not found.")

    def update_patient(self, patient_id, name=None, age=None, gender=None, diagnosis=None):
        patient = self.patients.get(patient_id)
        if patient:
            if name:
                patient.name = name
            if age:
                patient.age = age
            if gender:
                patient.gender = gender
            if diagnosis:
                patient.diagnosis = diagnosis
            self.save_patients()
            print(f"Patient ID {patient_id} updated successfully.")
        else:
            print(f"Patient with ID {patient_id} not found.")

    def search_patient_by_name(self, name):
        found = False
        for patient in self.patients.values():
            if name.lower() in patient.name.lower():
                found = True
                print(f"ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}, Gender: {patient.gender}, Diagnosis: {patient.diagnosis}")
        if not found:
            print(f"No patients found with the name '{name}'.")

def login_signup_menu(system):
    while True:
        print("\n--- Select Role ---")
        role = ""
        while role not in ["doctor", "nurse"]:
            role = input("Enter role (doctor/nurse): ").lower()
            if role not in ["doctor", "nurse"]:
                print("Invalid role. Please enter 'doctor' or 'nurse'.")

        print("\n--- Login / SignUp ---")
        print("1. Signup")
        print("2. Login")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            system.signup(username, password, role)
            break
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            system.login(username, password, role)
            if system.logged_in_user:
                break
        else:
            print("Invalid choice, please select 1 or 2.")

def main_menu(system):
    while True:
        print("\n--- E-Health System ---")
        if system.logged_in_user:
            print(f"Logged in as: {system.logged_in_user.username} ({system.logged_in_user.role})")
        else:
            print("You are not logged in.")

        if system.logged_in_user:
            user_role = system.logged_in_user.role
            if user_role == "doctor":
                print("1. View All Patients")
                print("2. Search Patient by ID")
                print("3. Search Patient by Name")
                print("4. Logout")
                print("5. Exit")
                choice = input("Enter your choice: ")

                if choice == '1':
                    system.view_patients()
                elif choice == '2':
                    patient_id = int(input("Enter patient ID: "))
                    system.search_patient_by_id(patient_id)
                elif choice == '3':
                    name = input("Enter patient name to search: ")
                    system.search_patient_by_name(name)
                elif choice == '4':
                    system.logged_in_user = None
                    print("Logged out successfully.")
                elif choice == '5':
                    print("Exiting system.")
                    break
                else:
                    print("Invalid choice. Please try again.")

            elif user_role == "nurse":
                print("1. Add New Patient")
                print("2. View All Patients")
                print("3. Search Patient by ID")
                print("4. Update Patient Record")
                print("5. Logout")
                print("6. Exit")
                choice = input("Enter your choice: ")

                if choice == '1':
                    name = input("Enter patient name: ")
                    age = int(input("Enter patient age: "))
                    gender = input("Enter patient gender: ")
                    diagnosis = input("Enter patient diagnosis: ")
                    system.add_patient(name, age, gender, diagnosis)
                elif choice == '2':
                    system.view_patients()
                elif choice == '3':
                    patient_id = int(input("Enter patient ID: "))
                    system.search_patient_by_id(patient_id)
                elif choice == '4':
                    patient_id = int(input("Enter patient ID to update: "))
                    if patient_id not in system.patients:
                        print(f"Patient with ID {patient_id} not found.")
                        continue
                    print("Leave fields blank to keep the current value.")
                    name = input(f"Enter new name (current: {system.patients[patient_id].name}): ")
                    age_input = input(f"Enter new age (current: {system.patients[patient_id].age}): ")
                    age = int(age_input) if age_input else None
                    gender = input(f"Enter new gender (current: {system.patients[patient_id].gender}): ")
                    diagnosis = input(f"Enter new diagnosis (current: {system.patients[patient_id].diagnosis}): ")
                    system.update_patient(patient_id,
                                          name if name else None,
                                          age,
                                          gender if gender else None,
                                          diagnosis if diagnosis else None)
                elif choice == '5':
                    system.logged_in_user = None
                    print("Logged out successfully.")
                elif choice == '6':
                    print("Exiting system.")
                    break
                else:
                    print("Invalid choice. Please try again.")
            else:
                print(f"Unknown user role: {user_role}. Logging out for safety.")
                system.logged_in_user = None
        else:
            login_signup_menu(system)

if __name__ == "__main__":
    system = EHealthSystem()
    main_menu(system)
