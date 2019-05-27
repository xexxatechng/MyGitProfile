/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pricearraycalculation;
import java.lang.*;
/**
 *
 * @author HP
 */
public class PriceArrayCalculation {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // Declare an array
        System.out.println("index" + "\t" + "Value");
        int priceArray[] = {2, 14, 35, 67, 85};
        int subscripts;
        for(subscripts = 0; subscripts < priceArray.length; ++subscripts){
            priceArray[subscripts] += 3;
            //priceArray.append(subscripts);
            System.out.println(subscripts + "\t" + priceArray[subscripts]);
        }
        
        System.out.println("----------------------------------------------");
        int sum = 0;
        for(int counter = 0; counter < 5; ++counter){
            sum += priceArray[counter]; 
        }
        System.out.println("Sum of array is " + sum);
    }
    
}
