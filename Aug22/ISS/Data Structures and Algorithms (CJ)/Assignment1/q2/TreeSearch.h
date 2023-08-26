using namespace std;

/**
 * Class to build a Binary tree and traverse it to find an element
 *
 * @param treeArr - pointer to array that stores the elements of tree
 * @param sortedArr - pointer to array that stores the sorted elements
 * @param size - total number of elements in tree
 */
class BinaryTree {
  private:
    int *treeArr;
    int *sortedArr; // Optional: Extra Credit
    int size;
    int capacity;

  public:
    // constructor
    BinaryTree(int size_);
    int insert(int key); // insert lever order
    int insertSorted(int *keys); // insert all keys in sorted order // Optional: Extra Credit
    int findByInOrder(int key, int from);
    int findByLevelOrder(int key);
    int findByBinarySearch(int key); // Optional: Extra Credit
};
