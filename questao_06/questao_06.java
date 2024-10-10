class Motor {
    private String tipo;

    public Motor(String tipo) {
        this.tipo = tipo;
    }

    public String getTipo() {
        return tipo;
    }
}

class Carro {
    private String marca;
    private String modelo;
    private int ano;
    private Motor motor;

    public Carro(String marca, String modelo, int ano, Motor motor) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
        this.motor = motor;
    }

    
    public void exibirDetalhes() {
        System.out.printf("Carro: %s %s, Ano: %d, Motor: %s%n", marca, modelo, ano, motor.getTipo());
    }

    public static void main(String[] args) {
        Motor motor1 = new Motor("Gasolina");
        
        Carro carro1 = new Carro("Peugeot", "208", 2021, motor1);
        
        carro1.exibirDetalhes();
    }
}
