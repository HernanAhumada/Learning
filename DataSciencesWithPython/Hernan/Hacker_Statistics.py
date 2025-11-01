import numpy as np
import matplotlib.pyplot as plt

# Set the seed
np.random.seed(123)

# Generate and print random float
for i in range(1,11):
    print(np.random.rand())

#Throw the dice
# Use randint() to simulate a dice
print(np.random.randint(1, 7))
# Use randint() again
print(np.random.randint(1, 7))

'''you're walking up the empire state building to DataCamp HeadQuarters and you're playing a game with a friend.
You throw a die.
If it's 1 or 2 you'll go one step down.
If it's 3, 4, or 5, you'll go one step up.
If you throw a 6, you'll throw the die again and will walk up the resulting number of steps.'''
# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1, 7)

if dice <= 2 :
    step = step - 1
elif dice >= 3 and dice <= 5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)

# Print out dice and step
print(dice)
print(step)


print('#####################################################')
print('#####################################################')
print('#####################################################')
print('#####################################################')
print('#####################################################')


# NumPy is imported, seed is set to 123

# Initialize random_walk
all_walks = []

# Simulate random walk five times
for i in range(20) :
    random_walk = [0]
    for x in range(100) :
        # Set step: last element in random_walk
        step = random_walk[x]
        # Roll the dice
        dice = np.random.randint(1,7)
        # Determine next step. Use max to make sure step can't go below 0
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        # Implement clumsiness
        if np.random.rand() <= 0.005:
            step = 0
        # append next_step to random_walk
        random_walk.append(step)
    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print random_walk
print(random_walk)
# Print all_walks
print(all_walks)

plt.plot(random_walk)
plt.show()
# Clear the figure
plt.clf()

plt.plot(all_walks)
plt.show()
plt.clf()
# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks) 
# Plot np_aw and show
plt.plot(np_aw)
plt.show()
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()

ends = np_aw_t[-1,:]

#what's the estimated chance that you'll reach at least 60 steps high 
# if you play this Empire State Building game? 
print(str(np.sum(ends >= 60) / 20 * 100) + '%')