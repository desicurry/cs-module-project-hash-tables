# Your code here
table = {}

def expensive_seq(x, y, z):
    # Your code here
    # We can use caching to help with the crazy recursions
    # Much like the fibonacci example we'll cache results to save time on repetitions
    if x <= 0:
        return y +z

    if (x, y, z) not in table:
        table[(x, y, z)] = expensive_seq(x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)

    return table[(x, y, z)]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
