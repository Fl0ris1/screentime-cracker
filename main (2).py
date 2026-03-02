file = open("combinations.txt", "w")

posx=[0,100,200,300,400,500,600,700,800,900]
posy=[0,100,200,300,400,500,600,700,800,900]
count = 0
rows = 10
codes=[]

for i in range(10000):
    # :04d formats the integer to be 4 digits long, padding with leading zeros

    count += 1
    if count == rows:
        file.write(f"{i:04d}\n")
        count = 0

    else:
        file.write(f"{i:04d} ")
        
    codes.append(f"{i:04d}")
    
"""for i in range(len(codes)):
    file.write(codes[i])"""

code=list(str(codes[6309]))
for i in range(len(code)):
        print(f"goto x: {posx[int(code[i])]} y: {posy[int(code[i])]}")