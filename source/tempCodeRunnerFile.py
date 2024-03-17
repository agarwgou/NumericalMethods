    x = 10776321
    nsteps = 1200
    s = x / nsteps
    y = 0
    for i in range(nsteps):
        y += s
    print(x - y)

    x = 10.56
    print(x == x + 5e-16)

    x = 0.1234567891234567890
    y = 0.1234567891
    scale = 1e16
    z1 = (x-y) * scale
    print("z1 = ", z1)

    z2 = (x*scale - y*scale)
    print("z2 = ", z2)