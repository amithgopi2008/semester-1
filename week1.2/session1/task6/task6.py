# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)

oasisalbums = ["Definitely Maybe", "What's the story, morning glory", "The Masterplan", "Be Here Now"]
radioheadalbums = ["In Rainbows", "OK Computer", "The Bends", "Amnesiac"]
kanyewestalbums = ["The College Dropout", "Late Registration", "Graduation", "808's", "MBDTF", "Yeezus"]

musicdatabase = {
    "Oasis": oasisalbums,
    "Kanye West": kanyewestalbums,
    "Radiohead": radioheadalbums,

}

pprint(musicdatabase)



# Pretty-print the data structure

# Display details of one album recorded by a specific artist
