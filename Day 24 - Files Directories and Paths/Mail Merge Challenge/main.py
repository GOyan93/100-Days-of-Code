#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Generates template letter from file.
with open("Input/Letters/starting_letter.txt", mode= "r") as example:
    template = example.read()

# Creates name list from file.
with open("Input/Names/invited_names.txt", mode= "r") as name_list:
    names = name_list.readlines(-1)
    names = [name.rstrip() for name in names]

# Inserts the name into the template per person, resets template at end.
for name in names:
     with open(f"Output/ReadyToSend/{name}'s_letter.txt", mode= "w") as custom_letter:
         template = template.replace("[name]", name)
         custom_letter.write(template)
         with open("Input/Letters/starting_letter.txt", mode="r") as example:
             template = example.read()



