
# Ransomware.exe

## Solution

After a quick search i could see few things.
1. With PEiD i can see that the file is packed with **UPX**.
2. After some encryptions with the file its looks like is xor all the file always with **4 bytes** :  
Example:The binary data of my file is **"41 41 41 41 41 41 41 41"** and the encrypted file is **"34 42 24 AF 34 42 24 AF"**  
So in this case it is XOR with **"75 03 65 ee 75 03 65 ee "** and the 4 bytes are **0x75 0x03 0x65 0xee**  


#### Read the asm

1.In the main its check whether argc = 2 either exit.  
2.call _access to check whether the file mode is **Read/write** , Either exit.
3. Calling "_encrypt_file" define in the stack all relevant variables.  
4.Reading file , loading to input_file the bytes from 0 to seek_end jump if zero , zero - success.  
5.calling fseek and after ftell.If the size of the file equal to 0FFFFFFFFh(4294967295d) exit.  
6. Writing into ecx all the file data with fread,Checking if all the data has been writed to ecx and continue.Else exit.


#### Creating The Key !!!
1.key = ((((0EEEEh+file_size) << 10h)+0FFFFh)file_size).    
2.If edx(0) > file size then jump , We are not jump ! 







