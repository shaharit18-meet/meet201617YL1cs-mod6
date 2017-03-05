#Module 6, Part 5: Practice with dictionaries here


my_phonebook={"Statue of Liberty":2125555555, "Ghostbusters":2125551234}

###
#Assign the value of the Statue of Liberty's phone number to the variable, num
num= my_phonebook["Statue of Liberty"]
###

###
#Print the variable, num
print(num)
###

###
#Change the value of the Ghostbusters' phone number to 2125559876
###
my_phonebook["Ghostbusters"]= 2125559876

#Here's an empty dictionary
your_phonebook={}

###
#Add 5 values to it like this
#your_phonebook['key']=value
your_phonebook['mom']=74782347
your_phonebook['dad']=7648562349
your_phonebook['grandma']=75349692
your_phonebook['grandpa']=84705723
your_phonebook['someone else']=476520348570
###

###
#Use the keys() method: your_phonebook.keys()
#It will produce a sequence of all the keys

#Loop over this sequence with a for loop
#using syntax like
sequence_of_keys= your_phonebook.keys()
for key in sequence_of_keys:
    
    print(key+"=" + str(your_phonebook[key]))



#Use the loop to print to the shell the key and value
#of every element in the dictiona
