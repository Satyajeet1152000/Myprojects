s = input("string: ")
s = s.lower()

adds = ['trailer',
       'official trailer',
       'movie',
       'movie trailer',
       'movie official trailer',
       ]

print(s,",")
for i in range(len(adds)):
    print(f"{s} {adds[i]},")