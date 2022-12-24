public class minimum {
    public static void main(String[] args) {
        int[] arr = { 12, 0, 3, 5, 55, 6, 7, 89, 77, 45 };
        System.out.println(min(arr));
    }

    static int min(int[] arr) {
        int ans = arr[0];

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < ans) {
                ans = arr[i];
            }
        }
        return ans;
    }
}
