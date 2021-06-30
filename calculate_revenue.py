
#Answer 1
sales=150
average_price = 2100
cogs_percentage = 0.59

# gross revenue
annual_gross_revenue = sales * average_price
quarterly_gross_revenue = annual_gross_revenue / 4.0
monthly_gross_revenue = annual_gross_revenue / 12.0


print ("The annual gross revenue ", annual_gross_revenue)
print ("The monthly gross revenue ", monthly_gross_revenue)
print ("quarterly gross revenue", quarterly_gross_revenue)

#Answer 2
#Net revenue accounts
cogs = annual_gross_revenue * cogs_percentage
annual_net_revenue = annual_gross_revenue - cogs
quarterly_net_revenue = annual_net_revenue / 4.0
monthly_net_revenue = annual_net_revenue / 12.0



print ("The annual net revenue ", annual_net_revenue)
print ("The monthly net revenue ", monthly_net_revenue)
print ("quarterly net revenue", quarterly_net_revenue)