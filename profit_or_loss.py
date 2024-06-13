cost_price=int(input("enter the cost price"))
selling_price=int(input("enter the selling price"))
#using if else ladder
if selling_price>cost_price:
    print("profit is:",selling_price-cost_price)
elif selling_price<cost_price:
    print("loss is",cost_price-selling_price)
else:
    print("no profit no gain")    
