import { randomInt } from "node:crypto";
import { createInterface } from "node:readline";
import { spawn } from "node:child_process";
import { platform } from "node:os";

function open(url: string): void {
  let command: string;
  let args: string[];

  if (platform() === "win32") {
    command = "rundll32";
    args = ["url.dll,FileProtocolHandler", url];
  } else if (platform() === "darwin") {
    command = "open";
    args = [url];
  } else {
    command = "xdg-open";
    args = [url];
  }

  const process = spawn(command, args, {
    detached: true,
    stdio: "ignore",
  });

  process.on("error", (error) => {
    console.log(`Could not open browser: ${error.message}`);
  });

  process.unref();
}

function runPythonScript(): void {
  const python = platform() === "win32" ? "python" : "python3";

  const process = spawn(python, ["python/xd.py"], {
    stdio: "inherit",
  });

  process.on("error", (error) => {
    console.log(`Could not run Python script: ${error.message}`);
  });
}

async function normal(): Promise<void> {
  const randomNum = randomInt(1, 101); // Upper limit is exclusive
  let tries = 0;

  const terminal = createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  console.log("A number between 1 and 100 has been stored.");

  try {
    while (true) {
      const rawInput = await terminal.question("\nEnter your guess\n] ");
      const input = rawInput.trim();

      if (input === "cheatmode") {
        console.log(`YOU WIN!!\nYour guess: ${randomNum}\nTries: 0`);
        break;
      }

      // Check that the input looks like a whole number, then convert it.
      if (!/^[+-]?\d+$/.test(input)) {
        console.log("Invalid input. Try again.");
        continue;
      }

      const guess = Number(input);

      if (!Number.isSafeInteger(guess)) {
        console.log("Invalid input. Try again.");
        continue;
      }

      if (guess === randomNum) {
        console.log(`YOU WIN!!!\nTries: ${tries}`);
        open("https://youtu.be/c7TNPiryDyg?si=TXVUx6MgcSBFpnEP&t=32");
        break;
      } else if (guess > randomNum) {
        console.log(`${guess} is greater! Try a smaller one!`);
      } else {
        console.log(`${guess} is smaller! Try a greater one!`);
      }

      tries++;
      console.log(`Tries: ${tries}`);
      runPythonScript();
    }
  } finally {
    terminal.close();
  }
}

normal().catch((error) => {
  console.error(error);
});
