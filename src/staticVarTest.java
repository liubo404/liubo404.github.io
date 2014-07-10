public class staticVarTest {
    public static void prt(String s) {
        System.out.println(s);
    }

    public static void main(String[] args) {
        staticVar v1,v2;
        v1 = new staticVar();
        v2 = new staticVar();
        prt("v1.c=" +v1.c+"v2.c="+v2.c);
        v1.inc();
        prt("v1.c=" +v1.c+"v2.c="+v2.c);
    }
}
