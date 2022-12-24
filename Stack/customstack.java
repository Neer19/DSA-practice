public class customstack {
    protected int[] data;
    private static final int DEFAULT_SIZE = 10;

    int ptr = -1;

    public customstack() {
        this(DEFAULT_SIZE);
    }

    public customstack(int size) {
        this.data = new int[size];
    }

    public boolean push(int item) {
        if (isFull()) {
            System.out.println("stack is  full");
            return false;
        }
        ptr++;
        data[ptr] = item;
        return true;
    }

    public int pop() throws stackexception {
        if (isempty()) {
            throw new stackexception("can not pop");
        }
        return data[ptr--];
    }

    public int peek() throws stackexception {
        if (isempty()) {
            throw new stackexception("can not peek");
        }
        return data[ptr--];
    }

    public boolean isFull() {
        return ptr == data.length - 1;
    }

    public boolean isempty() {
        return ptr == -1;
    }

}
