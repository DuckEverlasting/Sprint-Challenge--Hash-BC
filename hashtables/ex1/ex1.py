#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_remove,
    hash_table_retrieve,
    hash_table_resize
)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(length):
        if hash_table_retrieve(ht, weights[i]) != None:
            prev = hash_table_retrieve(ht, weights[i])
            hash_table_insert(ht, weights[i], f'{prev}-{i}')
        else:
            hash_table_insert(ht, weights[i], i)
    for i in range(limit):
        if limit - i == i:
            print(hash_table_retrieve(ht, i))
            x = hash_table_retrieve(ht, i)
            if isinstance(x, str):
                x = x.split("-")
                if x[1] > x[0]:
                    return (int(x[1]), int(x[0]))
                else:
                    return (int(x[0]), int(x[1]))
        else:
            a = hash_table_retrieve(ht, i)
            if isinstance(a, str):
                a = a.split("-")
                a = a[-1]
            b = hash_table_retrieve(ht, limit - i)
            if isinstance(b, str):
                b = b.split("-")
                b = b[-1]
            if a and b:
                if b > a:
                    return (b, a)
                else:
                    return (a, b)

    return None

ht = HashTable(16)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
