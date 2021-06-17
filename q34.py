'''
GCD OF GIVEN INDEX RANGE IN AN ARRAY

given an array a[0...n-1]. we should be able to efficiently find the GCD
from index qs(query start) to qe (query end) where 0 <= qs <= qe <= n-1

Input : a[] = {2, 3, 60, 90, 50};
        Index Ranges : {1, 3}, {2, 4}, {0, 2}
Output: GCDs of given ranges are 3, 10, 1

A simple solution is to run a loop from qs to qe and find GCD in given range. 
This solution takes O(n) time in worst case.

Method 2 (2D Array)

Another solution is to create a 2D array where an entry [i, j]
stores the GCD in range arr[i..j]. GCD of a given range can now be calculated 
in O(1) time, but preprocessing takes O(n^2) time. Also, this approach needs 
O(n^2) extra space which may become huge for large input arrays.

Method 3 (Segment Tree)

Prerequisites : Segment Tree Set 1, Segment Tree Set 2
Segment tree can be used to do preprocessing and query in moderate time. 
With segment tree, preprocessing time is O(n) and time to for GCD query is O(Logn). 
The extra space required is O(n) to store the segment tree.

Representation of Segment trees

Leaf Nodes are the elements of the input array.
Each internal node represents GCD of all leaves under it.
Array representation of tree is used to represent Segment Trees i.e., for each node at index i,
Left child is at index 2*i+1
Right child at 2*i+2 and the parent is at floor((i-1)/2).

Construction of Segment Tree from given array

Begin with a segment arr[0 . . . n-1] and keep dividing into two halves. Every time we divide the current segment into two halves (if it has not yet become a segment of length 1), then call the same procedure on both halves, and for each such segment, we store the GCD value in a segment tree node.
All levels of the constructed segment tree will be completely filled except the last level. Also, the tree will be a Full Binary Tree (every node has 0 or two children) because we always divide segments in two halves at every level.
Since the constructed tree is always full binary tree with n leaves, there will be n-1 internal nodes. So total number of nodes will be 2*n – 1.
Height of the segment tree will be &lceillog2n&rceil. Since the tree is represented using array and relation between parent and child indexes must be maintained, size of memory allocated for segment tree will be 2*2⌈log2n⌉ – 1

Query for GCD of given range

/ qs --> query start index, qe --> query end index
int GCD(node, qs, qe)
{
   if range of node is within qs and qe
      return value in node
   else if range of node is completely 
      outside qs and qe
      return INFINITE
   else
      return GCD( GCD(node's left child, qs, qe), 
                  GCD(node's right child, qs, qe) )
}

'''