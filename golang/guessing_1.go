package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"os/exec"
	"runtime"
	"strconv"
	"strings"
)

func open(url string) {
	switch runtime.GOOS {
	case "windows":
		exec.Command("rundll32", "url.dll,FileProtocolHandler", url).Start()
	case "linux": // Works perfectly on Arch with xdg-utils installed
		exec.Command("xdg-open", url).Start()
	}
}

func normal() {
	random_num := rand.Intn(100) + 1
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Println("A number between 0 and 100 has been stored.")
	tries := 0
	for {
		fmt.Printf("\nEnter your guess\n] ")

		if scanner.Err() != nil {
			fmt.Print(scanner.Err())
			break
		}
		if !scanner.Scan() {
			break
		}
		strInput := strings.TrimSpace(scanner.Text())
		intInput, err := strconv.Atoi(strInput)
		if err != nil && strInput != "cheatmode" {
			fmt.Print("Invalid Input. Try again.")
			continue
		}
		if strInput == "cheatmode" {
			fmt.Println("YOU WIN!!\nYour guess:", random_num, "\nTries: 0")
			break
		} else if intInput == random_num {
			fmt.Println("YOU WIN!!!", "\n", "Tries:", tries)
			open("https://youtu.be/c7TNPiryDyg?si=TXVUx6MgcSBFpnEP&t=32")
			break
		} else if intInput > random_num {
			fmt.Println(intInput, "is greater! Try a smaller one!")
			tries++
			fmt.Println("Tries:", tries)
			cmd := exec.Command("python3", "python/xd.py")
			_ = cmd.Run()
		} else if intInput < random_num {
			fmt.Println(intInput, "is smaller! Try a greater one!")
			tries++
			fmt.Println("Tries:", tries)
			cmd := exec.Command("python3", "python/xd.py")
			_ = cmd.Run()
		}
	}
}

/*
func special() {
	rand_num := rand.Intn(100)
	fmt.Println("The game is only for 2, 3, 4, and 5 players for now.")
	time.Sleep(2)
	var players int
	fmt.Printf("Select number of players:\n2, 3, 4, or 5\n] ")
	fmt.Scan(&players)
	if players > 5 || players < 0 {
		fmt.Println("2, 3, 4, or 5 only. Error.")
		errors.New("Selected number out of supported range.")
	}
	fmt.Print("Initialising players...")
	var player1 int
	var player2 int
	var player3 int
	var player4 int
	var player5 int
	time.Sleep(2)
	fmt.Print("Guess the number. (Psst! It's between 0 and 100!)")
	fmt.Printf("\nPlayer 1! Enter a number!\n] ")
	fmt.Scan(&player1)
	time.Sleep(1)
	fmt.Printf("Player 2! Enter a number!\n] ")
	fmt.Scan(&player2)
	time.Sleep(1)
	if players == 3 {
		fmt.Printf("Player 3! Enter a number!\n] ")
		fmt.Scan(&player3)
	}
	if players == 4 {
		fmt.Printf("Player 4! Enter a number!\n] ")
		fmt.Scan(&player4)
	}
	if players == 5 {
		fmt.Printf("Player 5! Enter a number!\n] ")
		fmt.Scan(&player5)
	}
	fmt.Println("Differences:")
	diff_1 := rand_num - player1
	fmt.Println("1:", diff_1)
	diff_2 := rand_num - player2
	fmt.Println("2:", diff_2)
	if players == 3 {
		diff_3 := rand_num - player3
		fmt.Println("3:", diff_3)
	}
	if players == 4 {
		diff_4 := rand_num - player4
		fmt.Println("4:", diff_4)
	}
	if players == 5 {
		diff_5 := rand_num - player5
		fmt.Println("5:", diff_5)
	}
}
*/

func main() {
	fmt.Println("========START========\n1 for normal, 2 for special (not available by default. slow. made while nasty.)")
	var game_runner int
	fmt.Scan(&game_runner)
	if game_runner == 1 {
		normal()
		/*
			} else if game_runner == 2 {
				special()
		*/
	} else {
		fmt.Println("Error. Invalid Input.")
	}
}
