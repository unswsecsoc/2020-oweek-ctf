### NOTES ###
Challenge runs on `localhost:8000`, change port (or host) as required
There is *Dockerfile* to copy files and run NodeJS with `npm`

### HOW TO SOLVE ###
>>> flag[0:8]   part 1
'OWEEK{bu'   : open "index.html" source
>>> flag[8:16]  part 2
'1lding_W'   : check "stylesheet.css"
>>> flag[16:24] part 3
'3b5ite_i'   : set "admin" cookie to true and check "flag3/4" cookie
>>> flag[24:]   part 4
'S_k00L!}'   : click button on box on "http://localhost:8000/findflag"
