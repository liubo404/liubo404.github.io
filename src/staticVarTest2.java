public class staticVarTest2{
    public static void prt(String s){
        System.out.println(s);
    }
    staticVar2 v = new staticVar2(10);
    static staticVar2 v1,v2;
    static{
        prt("v1.c="+v1.c+"v2.c="+v2.c);
        v1 = new staticVar2(27);
        prt("v1.c="+v1.c+"v2.c="+v2.c);
        v2 = new staticVar2(15);
        prt("v1.c="+v1.c+"v2.c="+v2.c);

    }

    public static void main(String[] args) {
        staticVarTest2 sv = new staticVarTest2();
        prt("sv.c="+sv.v.c);
        prt("v1.c="+v1.c+"v2.c="+v2.c);
        v1.inc();
        prt("v1.c="+v1.c+"v2.c="+v2.c);
        prt("sv.c="+sv.v.c);
    }
}
