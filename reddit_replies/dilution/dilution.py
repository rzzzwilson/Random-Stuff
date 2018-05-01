print("\n\nWelcome to the Dilution Helper!")

stock_conc = float(input("\nStock concentration (M): "))
min_conc = float(input("\nMinimum concentration (M): "))
max_conc = float(input("\nMaximum concentration (M): "))
num_std = int(input("\nNumber of standards: "))
vol_std = int(input("\nVolume of standards (mL): "))

# we don't really need *numbered* standards, we only need to know how many
# (ie, num_std).  see below
#standards = list(range(1, num_std + 1 ))
#print ("Standards: ")
#print(standards)

step_size = (max_conc - min_conc)/(num_std - 1)
print ("\nStep size (M): ")
print(step_size)

#std_concentrations = []
#for standard in standards:
#    std_concentration = min_conc + (standard - 1)*step_size
#    std_concentrations.append(std_concentration)
#    std_concentrations_round = [ round(std_concentration, 10) for  std_concentration in std_concentrations]
#    print ("\nStandard concentrations (M)")
#    print(std_concentrations_round)

# just generate the concentrations starting at minimum and adding step_size
# less chance of error with less code, and you don't need to compute 'standards'
std_concentrations = [min_conc + i*step_size for i in range(num_std)]
print ("\nStandard concentrations (M)")
print(std_concentrations)

# as long as your string is inside some sort of 'grouping' construct
# (parentheses here) you can do this to shorten lines
answer = input("\nVary the volume of the stock solution (V) or perform a "
               "series dilution where the previous standard is used a "
               "stock solution (S)? ").upper()

# shorten some names here, very similar names like 'stock_volumes' and
# 'stock_volume' is just asking for trouble!
if answer == "V":
    stock_volumes = []
    for std_con in std_concentrations:
        stock_vol = (std_con*vol_std)/stock_conc
        stock_volumes.append(stock_vol)

    # it's confusing to have a temp variable (stock_volume) with the same name
    # as another variable.  inside a generator or loop temp names can be short.
    # plus, it can be done once outside the 'if' statement
    #stock_volumes_round = [round(s, 3) for s in stock_volumes]
    #print("\nStock Volumes (mL)")
    #print(stock_volumes_round)
    #print("\n")
else:
    stock_volumes = []
    for std_con in reversed(std_concentrations):
        #stock_concs = std_con      # not used anywhere
        stock_vol = (std_con*vol_std)/stock_conc
        stock_volumes.append(stock_vol)

    #stock_volumes_round = [round(s, 3) for s in stock_volumes]
    #print("\nStock Volumes (mL)")      # do it once outside the 'if'
    #print(stock_volumes_round)
    #print("\n")

stock_volumes_round = [round(s, 3) for s in stock_volumes]
print("\nStock Volumes (mL)")
print(stock_volumes_round)
print("\n")

