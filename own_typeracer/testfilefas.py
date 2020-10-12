low = 97
upp = 65
let_in_alpha = 26
dict = {}

for i in range(26):
    dict[chr(low + i)] = chr(upp + i)

print(dict)

#97 --> a
#122 --> z
#65 --> A