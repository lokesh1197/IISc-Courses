#include <queue>
#include <stack>
#include "TreeSearch.h"
#include <iostream>
#include <fstream>
#include <chrono>
#include <algorithm>
using namespace std;

/**
 * Constructor to instantiate the array
 * @param size_ - number of elements in tree
 */
BinaryTree::BinaryTree(int size_){
  int a[size_];
  this->treeArr = a;
  this->size = 0; // maintains current index
  this->capacity = size_;
}

/**
 * Function to insert an element into the tree in level order
 * @param key - element to be inserted
 * @return 0 if insert was success, -1 if it failed
 */
int BinaryTree::insert(int key){
  if (this->size == this->capacity) return -1;

  this->treeArr[this->size] = key;
  (this->size)++;
  return 0;
}

/**
 * Function to find the key by performing an inorder order traversal of the tree
 * @param key - key to be searched for in the tree
 * @return value - return the index of the key (starting at 1) if found else
 * return -1
 */
int BinaryTree::findByInOrder(int key, int from = 0) {
  int leftIndex = (2*from) + 1;
  int rightIndex = leftIndex + 1;
  int left = leftIndex < this->size ? findByInOrder(key, leftIndex) : -1;

  if (left != -1) return left;
  if (this->treeArr[from] == key) return from;

  return rightIndex < this->size ? findByInOrder(key, rightIndex) : -1;
}

/**
 * Function to find the key by performing a level order traversal of the tree
 * @param key - key to be searched for in the tree
 * @return value - return the index of the key (starting at 1) if found else return -1
 */
int BinaryTree::findByLevelOrder(int key){
  for (int i = 0; i < this->size; i++) {
    if (this->treeArr[i] == key) return i + 1;
  }
  return -1;
}

/**
 * Optional: Extra Credit
 * Function to insert all elements as a sorted array
 * @param keys - elements to be inserted in sorted order
 * @return 0 if insert was success, -1 if it failed
 */
int BinaryTree::insertSorted(int* keys) {
  this->treeArr = keys;
  this->size = this->capacity;
  sort(this->treeArr, this->treeArr + this->capacity);
  return 0;
}

/**
 * Optional: Extra Credit
 * Function to find the key by performing a binary search over sorted array
 * @param key - key to be searched for in the sorted array
 * @return value - return the index of the key (starting at 1) if found else return -1
 */
int BinaryTree::findByBinarySearch(int key){
  int min = 0, max = this->size;

  for (int n = (min + max)/2; min < max; n = (min + max)/2) {
    if (this->treeArr[n] == key) return n;
    if (this->treeArr[n] > key) max = n;
    else min = n + 1;
  }

  return -1;
}

int main(int argc, char *argv[]){
  // return if insufficient arguments
  if (argc <= 2) return 0;

  // read from input number and query files using the file name passed in as inputs
  ifstream input_file(argv[1]);
  int ni;
  input_file >> ni;
  BinaryTree *head = new BinaryTree(ni);

  // insert each input number into the tree
  int input[ni];
  for (int i = 0; i < ni; i++) {
    input_file >> input[i];
    head->insert(input[i]);
  }

  // store queries in an array
  ifstream query_file(argv[2]);
  int nq;
  query_file >> nq;

  int queries[nq];
  for (int i = 0; i < nq; i++) {
    query_file >> queries[i];
  }

  // iterate and search for each query number using inorder traversal
  // measure the total time taken to search all the numbers using inorder
  int count_inorder = 0;
  auto start_inorder = chrono::high_resolution_clock::now();
  for (int i = 0; i < nq; i++) {
    if (head->findByInOrder(queries[i]) != -1) count_inorder++;
  }
  auto stop_inorder = chrono::high_resolution_clock::now();
  auto duration_inorder = chrono::duration_cast<chrono::milliseconds>(stop_inorder - start_inorder);

  // iterate and search for each query number using level-order traversal
  // measure the total time taken to search all the numbers using level-order
  int count_levelorder = 0;
  auto start_levelorder = chrono::high_resolution_clock::now();
  for (int i = 0; i < nq; i++) {
    if (head->findByLevelOrder(queries[i]) != -1) count_levelorder++;
  }
  auto stop_levelorder = chrono::high_resolution_clock::now();
  auto duration_levelorder = chrono::duration_cast<chrono::milliseconds>(stop_levelorder - start_levelorder);

  // output in the format "2a:123,456,789" where:
  // 123<=m is the number matching query numbers found 
  // 456 is the total time taken in milliseconds to complete the search using inorder traversal, and 
  // 789 is the total time taken in milliseconds to complete this search using level-order traversal.
  cout << "2a:" << count_inorder << "," << duration_inorder.count() << "," << duration_levelorder.count() << endl;

  // insert sorted
  BinaryTree *sorted_tree = new BinaryTree(ni);
  sorted_tree->insertSorted(input); 

  // iterate and search for each query number using binary search traversal
  // measure the total time taken to search all the numbers using binary search
  int count_binary_search = 0;
  auto start_binary_search = chrono::high_resolution_clock::now();
  for (int i = 0; i < nq; i++) {
    if (sorted_tree->findByBinarySearch(queries[i]) != -1) count_binary_search++;
  }
  auto stop_binary_search = chrono::high_resolution_clock::now();
  auto duration_binary_search = chrono::duration_cast<chrono::milliseconds>(stop_binary_search - start_binary_search);

  cout << "2c:" << duration_binary_search.count();
  return 0;
}
