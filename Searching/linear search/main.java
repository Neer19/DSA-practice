public class main {
    public static void main(String[] args) {
        int[] nums = { 23, 11, 24, 56, 45, 78, 90, 567, 45, 1, 5, 0 };
        int target = 1;
        int ans1 = learnear_search(nums, target);
        int ans2 = learnear_search2(nums, target);
        boolean ans3 = learnear_search3(nums, target);
        System.out.println(ans1);
        System.out.println(ans2);
        System.out.println(ans3);
        System.out.println("\n");
    }

    static boolean learnear_search3(int arr[], int target) {
        if (arr.length == 0) {
            return false;
        }

        for (int element : arr) {
            if (element == target) {
                return true;
            }
        }
        return false;
    }

    static int learnear_search2(int arr[], int target) {
        if (arr.length == 0) {
            return -1;
        }

        for (int element : arr) {
            if (element == target) {
                return element;
            }
        }
        return Integer.MAX_VALUE;
    }

    static int learnear_search(int arr[], int target) {
        if (arr.length == 0) {
            return -1;
        }

        for (int index = 0; index < arr.length; index++) {
            int element = arr[index];
            if (element == target) {
                return index;
            }
        }
        return -1;
    }
}