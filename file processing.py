name = input("Whats your name")




myfile = open("file.txt","a")



myfile = open("file.txt","r")

names = myfile.readlines()

print(names)


myfile.write(name)
