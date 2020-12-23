import file_input
lines = file_input.get_input(21)

data = []
for line in lines:
    ingr, alle = line.replace(')', '').strip().split('(contains ')
    ingredients = set(ingr.strip().split(' '))
    allergens = alle.strip().split(', ')
    data.append([ingredients, allergens])

allergen_foods = dict()
for ingredients, allergens in data:
    for allergen in allergens:
        if allergen not in allergen_foods:
            allergen_foods[allergen] = ingredients.copy()
        else:
            allergen_foods[allergen] &= ingredients

known_risks = set()
for allergen in allergen_foods:
    known_risks |= allergen_foods[allergen]

count = 0
for ingredients, x in data:
    for ingr in ingredients:
        if ingr not in known_risks:
            count += 1
print(count)

# and then I just did part 2 by hand c:
for allergen in allergen_foods:
    print(str(allergen) + ": " + str(allergen_foods[allergen]))
