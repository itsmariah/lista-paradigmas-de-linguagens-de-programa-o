// Em Java e Golang, crie métodos que permitam essa funcionalidade.

class Produto {
    private String nome;
    private double preco;

    public Produto(String nome, double preco) {
        this.nome = nome;
        this.preco = preco;
    }

    public Produto somar(Produto outro) {
        
        return new Produto(this.nome + " & " + outro.nome, this.preco + outro.preco);
    }

    @Override
    public String toString() {
        return "Produto: " + nome + ", Preço: R$" + String.format("%.2f", preco);
    }

    public static void main(String[] args) {
        Produto produto1 = new Produto("Produto A", 50.00);
        Produto produto2 = new Produto("Produto B", 30.00);
        
        Produto produtoTotal = produto1.somar(produto2);

        System.out.println(produtoTotal);
    }
}
