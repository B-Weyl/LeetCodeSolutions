codes = [
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
    "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-",
    "...-", ".--", "-..-", "-.--", "--.."
]
return_values = []
words = ["gin", "zen", "gig", "msg"]
ans = {}
the_ans = []

for pos, val in enumerate(codes):
    ans[val] = chr(97 + pos)
# print(ans.items())
ans2 = {y: x for x, y in ans.items()}
for word in words:
    z = ''
    for letter in word:
        z += ans2[letter]

    the_ans.append(z)
print(len(set(the_ans)))
