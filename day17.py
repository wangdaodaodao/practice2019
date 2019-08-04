fish = 6

while True:
    tolal = fish
    enough = True
    for _ in range(5):
        if (tolal - 1) % 5 == 0:
            tolal = (tolal - 1) // 5 * 4
        else:
            enough = False
            break
        if enough:
            print(fish)
            break
        fish += 5