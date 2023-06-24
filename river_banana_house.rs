//This program was written to encourage individuals to take action for the betterment of their community.

//Imports 
use std::string::String;

fn main() {
    // Variables to track the status of the action taken 
    let mut action_taken = false;
    let mut progress_made = 0;
    
    // Prints welcome message to introduce the program 
    println!("Welcome to 'Youth in Action'!");
    println!("This program was created to empower youth to take action and make positive changes in their community.");
    println!("Let's get started!");
    
    // Loop to execute the program 
    while !action_taken {
        // Prompts user to enter their idea 
        println!("What action would you like to take?");
        let mut action = String::new();
        std::io::stdin().read_line(&mut action).expect("Error reading user input");
        
        // Checks to see if action meets requirements 
        let action_lower = action.to_lowercase();
        if action_lower.contains("volunteer") || action_lower.contains("donate") || action_lower.contains("fundraise") {
            println!("Great! Your action has been accepted!");
            action_taken = true;
            progress_made += 1;
        } else {
            println!("Sorry, that action is not accepted. Please enter an action which fits into our criteria.");
            println!("You can volunteer, donate, or fundraise!");
            action_taken = false;
        }
    }
    
    // Once action is accepted, prompt the user to enter how many people they plan to involve 
    println!("Now, how many people do you plan to involve in your action?");
    let mut num_involved = String::new();
    std::io::stdin().read_line(&mut num_involved).expect("Error reading user input");
    let num_involved: u32 = num_involved.trim().parse().expect("Error converting user input to numerical value");
    println!("Great, so you will involve {} people in your action!", num_involved);
    progress_made += 1;
    
    // Prompts user to enter a timeframe for when they will take action 
    println!("Now, when do you plan to take action?");
    let mut time_frame = String::new();
    std::io::stdin().read_line(&mut time_frame).expect("Error reading user input");
    println!("Great, so you will take action {}!", time_frame);
    progress_made += 1;
    
    // Prompts user to enter a goal they hope to achieve with their action 
    println!("Now, what do you plan to achieve with your action?");
    let mut goal = String::new();
    std::io::stdin().read_line(&mut goal).expect("Error reading user input");
    println!("Great, so your goal is {}!", goal);
    progress_made += 1;
    
    // Prints out success message
    println!("Congratulations! You have taken the first steps to making a positive change in your community!");
    
    // Prints out progress made in the program 
    println!("You have made {}% progress in this program!", (progress_made/3)*100);
    
    // Prints out closing message 
    println!("Good luck in taking action!");
    println!(" Thank you for using 'Youth in Action'!");
}