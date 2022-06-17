package main

import (
	"fmt"
	"time"
)

func main() {
	iterations := 100 * 1000 * 1000
	a := make(map[int]int, iterations)

	startTime := time.Now()

	for i := 0; i < iterations; i++ {
		a[i] = i
	}

	fmt.Printf("%d iterations took %d\n", iterations, time.Since(startTime).Microseconds())

}
