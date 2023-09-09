# Python Testing!

In this repo, I try to figureout that what is testing, and how it feels when programs are under tests and then pass all of them!

This repo can use as a simple examples for those of python programmers that are new to testing and they want to have basic to advance examples.

## Unittest Examples:

1. Ex-1: chunked method

I have code a function like itertools.chunked method, and focus on testing this function by unittest module. 

For Run Tests, just run test_chunked.py file, or use command below when you are in Ex-1/ direcoty:

```
python3 -m unittest -v test_chunked.py
```

## Doctest Examples:
1. Ex-1: factorial

In Ex-1/factorial.py We have a function called 'factorial' that calculate factorial for us, for testing this module, you should move your terminal path in doctest/Ex-1/ and run command below:

```
python3 -m doctest -v factorial.py
```