songs = set()
songs.add(("Nickelback", "How you remind me"))
songs.add(("BigBang", "Bang Bang Bang"))
songs.add(("BigBang", "Fantastic Baby"))
songs.add(("Nickelback", "Animals"))
print(songs)
new_list = list(songs)
print(new_list)
list = [list for list in new_list if list !=('Nickelback', 'Animals')if list !=('Nickelback', 'How you remind me')]
print(list)