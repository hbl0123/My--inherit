package 继承;

//继承的练习（自己设计一个继承体系）
/*
    现在有四种动物：布偶猫，中国狸花猫，哈士奇，泰迪
    暂不考虑属性，只考虑行为
    请按照继承体的思想特点，进行继承体的设计。

    四种动物风别有以下行为：
    布偶猫：吃饭，喝水，抓老鼠
    中国狸花猫：吃饭，喝水，吃老鼠
    哈士奇：吃饭，喝水，看家，拆家
    泰迪：吃饭，喝水，看家，蹭一蹭
 */
public class Animal {
    public void eat(){
        System.out.println("吃东西");
    }
    public void drink(){
        System.out.println("喝水");
    }

}
