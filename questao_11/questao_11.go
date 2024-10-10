package main

import (
	"fmt"
)

type Funcionario interface {
	CalcularSalario() float64
}

type FuncionarioHorista struct {
	nome            string
	horasTrabalhadas int
	valorHora      float64
}

func (f FuncionarioHorista) CalcularSalario() float64 {
	return float64(f.horasTrabalhadas) * f.valorHora
}

type FuncionarioAssalariado struct {
	nome         string
	salarioMensal float64
}

func (f FuncionarioAssalariado) CalcularSalario() float64 {
	return f.salarioMensal
}

func main() {
	funcionario1 := FuncionarioHorista{"Junior", 160, 20}
	funcionario2 := FuncionarioAssalariado{"Vanessa", 3000}

	fmt.Printf("Salário de %s: R$ %.2f\n", funcionario1.nome, funcionario1.CalcularSalario())
	fmt.Printf("Salário de %s: R$ %.2f\n", funcionario2.nome, funcionario2.CalcularSalario())
}
