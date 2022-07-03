#include <bits/stdc++.h>

using namespace std;

class Node {
public:
	int data;
	Node* Link;

	Node(int data){
		this->data = data;
		Link = NULL;
	}
};

Node* head = NULL;
class LinkList {
public:
	void insert(int item){
		Node* newNode = new Node(item);
		if (head == NULL)
			head = newNode;
		else {
			newNode->Link = head;
			head = newNode;
		}
	}

	bool detect(){
		Node *slowPointer = head,
			*fastPointer = head;

		while (slowPointer != NULL && fastPointer != NULL && fastPointer->Link != NULL) {
			slowPointer = slowPointer->Link;
			fastPointer = fastPointer->Link->Link;
			if (slowPointer == fastPointer)
				return 1;
		}
		return 0;
	}
};

int main(){
	LinkList l1;
	l1.insert(10);
	l1.insert(20);
	l1.insert(30);
	l1.insert(40);
	l1.insert(50);

	Node* temp = head;
	while (temp->Link != NULL)
		temp = temp->Link;

	temp->Link = head;

	if (l1.detect())
		cout << "Loop exists in the Linked List" << endl;
	else
		cout << "Loop does not exists in the Linked List" << endl;

	return 0;
}




// This code is written by Ayush :-) 