"""
display a list of food
a user will choose from a list of menu items
if it doesn't exist... handle exception
if it does exist... then print out message saying their food is done

menu

1. ramen
2. a single lychee
3. ice cream

please order an item

> 2
your single lychee is done

=====

> 100
we don't have that

> "whatever"
please enter a number
"""

food = ['ramen', 'lychee', 'red bean ice cream']

for i, item in enumerate(food):
    """
    print(str(i + 1) + '. ' + item)
    print('%s. %s' % (i + 1, item))
    print('{}. {}'.format (i + 1, item))
    """
    print(f'{i + 1}. {item}')

answer = input('what would you like to order?')

try:
    menu_number = int(answer)
    food_item = food[menu_number - 1]
except ValueError:
    print('that was not a number')
    food_item == None
except IndexError:
    print('that menu item does not exist')
    food_item == None

if food_item is not None:
    print(f'Your {food_item} is ready')



















