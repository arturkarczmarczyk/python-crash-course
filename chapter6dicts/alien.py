alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0['x'] = 0
alien_0['y'] = 25
print(alien_0)


del alien_0['points']
print(alien_0)


print(alien_0.get('color', 'No color'))
print(alien_0.get('points', 'No points'))
