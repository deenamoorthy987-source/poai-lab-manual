#EX No: 7 Implementation of Backward Chaining

#Write a Pyhton progrom for backwards chaining for the foloowing: "As per the law, it is a crime for an American to sell weapons to hostile nations."
#Count A, an enemy of America, has some missilesm and all the missiles were sold to it by Robert, who is an American Citizen." Prove that "Robert is criminal"

print("BACKWARD CHAINING")

print("\nEnter the facts (Yes/No)\n")

facts = {}

facts["American"] = input("Is Robert an American? (yes/no): ").lower()
facts["Missile"] = input("Is M1 a Missile? (yes/no): ").lower()
facts["Enemy"] = input("Is CountryA an Enemy of America? (yes/no): ").lower()
facts["Sell"] = input("Did Robert sell M1 to CountryA? (yes/no): ").lower()

def prove(goal):

    if goal == "Criminal":
        
        print("\nGoal : Criminal(Robert)")
        
        return (prove("American") and 
                prove("Weapon") and 
                prove("Hostile") and 
                prove("Sell"))

    elif goal == "American":
        print("Checking American")
        return facts["American"] == "yes"

    elif goal == "Weapon":
        print("Need Weapon(M1)")
        return prove("Missile")

    elif goal == "Missile":
        print("Checking Missile")
        return facts["Missile"] == "yes"

    elif goal == "Hostile":
        print("Need Hostile(CountryA)")
        return prove("Enemy")

    elif goal == "Enemy":
        print("Checking Enemy")
        return facts["Enemy"] == "yes"

    elif goal == "Sell":
        print("Checking Sell")
        return facts["Sell"] == "yes"

    return False

if prove("Criminal"):
    print("\nConclusion")
    print("Robert is Criminal")
else:
    print("\nConclusion")
    print("Cannot prove Robert is Criminal")


#OUTPUT:
#Sample Input:
#Is Robert an American? (yes/no) : yes
#Is M1 a Missile? (yes/no) : yes
#Is CountryA an Enemy of America? (yes/no):
#yes

#SAMPLE OUTPUT:  
#Goal: Criminal(Robert)
#checking American
#Need Weapon(M1)
#Checking Missile
#need Hostile (Country A)
#Checking Enemy
#Checking Sell
#Robert is Criminal
