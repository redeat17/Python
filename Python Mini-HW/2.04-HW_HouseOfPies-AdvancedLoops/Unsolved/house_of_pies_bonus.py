print("Welcome to the House of Pies! Here are our pies: ")
pie_menu = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]
pie_purchases = []
for i in pie_menu:
    print("("+str(pie_menu.index(i)+1)+") " + i)
buy = "y"
count = 0
while buy.lower() == "y":
    order = int(input("Please tell us the number of the pie you like: "))
    print(f"Great! We'll have the {pie_menu[order-1]}")
    pie_purchases.append(str(pie_menu[order-1]))
    count = count + 1
    buy = input("Do you want to make another order? ")
print("Total pies ordered: " + str(count));
for pie in pie_menu:
    count = pie_purchases.count(pie)
    print(str(count)  + ' ' +pie );