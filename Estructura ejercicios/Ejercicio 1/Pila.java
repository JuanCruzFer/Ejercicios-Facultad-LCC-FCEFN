
public interface Pila<T> {
    void push(T elemento); //Agregar elemento a la pila
    T pop();
    T peek();
    boolean isEmpty();
    int size();
    void Recorrer();
}