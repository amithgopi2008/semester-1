# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey",
    "Belfast": "Lagan",
    "Cardiff": "Taff"
}


# Display all the keys

riverkeys = rivers.keys()
print(riverkeys)

# Display all the values

rivervalues = rivers.values()
print(rivervalues)

# Display all the key:value pairs, as tuples

rivertuple = rivers.items()
print(rivertuple)

# Delete an entry from the rivers database

rivers.pop("Cardiff")
print(rivers)
