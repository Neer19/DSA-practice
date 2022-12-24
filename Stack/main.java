public class main {
    public static void main(String[] args) throws stackexception {
        customstack stack = new dynamic(10);

        stack.push(34);
        stack.push(10);
        stack.push(20);
        stack.push(90);
        stack.push(518);
        stack.push(809);

        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
    }
}