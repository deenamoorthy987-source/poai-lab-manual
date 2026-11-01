#Ex No : 8 IMPLEMENTATION OF FORWARD CHAINING

#A medical expert system stores the following rules:
#if a patient has fever and coughm then the patient has fule.
#if a patient ha fluwm then prescribe medicine.
#Ravi has fever.
#Ravi has cough.
#write a Python program to implement Forward Chaining.


print("MEDICAL EXPERT SYSTEM - FORWARD CHAINING\n")

patient=input("Enter Patient Name:")

fever=input("Dose the patient has Fever ? (yes/no): ").lower()

cough=input("Dose the patient has Cough ? (yes/no): ").lower()

print("\n Applying Rules...\n")

if fever=="yes" and cough=="yes":
  flu=True
  print(patient,"has flu")

if flu:
  medicine=True

else:
  medicine=False


if medicine:
  print(patient,"has Flu")
  print("Medicine should be prescribed")

else:
  print("Medicine cannot be prescribed")


#OUTPUT
#SAMPLE INPUT:
#Enter Patien Name : Ravi
#Does the patient have Fever? (yes/no) : yes
#Done the patient have Cough? (yes/no) : yes

#SAMPLE OUTPUT:
#Applying RUles...

# Ravi has fule
# Medice should be Prescribed


