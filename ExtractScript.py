# How to write: "","text","Emotion(H, S, A, N)","","","","",""

with open("FinProj/RomCom.txt") as file:
    lines = file.readlines()

write = open("./convertcsv.csv", "a")
for line in lines:
    if len(line) >= 8:
        write.write(f'"","{line}","","","","",""\n')

write.close()

