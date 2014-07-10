//public static class staticTest{
public class staticTest{
    public static void main(String[] args) {
        System.out.println("static class");

        //        staticTest.innerStaticClass ic = new statiTest.innerStaticClass().prt("Hello World");
        staticTest.innerStaticClass ic = new staticTest.innerStaticClass();
        ic.prt("Hello World");
        new staticTest.innerStaticClass().prt("Hello World again");
    }

    public static class innerStaticClass {
        public void prt(String s) {
            System.out.println(s);
        }
    }
}
