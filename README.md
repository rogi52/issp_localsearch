# Speeding up Local Search for the Indicator-based Subset Selection Problem by a Candidate List Strategy
This repository provides the C++ code used in the following paper:
> Speeding up Local Search for the Indicator-based Subset Selection Problem by a Candidate List Strategy

# Requirements
I compiled this code with gcc version 11 on the Ubuntu 22.04. Python 3 is needed to run "run.py". 

# Usage
## Compile
```
$ git clone https://github.com/rogi52/issp_localsearch.git
$ cd issp_localsearch
$ make
```

## Simple exapmle
```
$ python gen_connected.py --mode demo
$ python issp.py -d 2 -pf linear -n 1000 -I hv -r 1.1 -R 1000 -W 1000 -k 100 -alg fils-rlist-nlist -ln 20 -lr 20 -id 0
```

The first command runs a generator of point set such that:
- The number of objectives is $2$
- The shape of Pareto front is linear
- Point set size is $1000$

The second command runs local search with two neighbour list for an ISSP. 
The parameters of the ISSP are as follows:
- The number of objectives `-d` : $2$
- The shape of Pareto front `-pf` : linear
- Point set size `-n` : $1000$
- Indicator `-I` : hypervolume `hv` 
- Reference point of hypervolume `-r` : $1.1$
- Subset size `-k` : $100$
- Selector's algorithm `-alg` : local search with nearest neighbour list and random neighbour list `fils-rlist-nlist`
- Nearest neighbour list size `-ln` : $20$
- Random neighbour list size `-lr` : $20$
- Run ID (and for seed) `-id` : 0

## Reproduce results presented in the paper (YET)
```
$ python run_all.py
```
Note that this requires a high computational cost. 