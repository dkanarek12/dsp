# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

pwd - prints the current directory path /n
ls - lists the files/directories located in the current directory \n
cd - changes the current directory
pushd/popd - adds/removes a directory to a queue allowing the user to quickly swithc between working directories
man - displays a help manual
find  - locates files/directories
rm - deletes files
rmdir - deletes directories
mv - moves files/directories to another location
less - displays contents of a file

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

ls -a : lists all files/directories as well as files/directories within the directories
ls -l : lists properties of files/directories in the current directory
ls -lh : same as above byt file sizes are abbreviated

The -a and -l flag together will list the properties of all files in the cuurenty directory tree

---



---

What does `xargs` do? Give an example of how to use it.

The 'xargs' command executes a series of arguments.

$ Echo 1 2 3 4 | xargs

This will execute the Echo commands for the arguments 1, 2, 3, and 4.
 
---

