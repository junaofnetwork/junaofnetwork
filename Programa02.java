//Nome: João Eduardo Brandenburg de Almei
import javax.swing.*;
public class Programa02 {
    public static void main(String[] args) {
        
    int n1, n2;
    int mod, div;
    double raiz, pot;
    String msg = "";


    //entrada de dados
    n1 = Integer.parseInt(JOptionPane.showInputDialog("Digite Um numero Inteiro Por favor:"));
    n2 = Integer.parseInt(JOptionPane.showInputDialog("Digite Outro numero Inteiro Por favor:"));
    //processamento
    mod = n1 % n2;
    div = n1 / n2;
    raiz = Math.sqrt(n1);
    pot = Math.pow(n1, n2);
    //saida de dados
    msg = "n1 = " + n1 + " n2 = " + n2 + "\n";
    msg = msg + "resto da divisão de n1 por n2 = " + mod + "\n";
    msg = msg + "quociente da divisão de n1 por n2 = " + div + "\n";
    msg = msg + "raiz quadrada de n1 = " + raiz + "\n";
    msg = msg + "potencia de n1 e n2 = " + pot + "\n";
    System.out.println(msg);
    System.exit(0);

    }
}
