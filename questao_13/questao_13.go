package main

import (
	"fmt"
)

func Fatorial(n int) int {
	if n < 0 {
		panic("Fatorial não é definido para números negativos.")
	}
	if n == 0 || n == 1 {
		return 1
	}
	return n * Fatorial(n-1)
}

func main() {
	numero := 5
	resultado := Fatorial(numero)
	fmt.Printf("O fatorial de %d é %d.\n", numero, resultado)
}
