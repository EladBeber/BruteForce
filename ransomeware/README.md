
# Ransomware.exe

## Solution

After a quick search i could see few things.
1. With PEiD i can see that the file is packed with **UPX**.
2. After some encryptions with the file its looks like is xor all the file always with **4 bytes** :  
Example:The binary data of my file is **"41 41 41 41 41 41 41 41"** and the encrypted file is **"34 42 24 AF 34 42 24 AF"**  
So in this case it is XOR with **"75 03 65 ee 75 03 65 ee "** and the 4 bytes are 75 03 65 ee  


## Read the asm

1.In the main its check whether argc = 2 either exit probably..
2.call _access to check whether the file mode is **Read/write** , Either exit...



