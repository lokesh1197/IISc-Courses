### Test whether your code is compatible with our testing framework
All codes will be run and tested on the Turing cluster. In the commands below, we suppose that your email id is `YourIIScEmailAlias@iisc.ac.in`, and your github ID is `YourGitAccountID`

```
ssh YourIIScEmailAlias@turing.cds.iisc.ac.in
mkdir test-compatibility
cd test-compatibility
git clone https://github.com/YourGitAccountID/DS221-2022-YourIIScEmailAlias/
cd DS221-2022-YourIIScEmailAlias/q1
make clean
make CXX="g++-9"
wget https://raw.githubusercontent.com/DS221-2022/Assignment/master/tests/t1/expr1.txt
cat expr1.txt | ./ExprTree 
cd ../q2
make clean
make CXX="g++-9"
wget https://raw.githubusercontent.com/DS221-2022/Assignment/master/tests/t1/num1.txt
wget https://raw.githubusercontent.com/DS221-2022/Assignment/master/tests/t1/query1.txt
./TreeSearch num1.txt query1.txt  
```

If this was your first login to the Turing cluster, do not forget to setup your personal password by using `passwd` command. In the Turing cluster, default `g++` compiler for C++ is old.  An updated C++ compiler `g++-9` can be used instead, as done above.
