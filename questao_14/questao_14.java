public class questao_14 {
    private static questao_14 instancia;

    private questao_14() {
    }

    public static questao_14 getInstancia() {
        if (instancia == null) {
            instancia = new questao_14();
        }
        return instancia;
    }

    public void setConfig(String chave, String valor) {
    }

    public String getConfig(String chave) {
        return null;
    }

    public static void main(String[] args) {
        questao_14 config1 = questao_14.getInstancia();
        config1.setConfig("tema", "escuro");

        questao_14 config2 = questao_14.getInstancia();
        System.out.println(config2.getConfig("tema"));

        System.out.println(config1 == config2);
    }
}
