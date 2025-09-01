# Hospital-Management-System



## 📌 Overview
The **E-Health System** is a **Python-based console application** designed to manage patients' records with **role-based access control**. It supports two roles:
- **Doctor** – Can view and search patient details.
- **Nurse** – Can add, view, update, and search patient details.

The system uses **text files** (`users.txt` and `patients.txt`) for persistent storage of users and patients.

---

## ✅ Features
### **Authentication & Authorization**
- **Signup & Login** with role (`doctor` or `nurse`).
- Role-based menus and permissions.

### **Doctor Role**
- View all patients.
- Search patients by **ID** or **Name**.

### **Nurse Role**
- Add new patients.
- View all patients.
- Search patients by **ID**.
- Update patient records.

### **Common Features**
- Persistent storage using `users.txt` and `patients.txt`.
- Input validation for roles and menu options.

---

## 🗂️ File Structure
```
EHealthSystem/
│
├── e_health_system.py       # Main application file (your code)
├── users.txt                # Stores user credentials and roles
├── patients.txt             # Stores patient details
└── README.md                # Project documentation
```

---

## ⚙️ How It Works
1. **Run the program**:
   ```bash
   python e_health_system.py
   ```
2. **Select a role** (`doctor` or `nurse`).
3. **Login** or **Sign up**:
   - Signup creates a new user in `users.txt`.
   - Login validates against saved users.
4. **Access the role-based menu**:
   - **Doctor** → View/Search patients.
   - **Nurse** → Add/View/Update/Search patients.

---

## 🧑‍💻 Classes & Responsibilities
### **1. User**
- Stores `username`, `password`, and `role`.
- Provides password verification.

### **2. Patient**
- Stores patient details (`id`, `name`, `age`, `gender`, `diagnosis`).
- Converts patient details to string for file storage.

### **3. EHealthSystem**
- Manages:
  - Users (`signup`, `login`, save/load from `users.txt`).
  - Patients (`add`, `view`, `search`, `update`, save/load from `patients.txt`).
- Handles **role-based menus**.

---

## 📂 Data Storage Format
### **users.txt**
```
username:password:role
```
Example:
```
john123:pass123:doctor
nurse01:nursepass:nurse
```

### **patients.txt**
```
patient_id:name:age:gender:diagnosis
```
Example:
```
1:Alice:30:Female:Flu
2:Bob:45:Male:Diabetes
```

## ▶️ Example Usage
```
--- Select Role ---
Enter role (doctor/nurse): nurse

--- Login / SignUp ---
1. Signup
2. Login
Enter your choice: 1
Enter username: nurse01
Enter password: nursepass
User nurse01 signed up successfully as nurse!

--- E-Health System ---
Logged in as: nurse01 (nurse)
1. Add New Patient
2. View All Patients
3. Search Patient by ID
4. Update Patient Record
5. Logout
6. Exit
```

---


---

## 🛠️ Requirements
- Python 3.x
- No external libraries required.

