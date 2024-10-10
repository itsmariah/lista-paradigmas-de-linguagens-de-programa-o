class Carro {
    private String marca;
    private String modelo;
    @SuppressWarnings("unused")
    private int ano;
    private int velocidade;

    public Carro(String marca, String modelo, int ano) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
        this.velocidade = 0;
    }

    public void acelerar(int valor) {
        velocidade += valor;
        System.out.printf("%s %s acelerou para %d km/h.%n", marca, modelo, velocidade);
    }

    public void frear(int valor) {
        velocidade -= valor;
        if (velocidade < 0) {
            velocidade = 0;
        }
        System.out.printf("%s %s freou para %d km/h.%n", marca, modelo, velocidade);
    }

    public void exibirVelocidade() {
        System.out.printf("Velocidade atual de %s %s: %d km/h%n", marca, modelo, velocidade);
    }

    public static void main(String[] args) {
        Carro carro1 = new Carro("Peugeot", "208", 2021);
        
        carro1.acelerar(50);
        carro1.exibirVelocidade();
        carro1.frear(20);
        carro1.exibirVelocidade();
        carro1.frear(40);
        carro1.exibirVelocidade();
    }
}
