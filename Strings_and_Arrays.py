#This are probelem sets from codepath TIP 103 

#Strings and Arrays
#Problem 1: Hunny Hunt
def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
print(linear_search(items, target))
#returns 3

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
print(linear_search(items, target))
#returns -1 



#Problem 2: Bouncy, Flouncy, Trouncy, Pouncy
def final_value_after_operations(operations):
    value = 1
    for operation in operations:
        if operation in ("bouncy", "flouncy"):
            value += 1
        if operation in ("trouncy",  "pouncy"):
            value -= 1
    return value

operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))
#returns 2

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))
#returns 4



#Problem 3: T-I-Double Guh-Er II
def tiggerfy(word):
    word = word.lower()
    word = word.replace('t', '')
    word = word.replace('i', '')
    word = word.replace('gg', '')
    word = word.replace('er', '')
    return word


word = "Trigger"
print(tiggerfy(word))
#returns "r"

word = "eggplant"
print(tiggerfy(word))
#returns "eplan"

word = "Choir"
print(tiggerfy(word))
#returns "Chor"



#Problem 4: Non-decreasing Array
def non_decreasing(nums):
	count = 0
	for i in range(len(nums)-1):
		if nums[i] > nums[i+1]:
			count += 1
			if count > 1:
				return False
	return True


nums = [4, 2, 3]
print(non_decreasing(nums))
#returns True

nums = [4, 2, 1]
print(non_decreasing(nums))
#returns False


#Problem 5: Missing Clues
def find_missing_clues(clues, lower, upper):
    result = []
    i = lower

    while i <= upper:
        if i not in clues:
            start = i

            while i <= upper and i not in clues:
                i += 1

            end = i - 1
            result.append([start, end])
        else:
            i += 1

    return result

clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(find_missing_clues(clues, lower, upper))
#returns [[2, 2], [4, 49], [51, 74], [76, 99]]

clues = [-1]
lower = -1
upper = -1
print(find_missing_clues(clues, lower, upper))
#returns []



#Problem 6: Vegetable Harvest
def harvest(vegetable_patch):
    n = len(vegetable_patch)
    m = len(vegetable_patch[0])
    carrot = 0
    for i in range(n):
        for j in range(m):
            if vegetable_patch[i][j] == 'c':
                carrot += 1
    return carrot
    
    
	
vegetable_patch = [['x', 'c', 'x'],['x', 'x', 'x'],['x', 'c', 'c'],['c', 'c', 'c']]
print(harvest(vegetable_patch))
#returns 6



#Problem 7: Eeyore's House
def good_pairs(pile1, pile2, k):
    count = 0
    for i in pile1:
        for j in pile2:
            if i % (j*k) == 0:
                count += 1
    return count


pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
print(good_pairs(pile1, pile2, k))
#returns 5

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
print(good_pairs(pile1, pile2, k))
#returns 2



#Problem 8: Local Maximums
def local_maximums(grid):
    n = len(grid)
    result = []

    for i in range(n - 2):
        row = []
        for j in range(n - 2):

            max_val = 0

            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    max_val = max(max_val, grid[x][y])

            row.append(max_val)

        result.append(row)

    return result


grid = [
	[9, 9, 8, 1],
	[5, 6, 2, 6],
	[8, 2, 6, 4],
	[6, 2, 2, 2]
]
print(local_maximums(grid))
#returns [[9, 9], [8, 6]]

grid = [
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 2, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1]
]
print(local_maximums(grid))
#returns [[2, 2, 2], [2, 2, 2], [2, 2, 2]]