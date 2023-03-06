#include bits/stdc++.h>
using namespace std;
struct Node
{
  int data;
  Node *left, *right;
};
// function to create a new node
Node *newNode(int data)
{
  Node *temp = new Node;
  temp->data = data;
  temp->left = temp->right = NULL;
  return temp;
}

int getMaxWidth(Node *root)
{
  if (root == NULL)
    return 0;
  queue<Node *> q;
  q.push(root);
  int result = 0;
  while (!q.empty())
  {
    int count = q.size();
    result = max(count, result);
    while (count--)
    {
      Node *temp = q.front();
      q.pop();
      if (temp->left != NULL)
        q.push(temp->left);
      if (temp->right != NULL)
        q.push(temp->right);
    }
  }
  return result;
}
// Driver code
int main()
{
  Node *root = newNode(1);
  root->left = newNode(2);
  root->right = newNode(3);
  root->left->left = newNode(4);
  root->left->right = newNode(5);
  root->right->right = newNode(8);
  root->right->right->left = newNode(6);
  root->right->right->right = newNode(7);
  cout << getMaxWidth(root);
  return 0;
}