def elf_maximums(input):
    output = []
    i = 0
    for line in input:
        # count the amount of \n in the line
        # retrieve number int from line, ignoring whitespace. if there is no number, return 0
        if line == "":
            i += 1
            continue

        number = int(line)

        # check if output has index i
        if len(output) <= i:
            output.append(0 if line == '' else number)
        else:
            output[i] += 0 if line == '' else number
    return output

if __name__ == "__main__":
    input = open("day1_input.txt", "r").read().split('\n')
    elf_maximums = elf_maximums(input)

    print(f"Solution: {max(elf_maximums)}")
    print(f"Solution2: {sum(sorted(elf_maximums, reverse=True)[:3])}")
