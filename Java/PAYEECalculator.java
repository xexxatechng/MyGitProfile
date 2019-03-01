/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package payeecalculator;
import java.util.Scanner;
/**
 *
 * @author HP
 */
public class PAYEECalculator 
{

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) 
    {
               // Variable declarations
        
        double earnedIncome, basicSalary, housing, utility, meal;
        double entertainment, transport;
        
        // Create Scanner object
        Scanner getValue = new Scanner(System.in);
        
        // Request for Gross Payment or Earned Salary
        System.out.println("Enter Gross Earnings: = ");
        earnedIncome = getValue.nextDouble();
        
        // Housing calculation
        housing = (0.3 * earnedIncome);
        System.out.println("Housing Allowance:= " + housing);
        
        // Utilty calculation
        utility = (0.05 * earnedIncome);
        System.out.println("Utility:= " + utility);
        
        // Meal calculation
        meal = (0.1 * earnedIncome);
        System.out.println("Meal Allowance:= " + meal);
        
        // Entertain calculation
        entertainment = (0.05 * earnedIncome);
        System.out.println("Entertainment Allowance:= " + entertainment);
        
        // Transport calculation
        transport = (0.1 * earnedIncome);
        System.out.println("Transport Allowance:= " + transport);
        
        // Basic Salry calculation
        basicSalary = (0.4 * earnedIncome);
        System.out.println("Basic Salary:= " + basicSalary);
        
        System.out.println();
        /*double Totalsum = basicSalary + transport + entertainment + meal + utility + housing;
        System.out.println("Gross Earnings/Earned Income: = " + Totalsum);
        
        System.out.println();*/
        
        /*Calculate Tax relief and exemptions*/
        double personalAllowance = (earnedIncome * 0.2) + 200000;
        System.out.println("Personal Allowance is: " + personalAllowance);
        
        /*Calculate for Pensions*/
        double pension = (0.08 *(basicSalary + housing + transport));
        System.out.println("Pension:= " + pension);
        
        System.out.println();
        
        /*Calculation of Taxable Income*/
        double taxableIncome = earnedIncome -(personalAllowance + pension); 
        System.out.println("Taxable Income: = " + taxableIncome);
        System.out.println();
        
        //PAYEE
        double balance, firstPAYEE, secPAYEE, thirdPAYEE, fourthPAYEE, fifthPAYEE, finalPAYEE;
        balance = taxableIncome;
        
        if (balance > 300000){
            //First Tax Calculation on 7% for First #300,000
                firstPAYEE = (0.07 * 300000);
                System.out.printf("First PAYEE %.2f ", firstPAYEE);
                System.out.println();
                balance = balance - 300000;
                System.out.println("Balance after first #300,000 deduction = " + balance);
                System.out.println();}
        else{
                System.out.println();
        }
        
          
        if (balance > 300000){
                //Second Tax Calculation on 11% for second %300,000
                secPAYEE = (0.11 * 300000);
                System.out.println("Second PAYEE = " + secPAYEE);
                balance = balance - 300000;
                System.out.println("Balance after second #300,000 deduction = " + balance);
                System.out.println();}
        else {
                System.out.println();
        }
        
        
        if (balance > 500000){
            //Third Tax Calculation on 15% for #500,000
              thirdPAYEE = (0.15 * 300000);
              System.out.printf("Third PAYEE %.2f ", thirdPAYEE);
              System.out.println();
              balance = balance - (500000);
              System.out.println("Balance after first #500,000 deduction = " + balance);
              System.out.println(); }
        else {
              System.out.println();
        }
        
        
        if (balance > 500000){
              //Fourth Tax Calculation on 19% for #500,000
              fourthPAYEE = (0.19 * 500000);
              System.out.printf("Fourth PAYEE %.2f ", fourthPAYEE);
              System.out.println();
              balance = balance - (500000);
              System.out.println("Balance after second #500,000 deduction = " + balance);
              System.out.println(); }
        
        else {
              System.out.println();
        }
        
        
        if (balance > 1291200){
                //Fifth Tax Calculation on 21% for #1,292,200
                fifthPAYEE = (0.21 * 1291200);
                System.out.printf("Fifth PAYEE %.2f ", fifthPAYEE);
                System.out.println();
                balance = balance - (1291200);
                System.out.println("Balance after #1,291,200 deduction = " + balance);
                System.out.println(); }
        
        else {
                System.out.println();
        }
        
        
        if (balance > 3200000){
        //Final Tax Calculation on 15% for #3,200,000
                finalPAYEE = (0.24 * 3200000);
                System.out.printf("Final PAYEE %.2f ", finalPAYEE);
                System.out.println();
                balance = balance - (3200000);
                System.out.println("Balance after #3,200,000 deduction = " + balance);
                System.out.println();
                System.out.println("Balance = " + balance); }
        
        
        else {
                System.out.println();
        }
        
        System.out.println("Annual TAX = " + balance);
    }
    
}
