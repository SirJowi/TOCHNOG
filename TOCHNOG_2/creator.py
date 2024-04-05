import os

start_directory = os.getcwd()

def checkFiles(inputPart):
    if not os.path.isfile(inputPart):
        print(inputPart + " is missing.")
        return False
    else:
        print(inputPart + " is found.")
        return True

# Check and combine files
file_parts = ["header", "init", "geometry", "materi", "boundaries", "mesh", "simulation" ]
combined_content = ""

for part in file_parts:
    if checkFiles(part):
        with open(part, 'r') as file:
            combined_content += file.read() + "\n"

# Write the combined content to creation.dat
if os.path.isfile("creation.dat"):
    print("creation.dat already exists. Clearing its contents.")

    with open("creation.dat", 'w') as file:
        file.write("")

with open("creation.dat", 'a') as file:
    file.write(combined_content)

print("Contents of creation.dat:")
print(combined_content)
