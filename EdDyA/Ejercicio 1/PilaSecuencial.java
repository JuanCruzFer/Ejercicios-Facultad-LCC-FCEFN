public class PilaSecuencial<T> implements Pila<T> {
    private T[] datos;
    private int tope;
    private int capacidad;

    @SuppressWarnings("unchecked")
    public PilaSecuencial(int capacidad) {
        this.capacidad = capacidad;
        this.datos = (T[]) new Object[capacidad];
        this.tope = -1;
    }
    
    @Override
    public void push(T elemento) {
        if (tope + 1== capacidad){
            throw new IllegalStateException("La pila está llena");
        }
        datos[++tope] = elemento;
    }

    @Override
    public T pop() {
        if (isEmpty()){
            throw new IllegalStateException("La pila está vacía");
        }
        return datos[tope--];
    }

    @Override
    public T peek() {
        if (isEmpty()){
            throw new IllegalStateException("La pila está vacía");
        }
        return datos[tope];
    }

    @Override
    public boolean isEmpty() {
        return tope == -1;
    }

    @Override
    public int size() {
        return tope + 1;
    }

    public void Recorrer(){
        for (T pilita :  datos){
            System.out.println(pilita);
        }
    }
}