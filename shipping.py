weight = 8.4
cost_ground = ""
cost_drone_shipping = ""
#ground shipping
if weight <= 2:
  cost_ground = 1.50 * weight + 20
elif weight > 2 and weight <= 6:
  cost_ground = 3.00 * weight + 20
elif weight > 6 and weight <= 10:
  cost_ground = 4.00 * weight + 20
else:
  cost_ground = 4.75 * weight + 20

#ground premium
cost_ground_premium = 125

#drone shipping
if weight <= 2:
  cost_drone_shipping = 4.50 * weight  
elif weight > 2 and weight <= 6:
  cost_drone_shipping = 9.00 * weight 
elif weight > 6 and weight <= 10:
  cost_drone_shipping = 12.00 * weight  
else:
  cost_drone_shipping = 14.25 * weight

print("The cost to ship Ground is: ", cost_ground )
print("The cost to ship Ground Premium is: ", cost_ground_premium )
print("The cost for Drone shipping is: ", cost_drone_shipping )