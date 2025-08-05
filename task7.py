# Changing the guest list : You just heard that one of your guests can't make the dinner, so you need
# to send out a new set of invaitation. You will have to think of someone else to ivite

#   Modify your list, replacing the name of the guest who can't make it with the name of the new person
#   you are inviting 

#   Print a second set of invaition message, one for each person who is still in your list

#   Create a list of guest

guest = ["Mushtaq","Hamza","Ahsan"]

#   Create a variable of guest

guest_not_attend = "Hamza"

#   replace the guest with new one

new_guest = "Umar"

index = guest.index(guest_not_attend)

guest[index] = new_guest

#   Print a new message 

for i in guest:
    print(i,"Your are still invited to a dinner")
