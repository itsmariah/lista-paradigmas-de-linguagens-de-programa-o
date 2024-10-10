package main

import (
	"fmt"
)

type Carro struct {
	marca  string
	modelo string
	ano    int
}

func (c Carro) ExibirDetalhes() {
	fmt.Printf("Carro: %s %s, Ano: %d\n", c.marca, c.modelo, c.ano)
}

func main() {
	carro1 := Carro{"Peugeot", "208", 2021}
	carro2 := Carro{"Caoa Chery", "Tiggo 7 Pro", 2020}
	carro3 := Carro{"Jeep", "Renegade", 2019}

	carro1.ExibirDetalhes()
	carro2.ExibirDetalhes()
	carro3.ExibirDetalhes()
}
