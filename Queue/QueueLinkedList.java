package Week5.Queue;
import java.util.Scanner;

public class QueueLinkedList {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        s.nextLine();
        Queue queue = new Queue();
        for (int i=0;i<n;i++) {
            String str = s.nextLine();
            String[] a = str.split(" ");
            if (a[0].equals("E")) {
                queue.enqueue(Integer.parseInt(a[1]));
            } else if (a[0].equals("D")) 
                System.out.println(queue.dequeue()+" ");
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
}

class Queue {
    Node head;
    Node tail;

    Queue() {
        this.head = null;
    }

    public void enqueue(int x) {
        Node q = new Node();
        q.key = x;
        q.next = this.head;
        if (this.head==null) this.tail = q;
        this.head = q;
    }

    public int dequeue() {
        if (this.head == this.tail) {
            int val = this.head.key;
            this.tail = null;
            this.head = null;
            return val;
        } else {
            Node q= this.head;
            while(q.next != this.tail) {q = q.next;}
            int val = this.tail.key;
            q.next = null;
            this.tail = q;
            return val;
        }
    }
}
