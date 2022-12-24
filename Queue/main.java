public class main {
    public static void main(String[] args) throws Exception {
        CircularQueue queue = new CircularQueue(5);
        queue.insert(30);
        queue.insert(61);
        queue.insert(57);
        queue.insert(9);
        queue.insert(5);

        queue.display();

        System.out.println(queue.remove());
        queue.insert(900);
        queue.display();

        System.out.println(queue.remove());
        queue.insert(99);
        queue.display();

        System.out.println(queue.remove());
        queue.insert(466);
        queue.display();

        System.out.println(queue.remove());
        queue.insert(785);
        queue.display();

    }
}