# 1.Write a Python program that takes order from the user, generates the bill according to the following guidance and displays it to the user. Create and automatic pizza order program. Based on a user's order, work out their final bill.

# Small Pizza: Rs.150  Small Pizza: Rs.150  Small Pizza: Rs.150
# Pepperoni for Small Pizza: Rs. 20
# Pepperoni for Medium or Large Pizza: Rs. 30 Extra cheese for any size pizza: Rs. 10



# print("Small Pizza: Rs.150  Medium Pizza: Rs.200   Large Pizza: Rs.250")
# print("Pepperoni for Small Pizza: Rs. 20\n Pepperoni for Medium or Large Pizza: Rs. 30\n Extra cheese for any size pizza: Rs. 10")
# total =0
# size=input("Choose Size (S, M, L):")
# if size=="S":
#     Pepperoni4S=input("Do you want Pepperoni (y/n) : ")
#     if Pepperoni4S=="y":
#         total=150+20
#     else:
#         print("enter Valid input")
#     cheese=input("Do yo want Extra cheese (Y/N) : ")
#     if cheese=="Y":
#         total+=10
#     else:
#         print("enter Valid input")
#     print("Total Amount to Pay : ",total)
# elif size=="M":
#     Pepperoni4M=input("Do you want Pepperoni (y/n) : ")
#     if Pepperoni4M=="y":
#         total=200+30
#     else:
#         print("enter Valid input")
#     cheese=input("Do yo want Extra cheese (Y/N) : ")
#     if cheese=="Y":
#         total+=10
#     else:
#         print("enter Valid input")
#     print("Total Amount to Pay : ",total)
# elif size=="L":
#     Pepperoni4L=input("Do you want Pepperoni (y/n) : ")
#     if Pepperoni4L=="y":
#         total=250+30
#     else:
#         print("enter Valid input")
#     cheese=input("Do yo want Extra cheese (Y/N) : ")
#     if cheese=="Y":
#         total+=10
#     else:
#         print("enter Valid input")
#     print("Total Amount to Pay : ",total)


# 2. Print the pattern
# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1 
# 6 5 4 3 2 1 
# 7 6 5 4 3 2 1 


# for i in range(1,8):
#     for j in range(i,0,-1):
#         print(j, end=" ")
#     print(" ")


# 3. Write a Python program find the longest string of a given list of strings. Go to the editor
# Input:
# ['cat', 'car', 'fear', 'center']
# Output:
# center
# Input:
# ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
# Output:
# shatter

text=['cat', 'car', 'fear', 'center']
lengest=text[0]
for i in text:
    if len(i) > len(lengest):
        lengest=i
print(lengest)


# 4. Have the function ArrayChallenge(arr) take the array of numbers stored in arr which will contain integers that represent the amount in dollars that a single stock is worth,and return 
# the maximum profit that could have been made by buying stock on day X and selling stock on day Y where Y>X .For example if array is [44,30,24,32,35,30,40,38,15] then your program should 
# return 16 because at index 2 the stock was worth $24 and at index 6 the stock was then worth $40, so if you brought the stock at $24 and sold it at $40, 
# you would have made a profit of $16,which is the maximum profit that could have been made with this list of stock prices.

def ArrayChallenge(arr):
    min_price=arr[0]
    max_profit=0
    for price in arr:
        if price < min_price:
            min_price=price
        profit=price - min_price
        if profit > max_profit:
            max_profit=profit
    return max_profit
arr=[50, 20, 40, 70, 30, 80]
print( ArrayChallenge(arr))






# 5. Word Count: Write a Python program that reads a text file and counts the number of occurrences of each word in the file.

# file = open("evaluation/text.txt", "r")
# text=file.read()
# file.close
# word_count={}
# word=text.split()
# for i in word:
#     if i in word_count:
#         word_count[i] +=1
#     else:
#         word_count[i]=1

# print(word_count)





