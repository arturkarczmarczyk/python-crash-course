motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles.insert(1, 'added')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

print(f"I removed {motorcycles.pop(1)}")
print(motorcycles)

motorcycles.remove("honda")
print(motorcycles)
