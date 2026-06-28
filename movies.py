menu={"DHURANDAR 2":190.00,
      "GBU"        :90.00,
      "ARASAN"     :189.00,
      "RRR"        :191.00,
      "PEDDI"      :199.00,
      "LUCIFER"    :1000.00}
booking=[]
total=0

for key,value in menu.items():
    print(f"{key:15}:₹{value}")

while True:
    x=input("select an item(enter q to quit):")
    if x.lower()== "q":
        break
    elif menu.get(x) is not None:
        booking.append(x)
print(booking)

for x in booking:
    total += menu.get(x)
    print(x, end ="")


print(f"total is {total:2f}")

