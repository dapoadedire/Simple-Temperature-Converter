

print("This is a Temperature Converter App")

should_continue = True


while should_continue == True:



      print()
      print()
      
      print("Which temperature unit do you want to convert? \nInput C for Celsius, \nK for Kelvin,\nF for Fahrenheit")
      convert_from = input()
      print()
      print()
     
      
      print("Which temperature unit do you want to convert to? \nInput C for Celsius,\nK for Kelvin,\nF for Fahrenheit ")
      convert_to = input()
      
      print()
      print()
      
       





#Fahrenheit to Celsius 

      if (convert_from == "F" and convert_to == "C" ): 
         
           print("Cool, let's get started. \nYou want to convert from FAHRENHEIT to CELSIUS ")
           
           print()
           Fahr = float(input('Input temperature in Fahrenheit = '))
           Cels = (Fahr - 32) * 5 / 9
  
           Cels3 = "{:.3f}". format(Cels) 
           Cels = float(Cels3)
 
           print('Tempearture in Celsius = ' + str(Cels))
 
# Fahrenheit to Kelvin 


      elif (convert_from == "F" and convert_to == "K" ): 
           print("Good, let's get started. \nYou want to convert from FAHRENHEIT to KELVIN ") 
           print()
           FAHr = float(input('Input temperature in Fahrenheit = '))
           KELv = (FAHr - 32) * 5 / 9 + 273.15
  
           KELv3 = "{:.3f}". format(KELv) 
           KELv = float(KELv3)
  
           print('Tempearture in Kelvin = ' + str(KELv))

  
# Kelvin to Celsius 

      elif (convert_from == "K" and convert_to == "C" ): 
           print("Good, let's get started. \nYou want to convert from Kelvin to Celcius") 
           print()
           kelv = float(input('Input temperature in Kelvin = '))
           cELS = kelv - 273.15
  
           cELS3 = "{:.3f}". format(cELS) 
           cELS = float(cELS3)
  
           print('Tempearture in Celsius = ' + str(cELS))


# Kelvin to Fahrenheit 

      elif (convert_from == "K" and convert_to == "F" ): 
           print("Good, let's get started. \nYou want to convert from Kelvin to Fahrenheit ") 
  
           print()
           Kelv = float(input('Input temperature in Kelvin = '))
           fahr = (Kelv - 273.15) * 9 / 5 + 32

           fahr3 = "{:.3f}". format(fahr) 
           fahr = float(fahr3)
           print('Tempearture in Fahrenheit = ' + str(fahr))

# Celsius to Fahrenheit 

      elif (convert_from == "C" and convert_to == "F" ): 
           print("Good, let's get started. \nYou want to convert from Celcius to Fahrenheit ") 
           print()
           cels = float(input('Input temperature in Celsius = '))
           fahr = (cels * 9 / 5) + 32

           fahr3 = "{:.3f}". format(fahr) 
           fahr = float(fahr3)
  
           print('Tempearture in Fahrenheit = ' + str(fahr))

# Celsius to Kelvin 

      elif (convert_from == "C" and convert_to == "K" ): 
           print("Good, let's get started. \nYou want to convert from Celsius to Kelvin") 
           print()
           CELS = float(input('Input temperature in Celsius = '))
           KELV = CELS + 273.15
  
           KELV3 = "{:.3f}". format(KELV) 
           KELV = float(KELV3)
  
           print('Tempearture in Kelvin = ' + str(KELV))
    
    
 
      
      else: 
           print("You have entered the wrong command.")
    
       
      print()
      print()
      print()
      
      
          
      run_again = input("Dear user, do you still want to convert? \nYes or No?")
      
      if run_again == "No": 
         should_continue = False
          
              
      
       
  
