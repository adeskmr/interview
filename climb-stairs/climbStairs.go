package main

import "fmt"

func climbStairs(n int) int{
	if n == 0 {return 0}
	if n == 1 {return 1}
	case1 := 1
	case2 := 2

	for i := 2; i <n; i++ {
		case1, case2 = case2, case1+case2
	}
	return case2
}

func main()  {
	fmt.Println(climbStairs(9))
}