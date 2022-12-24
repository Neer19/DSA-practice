public class searchinrange {
    public static void name(String[] args) {
        int[] arr = { 18, 30, 45, 12, 13, 19, 1, 7 };
        int target = 13;
        System.out.println(learnear_search(arr, target, 1, 5));
    }

    static int learnear_search(int arr[], int target, int start, int end) {
        if (arr.length == 0) {
            return -1;
        }

        for (int index = start; index <= end; index++) {
            int element = arr[index];
            if (element == target) {
                return index;
            }
        }
        return -1;
    }
}