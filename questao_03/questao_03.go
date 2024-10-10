package main

import (
	"fmt"
)

type ContaBancaria struct {
	titular string
	saldo   float64
}


func (c *ContaBancaria) Depositar(valor float64) {
	if valor > 0 {
		c.saldo += valor
		fmt.Printf("Deposito de R$ %.2f realizado. Saldo atual: R$ %.2f\n", valor, c.saldo)
	} else {
		fmt.Println("Valor de depósito deve ser positivo.")
	}
}


func (c *ContaBancaria) Sacar(valor float64) {
	if valor > c.saldo {
		fmt.Println("Saldo insuficiente para realizar o saque.")
	} else {
		c.saldo -= valor
		fmt.Printf("Saque de R$ %.2f realizado. Saldo atual: R$ %.2f\n", valor, c.saldo)
	}
}


func (c ContaBancaria) GetSaldo() float64 {
	return c.saldo
}

func main() {
	conta := ContaBancaria{titular: "Arthur", saldo: 1000}

	conta.Depositar(200)
	conta.Sacar(150)
	conta.Sacar(1200)
	fmt.Printf("Saldo final: R$ %.2f\n", conta.GetSaldo())
}
