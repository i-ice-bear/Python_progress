_brand_list = ["Samsung", "Dell", "HP", "Apple"]

for i in _brand_list:
    brand__name = input("What is your brand name > ").lower()
    if brand__name == "dell":
        print("Congrats! You own Dell")
        break
else:
    print("Get out!")
