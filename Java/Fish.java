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
public class Fish extends Pet {
    int currentDepth = 0;
    
    public int dive(int howDeep){ 
        currentDepth = currentDepth + howDeep;
        System.out.println("Diving for " + howDeep + " feet");
        System.out.println("I'm at " + currentDepth + " feet below sea level");
        
        return currentDepth;
    }

}
