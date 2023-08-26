## Programming assignment: DS221: INTRO TO SCALABLE SYSTEMS 

### POINTS: 150
```diff
Due date: Sept 23 6:00 PM
- *No extension will be granted*
```
-----------------------
### Question 1
#### Expression Evaluation using Trees and Stacks (90 points)

You are given a mathematical expression as a string that is read from console input. The expression will be composed of four binary operators + - * / and non-negative integers as operands. Each sub-expression formed from a operator will be enclosed within parenthesis, i.e., (L op R) where L is the left operand, op is the operator and R is the right operand. There may be zero or more spaces between the operators, operands and parenthesis.

* (a) Use a C++ STL stack data structure to verify if the given expression is valid. You should print the output "1a:true" or "1a:false" accordingly. (20 points)
* (b) Define a Tree data structure in C++ by implementing the virtual functions defined in the abstract class provided to you. Build an expression tree using the given input expression. The root must be an operator, its left and right subtrees must be its sub-expression, internal nodes should be operators and leaves must be integer operands. Parenthesis must not be placed in the node. Perform a pre-order traversal of the expression tree and print it to the console output as "1b:op L R ...". A space must separate the operators and operands. Do not print parentheses. (30 points)
* (c) Evaluate the expression tree you have constructed using an STL stack data structure. You should use default C++ integer-based arithmetic in all steps of your evaluation (i.e., NOT float or double). You should print the result of the expression tree as: "1c:123456" where 123456 is the output of evaluating the expression.(Print the value of [INT_MIN](tests/t3/q1o3.txt) if the expression was an invalid one. A suitable function is already provided in the skeleton code) (40 points)

Your main C++ program should be in the file `ExprTree.cpp` and the generated executable should be named `ExprTree`. A sample outline for `ExprTree.cpp` is provided. Your program will be executed and tested by an automated script like the following way
```
echo "((10 + 5) + (20/3))" | ./ExprTree    OR
cat <expression text file> | ./ExprTree
```
In the above example, your program should print the following output:
```
1a:true
1b:+ + 10 5 / 20 3
1c:21
```

-----------------------
### Question 2
#### Searching using arrays (60 points + 20 points extra credit)
You are given a input file with n+1 rows. The first line has a non-negative integer that indicates a count of the input numbers in the file 'n' and the remaining 'n' rows have an input integer each. As a first step, write C++ code to compactly insert these numbers into a binary tree implemented as an array.

* a) You are also given a separate _query_ file with m+1 numbers, one per line. The first line has a non-negative integer that indicates a count of the numbers in the file 'm' and remaining 'm' rows have a query integer each. Write an efficient C++ code to search for each number in this query file within the binary tree by performing:
  1. an in-order traversal, and 
  2. level-order traversal. 
* Measure the time taken to complete the search for all queried numbers using each strategy. Print to console output `2a:123,456,789` where 123<=m is a count of the queried numbers that were successfully found in the tree, 456 is the total time taken in **milliseconds** to complete all searches using in-order traversal, and 789 is the total time taken in milliseconds to complete all searches using level-order traversal. [30 points]

* b) For at least 3 different sizes of the input file, estimate the space taken by the array and the time taken by the two search strategies. You will need to create large inputs for a proper evaluation. Compare the observed figures with the expected space and time complexities. Provide a report with plots, comparisons and analysis of the observations. Explain any outliers. [30 points]

* c) Optionally, sort and store the input numbers in a sorted array. You may use the sort() function over arrays in C++ STL. Perform a binary search over this sorted array for the input queries. Print your output as "2c:345", where 345 is the total time taken for the binary search of all numbers to complete. Include an analysis of these results in your report. (EXTRA CREDIT: 20 points)

Your main program should be in the `TreeSearch.cpp` file and the generated executable should be named `TreeSearch`. Your program will be executed and tested by an automated script like the following way
```
./TreeSearch <input file name> <query file name>
```
-----------------------
### How to complete assignment?
* Start by [downloading](https://github.com/DS221-2022/Assignment/archive/refs/heads/master.zip) the code outline for ExprTree.cpp, TreeSearch.h and TreeSearch.cpp files. You can make changes to the cpp files. Make sure your code is well documented. Maintain good coding practices (indenting, comments, validations, etc.)
* Three test cases (expr1.txt, num1.txt, query1.txt, ...) are available. These test cases will be different from the ones which will be used while correcting your assignments and you are expected to run your code on other sample data of your own.
* Evaluation of the code will be done using automated scripts. This means you **must** follow instructions for compilation using Makefile, input format and console output format. If the automated compilation/evaluation fail, your assignment will not be evaluated.
* You should compile the code using the given Makefiles for each part of the assignment. Use gcc [version 9.1 ](https://lwn.net/Articles/787385/) or above. Do not change the Makefiles. We will compile your submission from source.
* Follow the console output format accurately as listed in the problem. You MUST NOT print anything else to the console output other than what is listed in the question. 
* Your solution should have the following folder structure and these exact file names. Nothing more, nothing less.
```
report.pdf
.gitignore
q1/
  makefile
  ExprTree.cpp
q2/
  makefile
  TreeSearch.h
  TreeSearch.cpp
```   
* You must host your solution as a **private** repository named "DS221-2022-YourIIScEmailAlias" on GitHub. Regularly push your code changes to GitHub. If you lose your code in your local machine due to any fault, you will not lose progress if your code is regularly backed up on GitHub. 
  
-----------------------
### How to submit assignment?
* Once your code is complete, [do a sanity check](tests/checkCompilation.md) to make sure that your submission is compatible with our automated testing framework.
* After checking the compatibility, you should [transfer the ownership of your private GitHub repository](https://docs.github.com/en/github/administering-a-repository/managing-repository-settings/transferring-a-repository#transferring-a-repository-owned-by-your-user-account) to `jyotshna-atcg`. Transfers made after deadline will be ignored.
* Start early, do not wait until the deadline.

-----------------------
### Policy
* Do not host your solutions on your GitHub public repository or any public online repository. Any student found posting their solutions in a public repository will get zero points for this assignment, besides other penalties. 
* Secure your account on the Turing cluster by using a personal password.
* Do not review or use code from others (including online sources) when developing your solution. Do not show your code to others.
* If you need help with programming or understanding a lecture topic, you can request an appointment with the instructor or the TA.
* Please comply with the IISc ethics policy.
