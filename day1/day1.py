def elf_maximums(input):
    output = []
    i = 0
    for line in input:
        if line == "":
            i += 1
            continue
        
        number = int(line)

        if len(output) <= i:
            output.append(0 if line == '' else number)
        else:
            output[i] += 0 if line == '' else number
    return output

if __name__ == "__main__":
    input = open("input.txt", "r").read().split('\n')
    elf_maximums = elf_maximums(input)

    print(f"Solution: {max(elf_maximums)}")
    print(f"Solution2: {sum(sorted(elf_maximums, reverse=True)[:3])}")
