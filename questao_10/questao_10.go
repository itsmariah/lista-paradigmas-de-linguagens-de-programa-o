package main

import "fmt"

func somarDois(a int, b int) int {
	return a + b
}


func somarTres(a int, b int, c int) int {
	return a + b + c
}

func main() {
	resultado1 := somarDois(10, 20)
	resultado2 := somarTres(10, 20, 30)

	fmt.Println("Resultado da soma de dois números:", resultado1)
	fmt.Println("Resultado da soma de três números:", resultado2)
}
