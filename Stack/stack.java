import java.util.*;

public class stack{
    public static void main(String[] args) {
        Stack<Integer> stack=new Stack<>();
        stack.push(35);
        stack.push(45);
        stack.push(40);

        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());


    }
}