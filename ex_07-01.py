fname = input("Enter file name: ")
count = 0
total = 0

try:
    fhand = open(fname)
except:
    print("File not found:", fname)
    quit()

for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        total += float(line.split()[1])

if count > 0:
    print("Average spam confidence:", total/count)
else:
    print("No lines found starting with 'X-DSPAM-Confidence:' in", fname)

    