temp = int(input("What is the temperature outside?: "))

# if temp == 101:
#    print ("Are you in hell? wkwk")
#elif temp >= 0 and temp <= 32:
#    print("The temperatur is good today")
#    print("Go outside!")
#elif temp < 0 or temp > 33:
#    print("Stay inside, protect your self!")
#else :
#    print("You will be freezing if you go outside!")

#if temp >= 5 and temp <= 36:
#    print("The weather is good!")
#elif temp == 0 or temp == 40:
#    print("Stay inside, protect your self!")
#else :
#    print("Warning! Extream weather, don't go outside!")

if not (temp >= 5 and temp <= 36):
    print("Stay inside, protect your self!")
elif not (temp == 0 or temp == 40):
   print("The weather is good!")    

else :
    print("Warning! Extream weather, don't go outside!")