def test():
    with open('d1input.txt') as f:
        data = f.readlines()
        data = map(int, data)

    current = 0
    occured = set()

    data = list(data)

    while True:
        for line in data:
            new = current + line

            if new in occured:
                print('occured before!', new)
                return

            current = new
            occured.add(new)


test()

