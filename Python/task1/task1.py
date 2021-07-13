with open("input.txt", "r", encoding="UTF-8") as inputFile:
    lines = inputFile.readlines()
    N = int(lines[0])
    M = int(lines[1])
    H = int(lines[2])
A = int(M / (H // N) + 0.5)
with open("output.txt", "w", encoding="UTF-8") as outputFile:
    outputFile.write(str(A))
