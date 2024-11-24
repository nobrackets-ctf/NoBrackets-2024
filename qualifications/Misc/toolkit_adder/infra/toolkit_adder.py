print("\033[38;5;33mTOOLKIT ADDER")
print("Send code that can change the world!")
print("____________________________________\033[0m")
print("Write your python function(s) line by line, write 'END' to finish and send:")

# Get input line by line
t = []
while (nl:=input("> ")) != "END":
    t+=[nl]


# Check if only functions are defined
for l in t:
    if l and not l.startswith(("def", "\t", "@"," ","  ","   ")):
        print("\033[38;5;160mPlease only give functions as input!\033[0m\nExemple:\n\t\tdef x():\n\t\t\tprint('hello world')\n")
        exit()
func = '\n'.join(t)

# Check if there is no compilation error
try:
    exec(func)
except Exception as e:
    print("\033[38;5;160m/!\\ Error :", e, "\033[0m")
    exit()


# Add function to the toolkit
with open("/app/toolkit.py","a") as f:
    f.write("\n\n"+func)


print("\n\033[38;5;36mYour function:\033[0m")
print(func)
print("\033[38;5;36mhas been sucessfully added! Good job!\033[0m")
