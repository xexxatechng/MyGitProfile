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
public class Pet {

   int age;
   float weight;
   float height;
   String color;
   
   public void eat() {
       System.out.println("I'm hungry, let me have a snack like nachos!.");
   }
   
   
   public void sleep() {
       System.out.println("Good night, see you tomorrow.");
   }
   
   public String say(String aWord) {
       String petResponse =  "Ok! OK!" + aWord;
       return petResponse;
   }
  
}
