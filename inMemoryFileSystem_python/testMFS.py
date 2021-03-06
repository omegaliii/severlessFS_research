from memoryFS import *

print("Making two directory under the root.")
mkdir("/dir1")
mkdir("/dir2")
print("list the root:")
ls("/")
print("======================================")

print("Creating a test.txt file under dir1")
create("/dir1/test.txt")
print("list dir1:")
ls("/dir1")
print("======================================")

print("Open the test.txt file")
openFile("/dir1/test.txt",'rw')
print("======================================")

print("Read test.txt file")
read("/dir1/test.txt")
print("Writing dir1")
write("/dir1/test.txt", "hello \n world")
print("Read test.txt file again:")
read("/dir1/test.txt")
print("Readline test.txt file:")
readline("/dir1/test.txt")
print("======================================")

print("Remove dir1.")
rmdir("/dir1")
print("list root:")
ls("/")
print("======================================")