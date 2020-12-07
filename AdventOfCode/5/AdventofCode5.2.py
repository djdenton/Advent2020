import csv,re

# Plane is 128 deep and 8 wide
# Numbering is 0 to 127 and 0 to 7
# Create a 2D array of seats on the aeroplane
depth = 128
width = 8
seats = [[[i,j] for j in range(width)] for i in range(depth)]

# Function to halve array based on the 
def halve_plane(seats,letter):
    half = len(seats)//2
    if letter in ['F','L']:
        return seats[:half]
    else:
        return seats[half:]

    
with open('input.txt') as csvfile:
    tickets = list(csv.reader(csvfile))
    tickets = [t[0] for t in tickets if re.search('[FB]{7}[RL]{3}',t[0])] #Remove any incorrect tickets  

    #tickets = ['BFFFBBFRRR','FFFBBBFRRR','BBFFBBFRLL']
    ticket_numbers = []
    highest = 0
    for ticket in tickets:
        seats_temp = seats
        # Find row
        for i in range(7):
            seats_temp = halve_plane(seats_temp, ticket[i])

        # Find seat
        seats_temp = seats_temp[0]    
        for i in range(3):
            seats_temp = halve_plane(seats_temp, ticket[i+7])

        
        seat = seats_temp[0][0] * 8 + seats_temp[0][1]
        ticket_numbers.append(seat)
        ticket_numbers.sort()

    all_tickets = [i for i in range(820)]
    print(set(all_tickets) - set(ticket_numbers)) # This is very lazy
 
