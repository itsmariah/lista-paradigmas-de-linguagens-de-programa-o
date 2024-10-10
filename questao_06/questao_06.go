package main

import (
	"fmt"
)

type Motor struct {
	tipo string
}

func (m Motor) GetTipo() string {
	return m.tipo
}

type Carro struct {
	marca string
	modelo string
	ano int
	motor Motor
}

func (c Carro) ExibirDetalhes() {
	fmt.Printf("Carro: %s %s, Ano: %d, Motor: %s\n", c.marca, c.modelo, c.ano, c.motor.GetTipo())
}

func main() {
	motor1 := Motor{tipo: "Gasolina"}
	
	carro1 := Carro{marca: "Peugeot", modelo: "208", ano: 2021, motor: motor1}
	
	carro1.ExibirDetalhes()
}
