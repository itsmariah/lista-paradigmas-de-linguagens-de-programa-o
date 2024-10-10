// Em Java e Golang, crie métodos que permitam essa funcionalidade.

package main

import (
	"fmt"
)

type Produto struct {
	nome  string
	preco float64
}

func (p Produto) Somar(outro Produto) Produto {
	return Produto{
		nome:  p.nome + " & " + outro.nome,
		preco: p.preco + outro.preco,
	}
}

func (p Produto) String() string {
	return fmt.Sprintf("Produto: %s, Preço: R$%.2f", p.nome, p.preco)
}

func main() {
	produto1 := Produto{"Produto A", 50.00}
	produto2 := Produto{"Produto B", 30.00}
	
	produtoTotal := produto1.Somar(produto2)

	fmt.Println(produtoTotal) 
}