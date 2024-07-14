def main():
    strength = int(input("Strength stat? (number) >>> "))
    buffIn = input("Strength stat buff? (y/n) >>> ")

    if buffIn == "y" or buffIn == "Y":
        buff = int(input("Buff percentage? (number 1-100) >>> ")) / 100
    else:
        buff = 0
    
    defense = int(input("Enemy defense stat? (number) >>> "))
    defBuffIn = input("Enemy defense buff? (y/n) >>> ")
    
    if defBuffIn == "y" or defBuffIn == "Y":
        defBuff = int(input("Buff percentage? (number 1-100) >>> ")) / 100
    else:
        defBuff = 0
    
    power = int(input("Attack power? (e.g: 50. If it is 25x2 for example then run this twice) >>> "))
    critIn = input("Crit? (y/n) >>> ")
    
    if critIn == "y" or critIn == "Y":
        crit = 1.5
    else:
        crit = 1
    
    guardIn = input("Opponent guarding? (y/n) >>> ")
    
    if guardIn == "y" or guardIn == "Y":
        guard = 0.5
    else:
        guard = 1
    
    buffAtk = strength * buff
    buffDef = defense * defBuff
    
    result = ((((strength + buffAtk) * 0.5) - ((defense + buffDef) * 0.25) + (power * 0.5)) * crit) * guard
    
    minimum = result - (result * 0.1)
    maximum = result + (result * 0.1)
    
    yw3 = input("Standing on front tile? (YW3 only, select 'n' otherwise) (y/n) >>> ")
    if yw3 == "y" or yw3 == "Y":
        tile = 1.1
    else:
        tile = 1
    
    print("\nMinumum: " + str(minimum * tile))
    print("\nMaximum: " + str(maximum * tile))
    input("\n\nPress Enter to exit...")

main()