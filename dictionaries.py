# uses key value pairs, like JS object

my_dictionary = {
  "value1": "key1",
  "value2": "key2"
}

print my_dictionary
print my_dictionary['value1']

price_matches = {
  "apple": 2.99,
  "pear": 1.99,
  "carrot": 0.79
}

grocery_price  = (price_matches["apple"] * 2) + price_matches["pear"]

print grocery_price

# adding to the dictionary
price_matches["lettuce"] = 0.99

print price_matches
print price_matches.keys()
print price_matches.values()
print price_matches.items()