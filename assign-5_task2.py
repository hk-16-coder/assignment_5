l = []
for i in range(1,11):
    l.append(i)

print(f"Original list : {l}")

extracted = l[0:6]
print(f"Extracted first five elements : {extracted}")

extracted.reverse()
print(f"Reversed extracted elements : {extracted}")
