import java.util.Scanner;
public class Conversor {
    public static String convertir(int n, int base){
        if (n == 0){
            return "0";
        }
        StringBuilder resultado = new StringBuilder();
        int cociente = n;
        while (cociente > 0){
            int resto = cociente % base;
            if (resto < 10){
                resultado.append(resto);
            } else {
                resultado.append((char)('A' +(resto - 10)));
            }
            cociente /= base;
        }
        return resultado.reverse().toString();
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un numero a convertir : "); int n = sc.nextInt();
        int op = -1;
        
        while (op != 0){
            System.out.println("===== MENÚ DE CONVERSIÓN =====");
            System.out.println("2. Convertir a Binario");
            System.out.println("8. Convertir a Octal");
            System.out.println("16. Convertir a Hexadecimal");
            System.out.println("0. Salir");
            System.out.println("Elige una opción: ");
            op = sc.nextInt();
            System.out.println();
            if (op == 2){
                System.out.println(n + ":En binario = " + convertir(n, 2));
                System.out.println();
            }else if(op == 8){
                System.out.println(n + ":En octal = " + convertir(n, 8));
                System.out.println();
            }else if(op == 16){
                System.out.println(n + ":En hexadecimal = " + convertir(n, 16));
                System.out.println();
            }
        }
        sc.close();
    }
    
}