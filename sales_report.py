"""Generate sales report showing total melons each salesperson sold."""


salespeople = [] # tool to pull each salesperson to return data
melons_sold = [] # same as above for total melon sold

f = open('sales-report.txt') # opens the file to the sales_report

for line in f: # this will loop over the sale report to create a list out of each line
    line = line.rstrip() #takes away whitespace (to the right) on each line of sale
    entries = line.split('|') # splits each line by the divider into a list
    salesperson = entries[0] # identifies who sold the melons
    melons = int(entries[2]) # identifies  how many melons were sold by that person

    if salesperson in salespeople: # if the sales person is already in salespeople, add the number of melons sold to their total melons sold
        position = salespeople.index(salesperson) #find the index that the salesperson is at and:
        melons_sold[position] += melons             # add that to the identical index number from melons_sold
        
    else: # if the sales person isn't in the salespeople list, add the persons name and melons of the sale to the list
        salespeople.append(salesperson)
        melons_sold.append(melons)

# loop over the indices in salespeople and print out coordinating total sold melons. This is beacuse the lists are acting as parallel lists, so the indices match per person
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')