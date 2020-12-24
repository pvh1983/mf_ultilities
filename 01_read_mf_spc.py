# Read *.spc file and convert to vector of dx and dy


ifile = 'input/model.spc'

ct = 1
dx = []
dy = []

with open(ifile) as f:
    for line in f:
        # Do something with 'line'
        tmp = line.split()
        print(f'tmp\n\n')
        if ct == 1:  # firt row
            nr, nc = int(tmp[0]), int(tmp[1])
            print(f'nr={nr}, nc={nc}\n')
        elif ct == 2:  # read origina
            x0, y0, z0 = float(tmp[0]), float(tmp[1]), float(tmp[2])
        else:
            ct2 = 0
            if len(dy) <= nr:
                for k in tmp:
                    dy.append(float(k))
            elif len(dx) <= nc:
                for k in tmp:
                    dx.append(float(k))
        # Increase row
        ct += 1

# Save outputs
file = open('output/grid_dx.csv', 'w')
for i in dx:
    file.write(f'i')
file.close()

file = open('output/grid_dy.csv', 'w')
for i in dy:
    file.write(f'i')
file.close()
