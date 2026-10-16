import sys

# Com-line arguments
Input_file = sys.argv[1]
Output_file = sys.argv[2]
Allowed_ids = set(sys.argv[3:])

counter = 0

with open(Input_file, "r") as sources:
    with open(Output_file, "w") as destination:

        for line in sources:
            parts = line.split()

            can_id = parts[2].split("#")[0]

            if can_id in Allowed_ids:
                destination.write(line)
                counter += 1

print("FILTER COMPLETED")
print("Input:", Input_file)
print("Output:", Output_file)
print("Selected IDs:", sorted(Allowed_ids))
print("Frames saved:", counter)

