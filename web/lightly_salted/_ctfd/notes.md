### HOW TO SOLVE ###
1. enter in any password. note that the error message shows a hash of your input as well as the expected hash.
2. figure out the hash algorithm after several attempts. specifically, it's the  base 16 difference (mod 16) between the ascii values of each character; with the string "salty" appended to the input
3. construct a password matching the given hash (such as 'fishandchips', the original password)
4. enter password into site, resulting page contains flag

