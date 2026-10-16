USD_Amount = float (input("Enter the amount by USD: "))
exchange_rate = 150
Exchange_rate = float (input ("Enter the exchange rate : ")) # we can also ask the user to enter the exchange rate so that we can know the amount by different exchange rate 
amount= USD_Amount * Exchange_rate
ETB_Amount = USD_Amount * exchange_rate # this one multiplies the amount by default 150
print ()
print ("======================")
print ("CURRENCY EXCHANGE ")
print ("======================")
print ()
print (f"USD Amount:   {USD_Amount}")
print ()
print (f"Exchange rate : 1 USD = {exchange_rate} ETB")
print ()
print (f"ETB Amount:    {ETB_Amount} ETB")
print ( amount)
print ("=======================")