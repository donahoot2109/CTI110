# CTI-110
# M3HW2 - Software Sales
# Timothy Donahoo
#13SEP2017

# A simple program using main()

def main():
    # This program will give you the total discount per packages bought over 10.
    packages = int(input ('Enter the number of packages'  + \
                                  ' purchased: '))

    # Variables to represent package price and to calculate a percentage of discount
    # of 10 packages or more bought. 
    
    packageRetail = 99
    if  packages < 10:               # Less then 10 packages you will not get a discount
        discount = 0.00
    elif packages < 20:             # 10% discount for packages 10 through 20
        discount = 0.10
    elif packages < 50:             # 20% discount for packages 21 through 49
        discount = 0.20
    elif packages < 100:           # 30% discount for packages 50 through 99
        discount = 0.30
    else:                                                
        discount = 0.40              # 40% discount for packages 100 or more.
        
    # Variables sub-total with discount of packages purchased
    subTotal = packages * packageRetail
    discountRate = discount * subTotal
    total = subTotal - discountRate

    # print dicount and total of purchase
    print ('Invoice: ')
    print ('Amount of discount: $' + format (discountRate, ',.2f')  \
           + '\nTotal amount: $' + format ( total, ',.2f'))

    
    
main ()
    
