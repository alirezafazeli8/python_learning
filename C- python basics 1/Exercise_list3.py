#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']

# print(friends.sort() + new_friend)

#NOTE solution

friends.extend(new_friend)
friends.sort()

print(friends)


