package main

import (
	"fmt"
)

type Professor struct {
	nome    string
	escolas []*Escola
}

func (p *Professor) AdicionarEscola(escola *Escola) {
	p.escolas = append(p.escolas, escola)
	escola.AdicionarProfessor(p)
}

func (p Professor) ListarEscolas() {
	fmt.Printf("Professor %s leciona nas escolas: ", p.nome)
	for _, escola := range p.escolas {
		fmt.Print(escola.nome + " ")
	}
	fmt.Println()
}

type Escola struct {
	nome       string
	professores []*Professor
}

func (e *Escola) AdicionarProfessor(professor *Professor) {
	e.professores = append(e.professores, professor)
}

func (e Escola) ListarProfessores() {
	fmt.Printf("Escola %s tem os professores: ", e.nome)
	for _, professor := range e.professores {
		fmt.Print(professor.nome + " ")
	}
	fmt.Println()
}

func main() {
	escola1 := &Escola{nome: "Escola A"}
	escola2 := &Escola{nome: "Escola B"}

	professor1 := &Professor{nome: "Viviano"}
	professor2 := &Professor{nome: "Thiago"}

	professor1.AdicionarEscola(escola1)
	professor1.AdicionarEscola(escola2)
	professor2.AdicionarEscola(escola1)

	professor1.ListarEscolas()
	professor2.ListarEscolas()

	escola1.ListarProfessores()
	escola2.ListarProfessores()
}
