package main

import (
	"fmt"
)

type Empregado struct {
	nome   string
	cargo  string
	salario float64
}

type Empresa struct {
	nome      string
	empregados []*Empregado
}

func (e *Empresa) AdicionarEmpregado(empregado *Empregado) {
	e.empregados = append(e.empregados, empregado)
}

func (e Empresa) ListarEmpregados() {
	fmt.Printf("Empregados da empresa %s:\n", e.nome)
	for _, empregado := range e.empregados {
		fmt.Printf("Nome: %s, Cargo: %s, Salário: %.2f\n", empregado.nome, empregado.cargo, empregado.salario)
	}
}

func main() {
	empresa := Empresa{nome: "Tech Solutions"}

	emp1 := &Empregado{nome: "Isadora", cargo: "Desenvolvedora", salario: 5000.00}
	emp2 := &Empregado{nome: "Diogo", cargo: "Gerente", salario: 8000.00}
	emp3 := &Empregado{nome: "Carolina", cargo: "Analista", salario: 6000.00}

	empresa.AdicionarEmpregado(emp1)
	empresa.AdicionarEmpregado(emp2)
	empresa.AdicionarEmpregado(emp3)

	empresa.ListarEmpregados()
}
