import statistics


Counter = 0
Can_ids = set()
framesD = {}
timestamps = {}
payloads = {}


print("KYRYL YERMOCHENKO SCRYPT 1")
print("...")
print("...")
print("CALCULATED PREIODS FOR ALL CAN_IDs")

# with open("idle1.log, "r") as file
with open("left.log", "r") as file:
    for line in file:
         parts = (line.split()) 
         PARTS = (parts[2].split("#"))         
         Frame = PARTS[0]
         Payload = PARTS[1]
         framesD[Frame] = framesD.get(Frame, 0) + 1
         Can_ids.add (Frame)
         Counter = Counter + 1

         timestamps.setdefault(Frame, []).append(float(parts[0].strip("()")))
         payloads.setdefault(Frame, set()).add(Payload)
 
# !Those are my tests! #


# first_five = timestamps["158"][:5]

# for i in range(len(first_five) -1):
#          Time_DIF_temp = (first_five[i+1] - first_five[i]) * 1000
#          print("Time_Difference:", Time_DIF_temp)

# all_times = timestamps["158"]

# for i in range(len(all_times) - 1):
#          Time_DIF_temp = (all_times[i+1] - all_times[i]) * 1000
#          intervals.append(float(Time_DIF_temp))


# !Those are my tests! #



for can_id, all_times in timestamps.items():
    intervals = []

    for i in range(len(all_times) - 1):
        time_diff = (all_times[i+1] - all_times[i]) * 1000
        intervals.append(time_diff)

    median_period = statistics.median(intervals)
    min_period = min(intervals)
    max_period = max(intervals)

    long_intervals = 0

    for interval in intervals:
        if interval > 2 * median_period:
            long_intervals = long_intervals + 1

    print("CAN_ID:", can_id,
		"Median:", round(median_period, 3), "ms",
		"Min:", round(min_period, 3), "ms",
		"Max:", round(max_period, 3), "ms",
		"Long intervals:", long_intervals,
		"Intervals:", len(intervals))


#for  can_idD, countD in framesD.items():
#    print("CAN_ID: ", can_idD, countD)

print("")
print("")
print("")
print("TOTAL of CAN Frames:", Counter)
print("Number of Unique IDs:", len(Can_ids))
print("")
print("UNIQUE PAYLOADS PERC CAN_ID")

for can_id, unique_payloads in payloads.items():
    print("CAN_ID:", can_id, "Unique payloads:", len(unique_payloads))
