#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_remove,
    hash_table_retrieve,
    hash_table_resize
)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)
    
    current = hash_table_retrieve(hashtable, "NONE")
    route[0] = current
    counter = 0
    while current is not "NONE":
        counter += 1
        current = hash_table_retrieve(hashtable, current)
        route[counter] = current

    return route
