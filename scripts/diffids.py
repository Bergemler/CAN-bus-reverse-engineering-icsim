import sys

file1 = sys.argv[1]
file2 = sys.argv[2]


ids1 = set()
ids2 = set()

payloads1 = {}
payloads2 = {}



with open(file1, "r") as file:
    for line in file:
        parts = line.split()
        can_id, payload = parts[2].split("#", 1)
        ids1.add(can_id)
        payloads1.setdefault(can_id, set()).add(payload)

with open(file2, "r") as file:
    for line in file:
        parts = line.split()
        can_id, payload = parts[2].split("#", 1)
        ids2.add(can_id)
        payloads2.setdefault(can_id, set()).add(payload)

common_ids = ids1 & ids2
only_first = ids1 - ids2
only_second = ids2 - ids1

print("Common IDs:", len(common_ids))
print("Only in file1:", sorted(only_first))
print("Only in file2:", sorted(only_second))



print("\nPAYLOAD COMPARISON")

for can_id in sorted(common_ids):
    first = payloads1[can_id]
    second = payloads2[can_id]

    new_payloads = second - first
    missing_payloads = first - second

    if new_payloads or missing_payloads:
        print(
            "CAN_ID:", can_id,
            "New:", len(new_payloads),
            "Missing:", len(missing_payloads)
        )

    if can_id == "188":
        print("  New payloads:", sorted(new_payloads))
        print("  Missing payloads:", sorted(missing_payloads))
