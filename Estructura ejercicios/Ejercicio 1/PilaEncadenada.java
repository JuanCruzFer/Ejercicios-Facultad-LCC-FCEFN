public class PilaEncadenada<T> implements Pila<T> {
    private class Nodo {
        T dato;
        Nodo siguiente;
        Nodo(T dato) {
            this.dato = dato;
            this.siguiente = null;
        }
    }

    private Nodo tope;
    private int capacidad;


    public PilaEncadenada() {
        this.tope = null;
        this.capacidad = 0;
    }

    @Override
    public void push(T elemento) {
        Nodo nuevo = new Nodo(elemento);
        nuevo.siguiente = tope;
        tope = nuevo;
        capacidad++;
    }

    @Override
    public T pop() {
        if (isEmpty()){
            throw new IllegalStateException("La pila está vacía");
        }

        T dato = tope.dato;
        tope = tope.siguiente;
        capacidad--;
        return dato;
    }

    @Override
    public T peek() {
        if (isEmpty()){
            throw new IllegalStateException("La pila está vacía");
        }
        return tope.dato;
    }

    @Override
    public boolean isEmpty() {
        return tope == null;
    }

    @Override
    public int size() {
        return capacidad;
    }

    public void Recorrer(){
        Nodo aux = tope;
        System.out.println("Pila: ");
        while (aux != null){
            System.out.println(aux.dato + "");
            aux = aux.siguiente;
        }
        System.out.println();
    }
}
