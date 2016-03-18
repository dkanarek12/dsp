# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists are dynamics and can have elements added. Tuples are immutable
and therefore can be used as keys to dictionaries.  

Both use indexing to find elements within them.  

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Sets contain unordered, unique elements. It takes O(1) time to find an 
element in a set since elemnts are stored in a hashtable. It takes O(n) time to 
find an elements in a list. 

A = [1, 2, 2, 3]
set(A) = [2, 1, 3]


---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Lambda functions are anonymous functions that can be quickly created and do
not need to be assigned a name.

Ex) sorted(tuples,key=lambda t: t[-1])

where tuples is a list of tuples will sort the list ausing the last element in 
each tuple as the key.


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions are quick ways to create a list based on a function of 
the elements and is evaluated faster than map when a lambda function is needed.

Ex) squares = [x**2 for x in range(5)] #squares = [0, 1, 4, 9, 16]

Dictionaries and sets can also be created quickly using comprehensions.

Ex) d = {x:x**2 for x in range(5)} # d = {0:0, 1:1, 2:4, 3:9, 4:16}
Ex) s = {x for x in 'hello world'}   # s = set(['h','e','l','o','w','r','d'])

Map applies a function to every element in a list and returns a list of the results
 
Ex) squares = map(lambda x: x**2,range(5))  #squares = [0, 1, 4, 9, 16]

Filter constructs a list from another list where the applied function returns true

Ex) squares = filter(lambda x: sqrt(x)/x == 1.0,range(20)) #squares = [0, 1, 4, 9, 16]

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

936 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

512 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

7849 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





