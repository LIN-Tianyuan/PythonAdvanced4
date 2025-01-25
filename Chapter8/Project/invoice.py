"""
# Method 1
fw = open("bill.txt.bak", "w")
fr = open("bill.txt", "r")
for line in fr:
    content = line.count('test')
    if content == 1:
        continue
    fw.write(line)
fw.close()
fr.close()
"""
"""
# Method 2
fw = open("bill.txt.bak", "w")
fr = open("bill.txt", "r")
for line in fr:
    if "test" not in line:
        fw.write(line)
fw.flush()
fw.close()
fr.close()
"""
with open("bill.txt.bak", "w") as fw:
    with open("bill.txt", "r") as fr:
        for line in fr:
            if "test" not in line:
                fw.write(line)
        fw.flush()