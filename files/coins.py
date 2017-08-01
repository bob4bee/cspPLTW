#Coin project.  User inputs a monetary amount in dollars.  The quantity and type of coints is returned.
amount=raw_input('Enter the monetary amount in dollars: $')
print
#Need to change the input into a float rather than a string.
#Also need to change dollar amount into coinage.
amount=float(amount)*100
#Need to define initial variables and set to zero.
quarters=0
dimes=0
nickels=0
pennies=0
#Calculate the number of quarters in the amount.
while amount>=25:
    quarters +=1
    amount=amount-25
#Calculate the number of dimes in the amount.
while amount>=10:
    dimes +=1
    amount=amount-10
#Calculate the number of nickels in the amount.
while amount>=5:
    nickels +=1
    amount=amount-5
#What remains is the number of pennies.
pennies=int(amount)
#Report the response to the user.
print "Optimally, you should have "+str(quarters)+\
" quarters, "+str(dimes)+\
" dimes, "+str(nickels)+\
" nickels, and "+str(pennies)+\
" pennies."