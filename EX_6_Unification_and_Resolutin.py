#Ex. No. 6 Implementation of Unification and Resolution Algorithm

#UNIFICATION Program

#Write a Python program to mplement the Unification algorithm for first-order predicate logic. The program shoul accept two predicates as input and determime whether they can be unified.
#If successful, display the substitution set; otherwisem display "Unification Failed".

def unify(predicate1, predicate2):

    predicate1 = predicate1.replace(" ", "")
    predicate2 = predicate2.replace(" ", "")

    p1 = predicate1.split("(")[0]
    p2 = predicate2.split("(")[0]

    if p1 != p2:
        return "Unification Failed"

    arg1 = predicate1[predicate1.find("(")+1:predicate1.find(")")].split(",")
    arg2 = predicate2[predicate2.find("(")+1:predicate2.find(")")].split(",")

    if len(arg1) != len(arg2):
        return "Unification Failed"

    substitution = {}

    for a, b in zip(arg1, arg2):

        if a.isupper() and b.isupper():
            if a != b:
                substitution[a] = b

        elif a.isupper():
            substitution[a] = b

        elif b.isupper():
            substitution[b] = a

        elif a != b:
            return "Unification Failed"

    return substitution


predicate1 = input("Enter Predicate 1 : ")
predicate2 = input("Enter Predicate 2 : ")

result = unify(predicate1, predicate2)

print("\nResult")
print(result)


# Sample Input 1
# Enter Predicate 1 : likes(X,apple)
# Enter Predicate 2 : likes(John,apple)

# Output
# Result
# {'X': 'John'}


# Sample Input 2
# Enter Predicate 1 : parent(X,Y)
# Enter Predicate 2 : parent(Ram,Shyam)

# Output
# Result
# {'X': 'Ram', 'Y': 'Shyam'}


# Failure Case
# Enter Predicate 1 : likes(X,apple)
# Enter Predicate 2 : hates(John,apple)

# Output
# Result
# Unification Failed

#==============================================================================================================================


#RESOLUTION PROGRAM

#Write a Python program to perform logical inference using the Resolution Principle for an Intelligent Traffic Management System and genetrate the corresponding resolvent.

print("Traffic Rule Resolution")

print("\nTraffic Symbols")
print("P : Traffic Signal is RED")
print("Q : Vehicles must STOP")
print("R : Emergency Vehicle is Allowed")

print("\nEnter the Traffic Clauses")

clause1 = set(input("Enter Clause 1 : ").split())
clause2 = set(input("Enter Clause 2 : ").split())

resolvent = set()

for literal in clause1:

    # Find complement
    if literal.startswith("~"):
        complement = literal[1:]
    else:
        complement = "~" + literal

    if complement in clause2:

        # Apply Resolution
        resolvent = (clause1 - {literal}) | (clause2 - {complement})

        break

print("\nResolvent")
print(resolvent)



#OUTPUT
#SAMPLE INPUT:
#Traffic Rule Resolution
#Traffic Symbols

#P : Traffic Signal is RED
#Q : Vehicles must STOP
#R : Emergency Vehicle is Allowed

#Enter the Traffic Clauses
#Enter Clauses 1 : P Q
#Enter Clauses 2 : ~Q R

#SAMPLE OUTPUT:
#Resolvent
#{'P','R'}

