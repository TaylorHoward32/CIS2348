#TaylorHoward
#1649552
#ZyLab 3.18

t_height = int(input('Enter wall height (feet): \n'))
t_width = int(input('Enter wall width (feet):\n'))
t_area = t_height * t_width
print('Wall area:', t_area, 'squared feet')
p_needed = t_area /350
print('Paint needed:', '{:.2f'.format(p_needed), 'gallons')

c_needed = round(p_needed)
print('Cans needed:', c_needed, 'can(s)\n\n')

p_prices = {'red': 35, 'blue': 25, 'green': 23}
p_color = input('Choose a color to paint the wall:\n')
print('Cost of purchasing {} paint: $'.format(p_color), end="")
print(p_prices[p_color])