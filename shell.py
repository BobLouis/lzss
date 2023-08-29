import os
import subprocess

# Get all files that start with "BLOCK"
files = [f for f in os.listdir() if f.startswith('BLOCK')]
subprocess.run(["gcc", "lzss.c", "-o", "lzss"])
subprocess.run(["gcc", "lzss_split.c", "-o", "lzss_split"])

sum = 0
for file in files:
    # Echo the filename
    print(file)

    # Execute the trans.py with --split argument
    subprocess.run(["python3", "trans.py", file, "--split"])
    # Execute the trans.py without any argument after file
    subprocess.run(["python3", "trans.py", file])

    # compress all
    print("compress all")
    subprocess.run(["./lzss", "e", "output.txt", "compress.txt"])
    all_total_output = subprocess.run(["./lzss", "e", "output.txt", "compress.txt"], capture_output=True, text=True).stdout
    all_total = int(all_total_output.split('total:')[1].split()[0])

    # split
    print("split")
    split_total_output = subprocess.run(["./lzss_split", "e", "data.txt", "compress.txt"], capture_output=True, text=True).stdout
    subprocess.run(["./lzss_split", "e", "data.txt", "compress.txt"])
    split_total = int(split_total_output.split('total:')[1].split()[0])

    sum += min(all_total, split_total)

print("all sum", sum)
