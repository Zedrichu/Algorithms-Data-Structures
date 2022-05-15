package Week5.Stack;
import java.util.Scanner;

public class StackLinkedList {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        s.nextLine();
        Stack stack = new Stack();
        for (int i=0;i<n;i++) {
            String str = s.nextLine();
            String[] a = str.split(" ");
            if (a[0].equals("PU")) {
                stack.push(Integer.parseInt(a[1]));
            } else if (a[0].equals("PO")) 
                System.out.println(stack.pop()+" ");
        }
        s.close();        
    }
}

class Node {
    int key;
    Node next;

    Node() {
        this.next = null;
    }

    Node(int x) {
        this.key = x;
        this.next = null;
    }
}

class Stack {
    Node head;

    Stack() {
        this.head = null;
    }

    public boolean isEmpty() {
        return this.head == null;
    }

    public void push(int x) {
        Node q = new Node(x);
        //q.key = x;
        q.next = this.head;
        this.head = q;
    }

    public int pop() {
        if (this.isEmpty()) { throw new Error("Stack is empty");}
        int val = this.head.key;
        this.head = this.head.next;
        return val;
    }
}