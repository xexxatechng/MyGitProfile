/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pet;

/**
 *
 * @author HP
 */
public class PetMaster {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Pet myPet = new Pet();
        
        
        myPet.sleep();
        myPet.eat();
        
        System.out.println();
        //declare a variable to call a method with return type.
        String petReaction;
        petReaction = myPet.say(" Tweet!! Tweet!!");
        System.out.println(petReaction);
        
        //Proving Inheritance by calling the Fish class which will be features
        //of the Pet class.
        System.out.println();
        System.out.println("//Inheritance call.");
        Fish myLittleFish = new Fish();
    
        myLittleFish.eat();
        myLittleFish.sleep();
        
        System.out.println();
        //declare variable to call a return type.
        myLittleFish.dive(50);
        
    }
    
}
