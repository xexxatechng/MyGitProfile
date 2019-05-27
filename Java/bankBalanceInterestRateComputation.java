
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package bankbalancevaryinginterest;
import javax.swing.JOptionPane;
/**
 *
 * @author HP
 */
public class BankBalanceVaryingInterest {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int selection;
        String balanceString;
        double balance;
        int tempBalance;
        int year = 1;
        double interest;
        
        balanceString = JOptionPane.showInputDialog(null, "Enter initial bank balance");
        balance = Double.parseDouble(balanceString);
        selection = JOptionPane.showConfirmDialog(null, "Do you want to see next year's balance?");
        
        while(selection == JOptionPane.YES_OPTION){
            for(interest = 0.02; interest <= 0.05; interest += 0.01){
                balance = balance + (balance * interest);
                tempBalance = (int)(balance * 100);
                balance = tempBalance / 100.0;
                JOptionPane.showMessageDialog(null, "After " + "years at " + interest + 
                        "\ninterest rate, balance is $" + balance);
                
            };
            selection = JOptionPane.showConfirmDialog(null, "Do you want to see the balance at the end "
             + "\nof another year?");
            ++year;
        }
        System.exit(0);
    }
    
}
