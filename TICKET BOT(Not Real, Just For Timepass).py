tick = int(input("How Many Tickets Do You Want($5): "))

if tick>0:
    print("Ticket",tick)
    tick3 = tick * 5

    print("Pay Your Bill $",tick3)
    inp = int(input("Bill:$"))

else:
    print("Please Enter Again")
if tick3 == inp:
    print("Thank you for purchasing")
elif tick >= inp:
    tick2 = tick3 - inp
    print("Thank you for purchasing")
    print("Please Take Your Chance $"+tick2)
elif tick < inp:
    tick4 = tick3 - inp
    print("Please Pay More $",tick4)
