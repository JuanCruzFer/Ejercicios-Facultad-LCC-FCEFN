public class Main {
    public static void main(String[] args) {
        Pila<Integer> pila = new PilaSecuencial<>(5);
        pila.push(1);
        pila.push(2);
        pila.push(3);
        pila.push(4);
        pila.push(5);
        System.out.println("Tope: " + pila.peek());
        System.out.println("Desapilado: " + pila.pop());
        System.out.println("Vacia?: " + pila.isEmpty());

        pila.Recorrer();

        Pila<String> pila2 = new PilaEncadenada<>();
        pila2.push("A");
        pila2.push("B");
        pila2.push("C");
        pila2.push("D");
        pila2.push("E");
        System.out.println("Tope: " + pila2.peek());
        System.out.println("Desapilado: " + pila2.pop());
        System.out.println("Vacia?: " + pila2.isEmpty());

        pila2.Recorrer();
    }
}
