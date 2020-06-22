import math


#main goal is to make currency generator
#The inputs will be given

#       1) user input = of currency usd or ....
#       2) user input for number

print("        =============================================",
      
      "             Deafult INR (Indian Rs)"
      "        =============================================" )

print()
print()

print("Please input the currency in capital letters : eg : USD, EUR")
print()
print()
print("        =============================================",
      
      "             Deafult Input in INR (Indian Rs)"
      "        =============================================" )
print()
print()
print("This converter only works for USD, Emirati Dirham, Russian Ruble, Venezuelan Bolivar, Turkish Lira, POUND, Thai baht, EURO/EUR, Riyal, South Korean won, KUWAITI DINAR/DINAR, ")
print('USD')
print('EUR')
print('DINAR')
print('RIYAL')
print('WON')
print('BAHT')
print('POUND')
print('LIRA')
print('BOLIVAR')
print('RUBLE')
print('DIRHAM')

print()
print()
while True:
            
    userinputs= float(input('Please input the INR amount:  '))
    usercurrencys= input('Please enter the currency you want to convert:  ')

    
    if usercurrencys =='USD':
        result_in_input_currency= userinputs * 76.04
        print(result_in_input_currency)
        
    elif  usercurrencys =='EUR':
        result_in_input_currency= userinputs * 85.18
        print(result_in_input_currency)
        
    elif usercurrencys == 'DINAR':
        result_in_input_currency= userinputs * 246.97
        print(result_in_input_currency)
        
    elif usercurrencys == 'RIYAL':
        result_in_input_currency= userinputs * 20.27
        print(result_in_input_currency)
        
    elif usercurrencys == 'WON':
        result_in_input_currency= userinputs * 0.063
        print(result_in_input_currency)
        
    elif usercurrencys == 'BAHT':
        result_in_input_currency= userinputs * 2.45
        print(result_in_input_currency)
        
    elif usercurrencys == 'POUND':
        result_in_input_currency= userinputs * 94.19
        print(result_in_input_currency)
        
    elif usercurrencys == 'LIRA':
        result_in_input_currency= userinputs * 11.09
        print(result_in_input_currency)
        
    elif usercurrencys == 'BOLIVAR':
        result_in_input_currency= userinputs * 0.00038
        print(result_in_input_currency)
        343424
    elif usercurrencys == 'RUBLE':
        result_in_input_currency= userinputs * 1.09
        print(result_in_input_currency)
        
    elif usercurrencys == 'DIRHAM':
        result_in_input_currency= userinputs * 20.70
        print(result_in_input_currency)
    elif usercurrencys =='EXIT':
        exit()
        

    
    