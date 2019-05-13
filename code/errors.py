"""
menu:
1. vegan ramen
2. pineapple cupcake
3. a lychee

please select a menu item:
> 2
here is your pineapple cupcake

please select a menu item:
> 100
we do not have that item

please select a menu item:
> i do not want anything!!!!!!
that is not a number, k thx bai
"""
food = 'vegan ramen', 'pineapple cupcake', 'lychee'

for i, f in enumerate(food):
    print(f'{i + 1}. {f}')
answer = input('select a menu item\n>')
try:
    food_index = int(answer)
    item = food[food_index - 1]
except (IndexError, ValueError) as e:
    print('that item does not exist')
    print(e)
    item = None

if item is not None:
    print(f'here is ur {item}')
"""
1. vegan ramen
2. pineapple cupcake
3. a lychee
"""












