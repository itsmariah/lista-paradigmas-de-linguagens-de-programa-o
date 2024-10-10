class Carro {
    private String marca;
    private String modelo;
    private int ano;

    
    public Carro(String marca, String modelo, int ano) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
    }

    
    public void exibirDetalhes() {
        System.out.printf("Carro: %s %s, Ano: %d%n", marca, modelo, ano);
    }

    public static void main(String[] args) {
        Carro carro1 = new Carro("Peugeot", "208", 2021);
        Carro carro2 = new Carro("Caoa Chery", "Tiggo 7 Pro", 2020);
        Carro carro3 = new Carro("Jeep", "Renegade", 2019);

        carro1.exibirDetalhes();
        carro2.exibirDetalhes();
        carro3.exibirDetalhes();
    }
}
