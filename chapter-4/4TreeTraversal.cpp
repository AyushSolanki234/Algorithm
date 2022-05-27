#include <iostream>
using namespace std;

struct Node {
	int data;
	struct Node *left, *right;
};

Node* newNode(int data){
	Node* temp = new Node;
	temp->data = data;
	temp->left = temp->right = NULL;
	return temp;
}

void Postorder(struct Node* node){
	if (node == NULL)
		return;
	Postorder(node->left);
	Postorder(node->right);
	cout << node->data << " ";
}

void Inorder(struct Node* node){
	if (node == NULL)
		return;

	Inorder(node->left);
	cout << node->data << " ";
	Inorder(node->right);
}

void Preorder(struct Node* node){
	if (node == NULL)
		return;
	cout << node->data << " ";
	Preorder(node->left);
	Preorder(node->right);
}

int main(){
	struct Node* root = newNode(1);
	root->left = newNode(2);
	root->right = newNode(3);
	root->left->left = newNode(4);
	root->left->right = newNode(5);

	cout << "Preorder traversal: ";
	Preorder(root);
	cout<<endl;

	cout << "Inorder traversal: ";
	Inorder(root);
	cout<<endl;

	cout << "Postorder traversal: ";
    Postorder(root);
	cout<<endl;
	return 0;
}

