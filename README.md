# README #

## What is this repository for? ##

This repository contains 2 Python Programs. 1st is a Digraph generator and the 2nd displays specific information about a Digraph.

Program A) Generates a digraph based on user input for number of vertices and if the graph is connected or not. If there are no system arguments then program randomly generates a Digraph.

Program B) Takes in user inputted edges to form a digraph and can take a start and end point to find a path in the Digraph to the point. 

## How do I get set up? ##

Instructions in this README file are for a Windows 11 environment

### Configuration ###

1. Clone and open the repository:

```
$ git clone https://github.com/coleyadron/DiGraph.git
```

2. Change the directory

```
$ cd DiGraph
```

3. Run Executable for Part A 

To generate with a specifc number vertices the first system argument must be a number and the second system argument must be "connected" for the digraph to be connected.

Example with System Arguments - $ python digraph.py 7 conncected or $ python digraph 14 not

```
$ python digraph.py
```

4. Run Executable for Part B:

To find a desired path from a start point to end point they must be entered as system arguments. In which the first system argument is the start and the second system argument is the end

Example with System Arguments - $ python pathDigraph.py a1 q3

If there is no system arguments the program will not find a path

```
$ python pathDigraph.py
```

### License ###

[GNU Public License](https://www.gnu.org/licenses/gpt-3.0.html)

### Who do I talk to? ###

Email cyadron@hawk.iit.edu