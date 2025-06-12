DB = ["looks", "swims", "quacks"]  # A set of facts
KB = [(["looks", "swims", "quacks"], "duck"), (["barks"], "dog"), (["hoots", "flies"], "owl")]  # A set of rules

count = 1  # Number of times we have iterated over the whole rule set
changes = True

while changes:
    changes = False  # Set the flag that there have been no changes to false
    print("Starting iteration " + str(count))
    
    for p in KB:  # For each rule in the set of rules ...
        antecedent, consequent = p
        print("Consider a rule where:")
        print(antecedent)
        print("implies:")
        print(consequent)
        
        # Determine if all literals in antecedent are also in DB
        satisfied = True  # Flag for entire premise being satisfied
        for q in antecedent:
            # q will be a string
            # DB is a list of strings
            if q not in DB:
                satisfied = False  # Flag as false, all clauses must be inferred
        
        # If it passes the above, then antecedent is satisfied
        # ...and consequent should be entailed
        if satisfied and consequent not in DB:
            DB.append(consequent)
            changes = True
            print("Antecedent is in DB, consequent is implied, DB is now:")
            print(DB)
        elif satisfied and consequent in DB:
            print("Consequent is implied, but was already in DB")
        else:
            print("Consequent is not implied")
    
    count = count + 1

print("No more changes. DB is:")
print(DB)

