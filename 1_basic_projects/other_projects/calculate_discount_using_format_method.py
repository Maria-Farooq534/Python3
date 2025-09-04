#original price $2.50 with a 7% discount:

original_p = int(input("Enter total price in $ : "))
discount = int(input("Enter discount in $ : "))

new_price = (1- (discount/100)) * original_p

#calculation = "${} discounted by {}% is {}.".format(original_p , discount , new_price)
calculation = "${:.2f} discounted by {}% is {:.2f}".format(original_p , discount, new_price) 
#:.2f indicates that its a floating point and will have 2 numbers after the floating point.
#If we want 4 digits after floating point for more precision, we can write :.4f
calculation = "${:.4f} discounted by {}% is {:.4f}".format(original_p , discount, new_price) 
print(calculation)

