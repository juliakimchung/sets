songs = set()
songs.add(("Nickelback", "How you remind me"))
songs.add(("BigBang", "Bang Bang Bang"))
songs.add(("BigBang", "Fantastic Baby"))
songs.add(("Nickelback", "Animals"))
songs.add(("EXO", "growl"))
songs.add(("BTS", "fire"))
songs.remove(("BTS", "fire"))
songs.update(["girsgeneration", "AOA", "f(x)"])
length = len(songs)
print(songs)
print(length)
new_list = list(songs)
print(new_list[0])
print(new_list)
list = [list for list in new_list if list !=('Nickelback', 'Animals')if list !=('Nickelback', 'How you remind me') if list != "AOA"]
print(list)


new_songs = set()
new_songs.update(["girlsgeneration", "f(x)"])
new_songs.add(("Nickelback", "How you remind me"))
new_songs.add(("EXO", "growl"))

print(new_songs)
another_songs = songs.union(new_songs)
print(another_songs)
print(songs.intersection(new_songs))
new_list = tuple(new_songs)
print(new_list)


