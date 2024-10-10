package main

import (
	"errors"
	"fmt"
)

var SaldoInsuficiente = errors.New("saldo insuficiente para realizar o saque")

type ContaBancaria struct {
	titular string
	saldo   float64
}

func (c *ContaBancaria) Depositar(valor float64) {
	c.saldo += valor
	fmt.Printf("Deposito de R$ %.2f realizado. Saldo atual: R$ %.2f\n", valor, c.saldo)
}

func (c *ContaBancaria) Sacar(valor float64) error {
	if valor > c.saldo {
		return SaldoInsuficiente
	}
	c.saldo -= valor
	fmt.Printf("Saque de R$ %.2f realizado. Saldo atual: R$ %.2f\n", valor, c.saldo)
	return nil
}

func main() {
	conta := ContaBancaria{titular: "Natan", saldo: 180}

	err := conta.Sacar(250)
	if err != nil {
		fmt.Println(err)
	}
}
