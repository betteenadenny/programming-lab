#include<stdio.h>
#include<stdlib.h>
#define s 100
int stack[s],top=-1;
void push();
void pop();
void display();
void peek();
int main()
{
int c;
while(1){
printf("\n Enter your choice:");
printf("\n 1.Push \n 2.Pop \n 3.Display \n 4.Peek \n 5.Exit");
do
{
	printf("\n Enter the choice:");
	scanf("%d",&c);
	switch(c){
		case 1:push();
			break;	
		case 2:pop();
			break;
		case 3:display();
			break;
		case 4:peek();
			break;
		case 5:exit(0);
		default:printf("\nWrong selection");
		}
}
while(c!=5);
}
}
void push(){ 
	int n;
	if(top==s)
		printf("overflow");
	else{
		printf("Enter element:");
		scanf("%d",&n);
		top++;
		stack[top]=n;
	}
}
void pop(){
	int t;
	if(top==-1)
		printf("Underflow");
	else{
		t=stack[top];
		printf("%d element deleted",t);
		top--;
	}}
void display(){
	if(top>=0)
		printf("Underflow,no elements to print");
	for(int i=top;i>=0;i--)
	{
	printf("\n%d",stack[i]);
	}
	}
void peek()
{
	if(top==1)
	{
		printf("\n stack is empty");
	}
	else
		printf("peek:%d",stack[top]);
}
		
