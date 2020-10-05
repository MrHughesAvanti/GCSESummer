name = input("Whats your name")




myfile = open("file.txt","a")

myfile.write(name)

myfile = open("file.txt","r")

names = myfile.readlines()

print(names)



