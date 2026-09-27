

# for i in range(10,21,3):
#    print(i)

# for i in range(5,101,5):
#    print(i)

# for i in range(1,11):
#    print(f"5x{i} = {5*i}")


# def udskriv_lige_tal(max_tal):
#    for tal in range(2,max_tal,2):
#        print(tal)

# udskriv_lige_tal(500)


# def udskriv_lige_tal_ny(max_tal):
#    for tal in range(2,max_tal):
#        if tal % 7 == 0:
#            print(tal)

# udskriv_lige_tal_ny(100)


count = 10
count_start = 0

print(f"Vi tæller ned fra {count}")
while count >= 1:
    print(f"{count}...")
    count -= 1
    count_start += 1

print(f"Nu har vi talt ned fra {count_start}")

