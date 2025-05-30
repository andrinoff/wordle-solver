use std::fs::File;
use std::io::{self, BufRead};
use prompted::input;

fn main() -> io::Result<()> {
    let path = "./words.txt"; 
    let file = File::open(path).unwrap_or_else(|e| {
        eprintln!("Error opening '{}': {}", path, e);
        std::process::exit(1);
    });
    let reader = io::BufReader::new(file);

    let lines: Vec<String> = reader.lines().collect::<Result<_, _>>()?;

    // let first_word = input!("Enter the first word: ");
    // println!("You entered: {}", first_word);
    
    println!("{:?}", &lines[0..1]); // Prints the first word

    Ok(())
}   

fn calculate_entropy(p: f32) -> f32 { // Calculates the inverse log with base 2 of the words 
   let entropy = -p.log2();
   println!("Entropy: {}", entropy);
   return entropy;

}


fn calculate_left(word: String, lines: Vec<String>) {
    let tempWords = lines;
    
}





// Tests
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_calculate_entropy() {
    assert_eq!(calculate_entropy(0.5), 1.0)
}
}