package main

import (
	"fmt"
	"sync"
)

type Configuracao struct {
	configuracoes map[string]string
}

var instancia *Configuracao
var mu sync.Mutex

func GetInstancia() *Configuracao {
	mu.Lock()
	defer mu.Unlock()

	if instancia == nil {
		instancia = &Configuracao{
			configuracoes: make(map[string]string),
		}
	}
	return instancia
}

func (c *Configuracao) SetConfig(chave, valor string) {
	c.configuracoes[chave] = valor
}

func (c *Configuracao) GetConfig(chave string) string {
	return c.configuracoes[chave]
}

func main() {
	config1 := GetInstancia()
	config1.SetConfig("tema", "escuro")

	config2 := GetInstancia()
	fmt.Println(config2.GetConfig("tema"))

	fmt.Println(config1 == config2)
}
