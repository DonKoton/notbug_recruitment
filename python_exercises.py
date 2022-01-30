# ------------ exercise 1 ------------
users = [{"name": "Kamil", "country": "Poland"}, {"name": "John", "country": "USA"}, {"name": "Yeti"}]

new_users = [user.get("name") for user in users if user.get("country") == "Poland"]

users2 = [{"name": "Kamil", "country": "Poland"},
          {"name": "John", "country": "USA"},
          {"name": "Yeti"},
          {"name": "Majkel", "country": "Poland"},
          {"name": "Jordan", "country": "Poland"},
          {"name": "Kaczor", "country": "Poland"},
          {"name": "Donald", "country": "Poland"},
          {"name": "Kebab", "country": "Turkey"},
          {"name": "Marek", "country": "Germany"},
          {"name": "Wayne", "country": "England"},
          {"name": "Lorenzo", "country": "Italy"},
          {"name": "Antoine", "country": "France"},
          ]

# example with more users to show
new_users2 = [user.get("name") for user in users2 if user.get("country") == "Poland"]

print(new_users)
print(new_users2)


# ------------ exercise 2 ------------
numbers = [1, 5, 2, 3, 1, 4, 1, 23, 12, 2, 3, 1, 2, 31, 23, 1, 2, 3, 1, 23, 1, 2, 3, 123]

result = 0

for counter, num in enumerate(numbers[4:], start=1):
    result += num
    if counter == 10:
        break

print(result)

# other solution
print(sum(numbers[4:14]))


# ------------ exercise 3 ------------
powers = [n**2 for n in range(21)]

print(powers)
