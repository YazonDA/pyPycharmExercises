""" Calculate the cost of a liter in the store packing box

"""
size_arr = [0, 0, 0, 0]
name_arr = ['size_1', 'size_2', 'size_3', 'price']
i = -1

while True:
    i = (i + 1) % 4
    s = input(name_arr[i] + ' = ')
    if s != '//':
        if i == 3:
            size_arr[i] = float(s)
            vol = 1
            for j in range(3):
                vol = vol * size_arr[j]
            print(f'{size_arr[0]}x{size_arr[1]}x{size_arr[2]} -- {vol:.2f}m3 & {size_arr[3] / vol:.2f}p/m3')
        else:
            size_arr[i] = int(s) / 1000
    else:
        break
