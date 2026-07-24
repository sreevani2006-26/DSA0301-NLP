import re
products = [
    "Laptop",
    "Laptop Stand",
    "Laptop Bag",
    "Wireless Mouse",
    "Gaming Mouse",
    "Bluetooth Speaker",
    "Smart Phone",
    "Phone Case",
    "Headphones",
    "Python Programming Book"
]
def search_products(keyword):
    print("\nSearch Keyword:", keyword)
    exact = [p for p in products if re.fullmatch(keyword, p, re.IGNORECASE)]
    print("\nExact Match:", exact)
    prefix = [p for p in products if re.search(r"^" + re.escape(keyword), p, re.IGNORECASE)]
    print("Prefix Match:", prefix)
    suffix = [p for p in products if re.search(re.escape(keyword) + r"$", p, re.IGNORECASE)]
    print("Suffix Match:", suffix)
    partial = [p for p in products if re.search(re.escape(keyword), p, re.IGNORECASE)]
    print("Partial Match:", partial)
    print("\n----- Report -----")
    print("Exact Matches :", len(exact))
    print("Prefix Matches:", len(prefix))
    print("Suffix Matches:", len(suffix))
    print("Partial Matches:", len(partial))
key = input("Enter product keyword: ")
search_products(key)
