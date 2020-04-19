#include<stdio.h>

struct node
{
  int roll;
	node *next;
};

node *root=NULL;

    void append(int roll)
    {
        if(root==NULL)
        {
            root=new node();
            root->roll=roll;
            root->next=NULL;
        }
    }

int main(){



    return 0;
}
