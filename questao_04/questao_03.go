package main

import (
	"fmt"
)

type Animal interface {
	Som()
}

type Cachorro struct{}

func (c Cachorro) Som() {
	fmt.Println("O cachorro faz: Au Au!")
}

type Gato struct{}

func (g Gato) Som() {
	fmt.Println("O gato faz: Meow!")
}

func main() {
	animais := []Animal{Cachorro{}, Gato{}}

	for _, animal := range animais {
		animal.Som()
	}
}
