#include <algorithm>
#include <cctype>
#include <cstddef>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <stack>
#include <string>

using namespace std;

/**
 * Class containing the data and functions for a single node in an expression
 * tree
 *
 * @param type - stores the type of the node, it can either be {0 : (operator),
 * 1: (operand)}
 * @param operator_ - stores the operator, values can be {+, -, *, /}. Present
 * only if type is 0
 * @param operand_ - stores the operand, the value is a non-negetive integers.
 * Present only if type is 1
 * @param left - link to the left child of the node
 * @param right - link to the right child of the node
 */
class ExprNode {
private:
  int type;
  char operator_;
  unsigned int operand_;
  ExprNode *left, *right;

public:
  /* Constructor definitions */
  ExprNode(unsigned int operand) {
    type = 1;
    operand_ = operand;
    operator_ = 0;
    left = NULL;
    right = NULL;
  }

  ExprNode(char op) {
    if (op == '+' || op == '-' || op == '*' || op == '/') {
      type = 0;
      operator_ = op;
      left = NULL;
      right = NULL;
    } else {
      throw invalid_argument("Invalid operator");
    }
  }

public:
  /* validates an operator */
  bool isOperator() {
    /* Implement your logic here */
    if (this->operator_ == '+' || this->operator_ == '-' ||
	this->operator_ == '*' || this->operator_ == '/')
      return true;
    return false;
  }

  /* get operator value */
  char getOperator() {
    /* Implement your logic here */
    return this->operator_;
  }

  /* get operand value */
  unsigned int getOperand() {
    /* Implement your logic here */
    return this->operand_;
  }

  /* get left child */
  ExprNode *getLeft() {
    /* Implement your logic here */
    return this->left;
  }

  /* get right child */
  ExprNode *getRight() {
    /* Implement your logic here */
    return this->right;
  }

  /* set left child */
  void setLeft(ExprNode *left) {
    /* Implement your logic here */
    this->left = left;
  }

  /* set right child */
  void setRight(ExprNode *right) {
    /* Implement your logic here */
    this->right = right;
  }
};

/**
 * Function to construct infix tree from expression
 *
 * @param exp - string expression for which tree is to be constructed
 * @param index - pointer to string index from where tree is to be constructed
 * @return node - returns root to infix expression tree
 */
ExprNode *buildInfixTree(string exp, int *index) {
  // Grammar: E -> (T)|N, T -> E op E
  ExprNode *root;

  // Check for E -> N, i.e., leaf nodes
  if (isdigit(exp[*index])) {
    int start = *index;
    while (isdigit(exp[*index]))
      (*index)++;

    unsigned int num = stoul(exp.substr(start, *index - start));
    root = new ExprNode(num);

  // Check for E -> (T), i.e., operator nodes
  } else if (exp[(*index)++] == '(') {
    ExprNode *left = buildInfixTree(exp, index);
    char op = exp[(*index)++];
    ExprNode *right = buildInfixTree(exp, index);
    (*index)++;

    root = new ExprNode(op);
    root->setLeft(left);
    root->setRight(right);

  } else {
    // cout << "Invalid Expression : Unable to create ExprTree" << endl;
    root = nullptr;
  }

  return root;
}

/**
 * Function to print pre order traversal for infix expression tree
 *
 * @param root - reference to the root of the infix tree
 * @returns - resultant expression string after pre order traversal
 */
string doPreOrder(ExprNode *root) {
  string result = "";

  // returns leaf node as it is
  if (root->getOperator() == 0)
    return to_string(root->getOperand());

  // returns operator node in postorder
  result += root->getOperator();
  result += " " + doPreOrder(root->getLeft());
  result += " " + doPreOrder(root->getRight());

  return result;
}

/**
 * Function to evaluate the expression tree using stacks
 *
 * @param root - reference to the root of the infix tree
 * @returns - result after expression is evaluated
 */
int evaluate(ExprNode *root) {
  switch (root->getOperator()) {
  case 0:
    return root->getOperand();
  case '+':
    return evaluate(root->getLeft()) + evaluate(root->getRight());
  case '-':
    return evaluate(root->getLeft()) - evaluate(root->getRight());
  case '*':
    return evaluate(root->getLeft()) * evaluate(root->getRight());
  case '/':
    return evaluate(root->getLeft()) / evaluate(root->getRight());
  default:
    return 0;
  }
}

int getIntMin() { return numeric_limits<int>::min(); }

/**
 * Checks whether a given
 * expression is a valid mathematical expression
 *
 * @param exp - expression string to be validated
 * @returns - true if the expression is valid, false otherwise
 */
bool isValid(string exp) {
  stack<char> st;

  /*
   * Grammar: E -> (T)|N, T -> E op E
   * top:  ( -> (, N
   * top:  N -> op, )
   * top: op -> (, N
   * top:  ) -> op, )
   * possible values in stack: '(', ')', 'o' -> operator, 'd' -> digit
   */
  for (int i = 0; i < exp.size(); i++) {

    // '(' cannot occur after ')' and 'd'
    if (exp[i] == '(') {
      if (!st.empty() && (st.top() == ')' || st.top() == 'd')) return false;
      st.push('(');

    // ')' cannot occur after '(' and 'o'
    } else if (exp[i] == ')') {
      if (st.empty() || st.top() == '(' || st.top() == 'o') return false;

      bool operatorFound = false;
      while (!st.empty() && st.top() != '(') {
	if (st.top() == 'o') operatorFound = true;
	st.pop();
      }
      // parentheses without any operators inside are invalid
      if (st.empty() || !operatorFound) return false;
      st.pop();
      st.push('d'); // expression inside parentheses evaluates to a number

    // 'o' cannot occur after '(' and 'o'
    } else if (exp[i] == '+' || exp[i] == '-' || exp[i] == '*' || exp[i] == '/') {
      if (st.empty() || st.top() == '(' || st.top() == 'o') return false;
      st.push('o');

    // 'd' cannot occur after ')'
    } else if (isdigit(exp[i])) {
      if (st.empty() || st.top() == ')') return false;
      st.push('d');
      // traverse all digits of the number
      while (i < 1 + exp.size() && isdigit(exp[i + 1])) i++;

    } else {
      return false; // unexpected character
    }
  }
  if (st.size() == 1 && st.top() == 'd')
    return true;
  return false;
  // if (!st.empty() && (st.size() != 1 || st.top() != 'd')) return false;
  // return true;
}

/**
 * Function to print output to console
 * @param result - result from evaluating validity of expression
 */
void printResultA(bool result) {
  cout << "1a:" << (result ? "true" : "false") << endl;
}

/**
 * Function to print output to console
 * @param result - expression from the pre order traversal
 */
void printResultB(string result) { cout << "1b:" << result << endl; }

/**
 * Function to print output to console
 * @param result - result after evaluation of expression
 */
void printResultC(int result) { cout << "1c:" << result << endl; }

int main() {
  /* Expression string */
  string input_exp;

  /* Input taken from console */
  getline(cin, input_exp);

  /* Create a new string without spaces from the input string */
  string exp;
  copy_if(input_exp.begin(), input_exp.end(), back_inserter(exp),
	  [](char c) { return (c != ' '); });

  /**
   * QUESTION 1 - PART A
   *
   * Check if the given expression is a valid mathematical expression
   */

  /* Validate expression */
  bool check = isValid(exp);

  /* Printing result to console */
  printResultA(check);

  /**
   * QUESTION 1 - PART B
   *
   * Build an infix expession tree for the given expression and
   * print the result of a pre order traversal on the expression tree
   *
   * Root : must be an operator
   * Left-subtree: sub expression
   * Right-subtree: sub expression
   * Leaves: integer operands
   *
   */

  ExprNode *root;
  string preOrderResult = "NA";
  if (check) {
    /* Construct infix expression tree */
    int index = 0;
    root = buildInfixTree(exp, &index);

    /* Print pre order traversal */
    preOrderResult = doPreOrder(root);
  }

  /* Printing result to console */
  printResultB(preOrderResult);

  /**
   * QUESTION 1 - PART C
   *
   * Check if the given expression is a valid mathematical expression
   */

  int result = getIntMin();

  /* Evaluate infix expression tree */
  if (check)
    result = evaluate(root);

  /* Printing result to console */
  printResultC(result);

  return 0;
}
