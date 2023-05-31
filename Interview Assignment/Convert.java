// I was asked to debug the below code

public class Convert {
    public static void main(String[] args) {
        int num = 101;
        int binary_val = num;
        int decimal_val = 0;
        int base = 1;
        while (num > 0) {
            int rem = num % 10;
            decimal_val = decimal_val + rem * base;
            num = num / 10;   // Incorrect logic = (num / 2)
            base = base * 2;  // Incorrect logic = (base*2)
        }
        System.out.println("The decimal of " + binary_val + " is " + decimal_val);
    } 
} 