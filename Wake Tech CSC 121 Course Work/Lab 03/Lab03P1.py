#
# Nathanael Long
# Sept 7th 2025
# Inventory Estimator
#

# Get the starting numbers of paperbacks and hardbacks.
books = int(input('What is the current number of books? '))
dvds = int(input('What is the current number of DVDs? '))
games = int(input('What is the current number of games? '))
print()

# Display the inventory stock table.
for month in range(1, 4):
    books += 45
    dvds += 32
    games += 15
    print(f'Month {month}')
    print(f'\tBooks: {books}')
    print(f'\t DVDs: {dvds}')
    print(f'\tGames: {games}')

