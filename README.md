See Instruction-of-Mobile-App-Calculator-testing.docx for more details on testing 

Quick notes on testing the calculator:
-The fields are listed in order of item name, price, quantity, a plus button for increasing the quantity, a minus button
-The five items that can be added are Apple, Orange, Headphones, Pear, and Grape. They are the items in catalogue.json. All the available items are displayed on your list at the beginning of the app, each with a quantity of 1. Pressing reset will return your list to this initial state. 
-Adding a non-existing item will produce an error alert 
-Adding an item existing on your item list will increase the quantity of 1
-Entering an invalid tax or discount percentage will produce an error alert 
-The tax and discount amounts are calculated as a percentage of the original total cost, and then added on to produce the final total cost. 
-Pressing submit will submit your order to the heroku server. See the word doc for info on how to view it. 
