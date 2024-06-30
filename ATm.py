#ATM MACHINE USING PYTHON


pin=2457
chances=4
balance=10000
print('*******************************')
print('*******************************')
print('*** WELCOME TO OCTANET BANK ***')
print('*******************************')
print('*******************************')

while chances!=0:
    user_pin=int(input("enter the four digit ATM pin : "))
    if(user_pin != pin):
     print("you have entered the wrong  ATM pin\n")
     chances=chances-1
     
    else:
       
       
       
       user_choice=input("1:BALANCE , 2: DEPOSIT, 3: WITHDRAW ,4: CHANGE PIN \n")
       if(user_choice == "1"):
          print("the current balance of your savings accout is : Rs.{balance}\n")


       if(user_choice == "2"):
          deposit=int(input("enter the amount you want to deposit\n"))
          balance=balance+deposit
          print('*******************************')
          print('*******************************')
          print('*** YOU HAVE DEPOSITED SUCCESFULLY ***')
          print('*******************************')
          print('*******************************')
          print("\n")
          print("\n")
          print(f"the  total amout you have  deposited is : Rs.{deposit}\n")
          print(f"your total amout after depositing is : Rs.{balance}\n")


       if(user_choice == "3"):
          withdraw=int(input("enter the amount you want to withdraw\n"))
          balance=balance-withdraw
          print('*******************************')
          print('*******************************')
          print('*** YOU HAVE WITHDRAWN SUCCESFULLY ***')
          print('*******************************')
          print('*******************************')
          print("\n")
          print("\n")
          print(f"the  total amout you have  withdrawn is : Rs.{withdraw}\n")
          print(f"your total amout after withdrawing  is : Rs.{balance}\n")
      
       if (user_choice =="4"):
       
        print('*****************************')
        new_pin = int(input('Enter the new pin: '))
        print('*****************************')
        
        
        print('******************')
        confirm_pin = int(input('Confirm the new pin: '))
        print('*******************')
        
        if confirm_pin != new_pin:
                print('------------')
                print('************')
                print('PIN MISMATCHEd')
                print('************')
                print('------------')
        else:
                pin = new_pin
                print('************')
                print('NEW PIN SAVED')
                print('************')
                

       
    user_exit=input("Would you like to EXIT ? Yes/No\n")
    if(user_exit=="Yes"):
            print('*******************************')
            print('*******************************')
            print('*** THANK YOU FOR USING OCTANET BANK ***')
            print('*******************************')
            print('*******************************')
            exit()
            break
    else:
        continue
                
       
       
       



      
       


     

