// Interfaces/Protocolos: Em Java e Golang, defina uma interface para imprimível que tenha um método imprimir. Implemente essa interface em classes como Relatório e  Contrato. Em Python, use a abordagem de protocolo ou classes abstratas.

interface Imprimivel {
    void imprimir();
}


class Relatorio implements Imprimivel {
    private String conteudo;

    public Relatorio(String conteudo) {
        this.conteudo = conteudo;
    }

    @Override
    public void imprimir() {
        System.out.println("Relatório: " + conteudo);
    }
}

class Contrato implements Imprimivel {
    private String partes;

    public Contrato(String partes) {
        this.partes = partes;
    }

    @Override
    public void imprimir() {
        System.out.println("Contrato: " + partes);
    }
}

public class questao_09 {
    public static void main(String[] args) {
        Imprimivel relatorio = new Relatorio("Relatório Mensal");
        Imprimivel contrato = new Contrato("Contrato de Prestação de Serviços");

        relatorio.imprimir();
        contrato.imprimir();
    }
}
