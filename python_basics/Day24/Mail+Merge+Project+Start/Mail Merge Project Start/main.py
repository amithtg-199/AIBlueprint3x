#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

invites = []
with open(r"Day24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt") as f:
    n = f.readlines()
    for name in n:
        invites.append(name.strip())

for name in invites:
    with open(r"Day24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r") as f:
        with open(f"Day24/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/{name}_letter.txt", mode = "w") as l:
            l.write(f.read().replace("[name]",name))
