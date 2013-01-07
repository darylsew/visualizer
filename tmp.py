import svt

x, y, z = svt.processWav("wubwub.wav", 1, 1650)

for i in range(len(z)):
    z[i] = abs(z[i][0]) + abs(z[i][1])

print max(z)
