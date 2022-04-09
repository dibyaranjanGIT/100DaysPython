file = open("file.txt", mode="w")
file.write("Hello World !")
file.close()

with open("file.txt","r") as f:
    content=f.read()
    print(content)