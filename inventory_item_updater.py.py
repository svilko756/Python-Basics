lists_of_producs = ["Apple", "Banana", "Orange", "Kiwi"]
choice = int(input("Choice? ")) 

if choice == 1:
    selected_product = (input("Please select your product to be replaced: "))
    if selected_product in lists_of_producs :
        for i, needed_product in enumerate(lists_of_producs):
            if needed_product == selected_product:
               lists_of_producs[i] = input("Enter your product: ")

print(lists_of_producs)
               