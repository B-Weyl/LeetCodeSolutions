s = ["ufvpzzgpswnk"]
chars = "avyteswqppomeojxoybotzriuvxolmllevluauwb"

for word in s:
    good = True
    total = 0
    for letter in word:
        # print(word.count(letter) > chars.count(letter))
        if word.count(letter) > chars.count(letter):
            good = False
        if letter not in chars:
            good = False
    print(good)

    if good is False:
        s.remove(word)
print(s)
for word in s:
    total += len(word)
