package 继承;

public class Test {
    public static void main(String[] args) {
        //创建对象并调用方法

        //1.创建布偶猫的对象


        RagDoll rd  = new RagDoll();
        rd.eat();
        rd.catchMouse();
        rd.drink();

        System.out.println("----------------------");
        //2.创建哈士奇的对象

        Husky Hu = new Husky();
        Hu.eat();
        Hu.breakHome();
        Hu.drink();
        Hu.lookHome();

    }
}
