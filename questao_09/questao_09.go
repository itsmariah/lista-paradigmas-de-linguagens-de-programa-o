package main

import "fmt"

type Imprimivel interface {
	Imprimir()
}

type Relatorio struct {
	conteudo string
}

func (r Relatorio) Imprimir() {
	fmt.Println("Imprimindo Relatório:", r.conteudo)
}

type Contrato struct {
	partes string
}

func (c Contrato) Imprimir() {
	fmt.Println("Imprimindo Contrato:", c.partes)
}

func main() {
	var imprimiveis []Imprimivel
	imprimiveis = append(imprimiveis, Relatorio{"Relatório Mensal"}, Contrato{"Contrato de Prestação de Serviços"})

	for _, i := range imprimiveis {
		i.Imprimir()
	}
}
