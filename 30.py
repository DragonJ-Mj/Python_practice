# 30.	The Sardar Patel Cricket Stadium, Motera has the following rates for different types of seats:
# •	Ordinary – 2500
# •	Pavillion – 3500
# •	Upper Pavillion – 4500
# •	Commentary Box – 6000
# •	VIP – 8000
# i.	They are giving 10% discount for online booking and 8% discount for advance booking and no discount is given for booking on match day from ticket window.
# ii.	Ask user to enter the booking type like online, advance or window booking.
# iii.	Ask user to select the types of seats.
# iv.	Compute the amount and print the ticket with proper format.


ticket_price = input("Sardar Patel Cricket Stadium Ticket Types\n\nOrdinary - 2500 rs - press 'ord'\nPavvillion - 3500 rs - press 'pav'\nUpper Pavillion – 4500 rs - press 'upp'\nCommentary Box – 6000 rs - press 'cbox'\nVIP – 8000 rs - press 'vip'\n\nEnter your Booking type - 'ord,pav,upp,cbox,vip' : ")

booking_type = input("Types of Booking\n\nOnline Booking - 10% instant discount- press 'on'\nAdvance Booking - 8% discount - press 'ad'\nNo discount on match day form ticket window\n\nEnter Your Booking type - 'on, ad' : ")

seats_enter = int(input("Enter number of seats :"))
match ticket_price:
    case 'ord':
        price = 2500
    case 'pav': 
        price = 3500
    case 'upp':
        price = 4500
    case 'cbox':
        price = 6000
    case 'vip':
        price = 8000
    case _:
        print("Invaide Type")
        
def totalSeats(price,seats):
    return price *seats
final_price = 0
def calPrice(bType,tPrice):
   match bType:
       case "on":
           final_price = tPrice - ((tPrice *10)/100)
       case "ad":
           final_price = tPrice - ((tPrice *8)/100)        
   return final_price   
fPrice = calPrice(booking_type, price)
print("Final Price is :",totalSeats(fPrice,seats_enter))
                