alphabet = ["a", "b", "c", "c", "b", "d", "e", "j", "j"]
duplicate = []

for alpha in alphabet:
    if alphabet.count(alpha) > 1:
        if alpha not in duplicate:
            duplicate.append(alpha)
    else:
        continue

print(duplicate)
