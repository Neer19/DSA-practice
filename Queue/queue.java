import java.util.*;

public class queue{
    public static void main(String[] args) {
        Queue<Integer> queue=new LinkedList<>();
        queue.add(35);
        queue.add(45);
        queue.add(40);

        System.out.println(queue.remove());
        System.out.println(queue.remove());
        System.out.println(queue.remove());


    }
}