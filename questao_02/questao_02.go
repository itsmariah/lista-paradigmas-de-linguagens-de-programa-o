package main

import (
	"fmt"
)

type Carro struct {
	marca    string
	modelo   string
	ano      int
	velocidade int
}

func (c *Carro) Acelerar(valor int) {
	c.velocidade += valor
	fmt.Printf("%s %s acelerou para %d km/h.\n", c.marca, c.modelo, c.velocidade)
}

func (c *Carro) Frear(valor int) {
	c.velocidade -= valor
	if c.velocidade < 0 {
		c.velocidade = 0
	}
	fmt.Printf("%s %s freou para %d km/h.\n", c.marca, c.modelo, c.velocidade)
}

func (c Carro) ExibirVelocidade() {
	fmt.Printf("Velocidade atual de %s %s: %d km/h\n", c.marca, c.modelo, c.velocidade)
}

func main() {
	carro1 := Carro{"Peugeot", "208", 2021}
	
	carro1.Acelerar(50)
	carro1.ExibirVelocidade()
	carro1.Frear(20)
	carro1.ExibirVelocidade()
	carro1.Frear(40)
	carro1.ExibirVelocidade()
}
