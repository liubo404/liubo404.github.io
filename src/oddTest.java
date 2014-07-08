/**
 *Boook:<< Java puzzlers,traps,pitfalls>>
 */
public class oddTest {
    public static void main(String[] args) {
        System.out.println(oddTest.isOdd(3));
        System.out.println(oddTest.isOdd(-3));
    }
    public static boolean isOdd(int i) {
        return i % 2 != 1;
    }
}
