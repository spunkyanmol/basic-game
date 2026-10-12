use std::io::{self, Write};
use std::process::Command;

fn open(url: &str) {
    if let Err(error) = webbrowser::open(url) {
        eprintln!("Could not open browser: {error}");
    }
}

fn run_python_script() {
    // Use "python" on Windows and "python3" on Linux/macOS.
    #[cfg(target_os = "windows")]
    let _ = Command::new("python")
        .arg("python/xd.py")
        .status();

    #[cfg(not(target_os = "windows"))]
    let _ = Command::new("python3")
        .arg("python/xd.py")
        .status();
}

fn normal() {
    let random_num: i32 = rand::random_range(1..=100);
    let mut tries = 0;

    println!("A number between 1 and 100 has been stored.");

    loop {
        print!("\nEnter your guess\n] ");
        let _ = io::stdout().flush();

        let mut input = String::new();

        // Read a line from the keyboard.
        match io::stdin().read_line(&mut input) {
            Ok(0) => break, // End of input
            Ok(_) => {}
            Err(error) => {
                eprintln!("Input error: {error}");
                break;
            }
        }

        let input = input.trim();

        if input == "cheatmode" {
            println!("YOU WIN!!\nYour guess: {random_num}\nTries: 0");
            break;
        }

        // Convert the text the user typed into an integer.
        let guess: i32 = match input.parse() {
            Ok(number) => number,
            Err(_) => {
                println!("Invalid input. Try again.");
                continue;
            }
        };

        if guess == random_num {
            println!("YOU WIN!!!\nTries: {tries}");
            open("https://youtu.be/c7TNPiryDyg?si=TXVUx6MgcSBFpnEP&t=32");
            break;
        } else if guess > random_num {
            println!("{guess} is greater! Try a smaller one!");
        } else {
            println!("{guess} is smaller! Try a greater one!");
        }

        tries += 1;
        println!("Tries: {tries}");
        run_python_script();
    }
}

fn main() {
    normal();
}
