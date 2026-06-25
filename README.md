# Python_practice

## Table of Content
- [Python\_practice](#python_practice)
  - [Table of Content](#table-of-content)
    - [24-Jun-2026](#24-jun-2026)
      - [30.py](#30py)
    - [25-Jun-2026](#25-jun-2026)
      - [19.py](#19py)
      - [20.py](#20py)
      - [21.py](#21py)

### 24-Jun-2026
#### 30.py
- The Sardar Patel Cricket Stadium, Motera has the following rates for different types of seats:
   - Ordinary – 2500
   - Pavillion – 3500
   - Upper Pavillion – 4500
   - Commentary Box – 6000
   - VIP – 8000
1. They are giving 10% discount for online booking and 8% discount for advance booking and no discount is given for booking on match day from ticket window.
2. Ask user to enter the booking type like online, advance or window booking.
3. Ask user to select the types of seats.
4. Compute the amount and print the ticket with proper format.
```python 
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
```

### 25-Jun-2026
#### 19.py 

- Problem: Use a while loop to repeatedly prompt a user to create a password. Keep looping until they enter a password that is at least 8 characters long.
- Expected Behavior: * User enters "123" \rightarrow Prints "Too short!", loops again.
- ​User enters "secret123" \rightarrow Prints "Password accepted!", terminates.

```python
user_password = input("Enter the Passward: ")
length = len(user_password)


while length <9 :
    if length>= 8:
        print("Password Accepted")
        break
    print("You entered ", user_password, "which is too short")
    loop_pass = input("Enter new password = ")
    length = len(loop_pass)
   
print("Password Accepted")
```

#### 20.py 

- use a for loop to find and print the largest number in a list.
- ​Given: scores = [45, 82, 94, 12, 75, 63]

```python
scores = [45, 82, 94, 12, 75, 63]
largest = scores[0]
for i in scores:
    if i > largest:
        largest = i
print(largest)

```

#### 21.py
- Problem: Given a list with duplicate elements, use a for loop to build a new list that contains each element exactly once (preserving the original order). Do not use set().
- ​Given: dupes = ['a', 'b', 'a', 'c', 'b', 'd']
- ​Expected Output List: ['a', 'b', 'c', 'd']
```python
dupes = ['a', 'b', 'a', 'c', 'b', 'd']
new = []
for i in dupes:
    if (i not in new):
        new.append(i)
print(new)
```