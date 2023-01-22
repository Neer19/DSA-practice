

public class lst {

    private Node head;
    private Node tail;
    private int size;

    public lst() {
        this.size = 0;
    }

    // insert first
    public void insFirst(int val) {
        Node node = new Node(val);
        node.next = head;
        head = node;

        if (tail == null) {
            tail = head;
        }

        size += 1;
    }

    // insert last
    public void insLast(int val){
        if(tail==null){
            insFirst(val);
            return;
        }

        Node node=new Node(val);
        tail.next=node;
        tail=node;
        size++;

    }

    // insert at nth value
    public void insert(int val,int index){
        if (index==0){
            insFirst(val);
            return;
        }
        if (index==size){
            insLast(val);
            return;
        }
        Node temp=head;
        for(int i=1;i<index;i++){
            temp=temp.next;
        }
        Node node=new Node(val,temp.next);
        temp.next=node;
        size++;
    }

    // delete first
    public int dltFirst(){
        int val=head.value;
        head=head.next;
        if(head==null){
            tail=null;
        }
        size--;
        return val;
    }

    // delete last
    public int dltLast(){
        if(size<=1){
            return dltFirst();
        }
        Node secondlast=get(size-2);
        int val=tail.value;
        tail=secondlast;
        tail.next=null;
        return val;
    }

    // delete nth index
    public int delete(int index){
        if(index==0){
            return dltFirst();
        }
        if(index==size-1){
            return dltLast();
        }
        Node prev=get(index-1);
        int val=prev.next.value;
        prev.next=prev.next.next;

        return val;
    }

    // find 
    public Node find(int value){
        Node node=head;
        while(node!=null){
            if(node.value==value){
                return node;
            }
            node=node.next;
        }
        return node;
    }

    public Node get(int index){
        Node node=head;
        for (int i = 0; i < index; i++) {
            node=node.next;
        }
        return node;
    }

    public void display() {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.value + "->");
            temp = temp.next;
        }
        System.out.println("End");
    }

    private class Node {
        private int value;
        private Node next;

        public Node(int value) {
            this.value = value;
        }

        public Node(int value, Node next) {
            this.value = value;
            this.next = next;
        }

    }

}
