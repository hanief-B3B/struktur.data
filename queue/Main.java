public class Main {
    public static void main(String[] args) {
        CircularQueue theQueue = new CircularQueue(5);
        System.out.println("front: " + theQueue.front + " rear: " + theQueue.rear);

        theQueue.insert(10);
        theQueue.insert(20);
        theQueue.insert(30);
        theQueue.insert(40);
        
        theQueue.remove();
        System.out.println("remove 1x, front: " + theQueue.front + " rear: " + theQueue.rear);
        
        theQueue.insert(50);
        theQueue.insert(60);
        System.out.println("add 2 elements, front: " + theQueue.front + " rear: " + theQueue.rear);
        
        theQueue.remove();
        System.out.println("remove 1x, front: " + theQueue.front + " rear: " + theQueue.rear);
        
        while (!theQueue.isEmpty()) {
            int n = theQueue.remove();
            System.out.print(n + " ");
        }
    }
}
