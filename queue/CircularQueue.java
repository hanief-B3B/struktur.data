public class CircularQueue {
    private int[] queueArray;
    private int maxSize;   
    public int front;     
    public int rear;      
    private int numItems; 

    public CircularQueue(int size) {
        maxSize = size + 1;
        queueArray = new int[maxSize];
        front = 0;
        rear = 0;
        numItems = 0;
    }

    public void insert(int item) {
        if (isFull()) {
            System.out.println("Queue is full! Cannot insert " + item);
            return;
        }
        queueArray[rear] = item;
        rear = (rear + 1) % maxSize;
        numItems++;
    }

    public int remove() {
        if (isEmpty()) {
            System.out.println("Queue is empty! Cannot remove an element.");
            return -1;
        }
        int temp = queueArray[front];
        front = (front + 1) % maxSize;
        numItems--;
        return temp;
    }

    public boolean isEmpty() {
        return numItems == 0;
    }

    public boolean isFull() {
        return numItems == maxSize - 1;
    }

    public int peek() {
        if (isEmpty()) {
            System.out.println("Queue is empty! No front element.");
            return -1;
        }
        return queueArray[front];
    }
}
