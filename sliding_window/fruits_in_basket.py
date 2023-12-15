# Given an array of characters where each character represents a fruit tree,
# you are given 2 baskets and your goal is to put maximum number of fruits in 
# each basket. The only restriction is that each basket can have only one type of fruit.

# You can start with any tree, but once you have started you can't skip a tree. You will
# pick one fruit from each tree until you cannot, i.e. you will stop when you have picked
#  from a third fruit type.

#  Write a function to return the max number of fruits in both the baskets.

# input Fruits = ['A', 'B', 'C', 'A', 'C']
# output = 3



# input Fruits = ['A', 'B', 'C', 'B', 'B', 'C']
# output = 5


def solution(trees):
    start_pos = 0
    basket = {}
    fruits = 0

    for i, v in enumerate(trees):
        basket[v] = basket.get(v, 0) + 1
        while len(basket) > 2:
            basket[trees[start_pos]] -= 1
            if basket[trees[start_pos]] == 0:
                del basket[trees[start_pos]]

            start_pos += 1
        fruits = max(fruits, i - start_pos + 1)

    return fruits

print(solution(['A', 'B', 'C', 'A', 'C']), 3)


print(solution(['A', 'B', 'C', 'B', 'B', 'C']), 5)