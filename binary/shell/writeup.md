Writeup - shell
===============

The time limit for this challenge was originally 30 seconds, but we saw that it was
a little hard for the inexperienced CTFer, so we added an additional 30 seconds to
the challenge.

Anyhow when you login to this challenge, you are presented with a shell. It's a pretty
crappy shell as there is really no indication that you are inside one (just start spamming
and you may see that you are in a shell).

There is a file called flag inside the environment you are presented with, but it is a 
little hidden. Searching through the shell by hand may take a while (or will it). Fortunately,
there is a quicker way to find files with a particular name. I personally am used to doing
`find / | grep flag`, which may or may not be the correct way to do it. By running this, you
will see that there is a file called `/var/lib/www/html/flag`. Just cat the file, and there's
your flag! 
