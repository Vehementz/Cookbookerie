# Litteral Types
type HelloLiteral = "Hello";

# String litteral
let hello: HelloLiteral = "Hello"; # Good
let hello: Helloliteral = "hi"; # Error ! 

let hello: "Hello" = "Hello";  # Good
let hello: "Hello" = "hi";  # Wrong

# Narrowing
let text: string = "Text";
let text: "The text" = "The text";

# Control flow analysis 
function sendReply(text: string) {
  if (text === "Hello") {
  console.log(text);
  }
}

