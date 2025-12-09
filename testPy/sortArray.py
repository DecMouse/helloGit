# create array includes some numbers
numbers = [12, 3, 6, 59, 80]

def sortArray(arr):
    return sorted(arr, reverse=True,)

if __name__ == "__main__":
	print(sortArray(numbers))
	
sortArray(numbers)