object YouthInAction { // Defines the object YouthInAction 
 
 // 1. Defines a function to print out a welcome message 
 def printWelcomeMessage() {
   println("Welcome to Youth in Action!")
 }
 
 // 2. Defines a function to print out a goodbye message 
 def printGoodbyeMessage() {
   println("Thank you for your participation!")
 }
 
 // 3. Defines a function to print out an introduction 
 def printIntroduction() {
   println("Youth in Action is a program designed to help young people make a difference in their communities.")
 }
 
 // 4. Defines a function to print out a list of events
 def printEvents() {
   println("Upcoming Youth in Action events:")
   println("\t• Youth in Action Leadership Summit, May 25th")
   println("\t• Youth in Action Movie Night, June 15th")
   println("\t• Youth in Action Summer Camp, August 5th-10th")
 }
 
 // 5. Defines a function to print out a mission statement 
 def printMissionStatement() {
   println("Youth in Action is dedicated to empowering young people to create positive change in their communities.")
 }
 
 // 6. Defines a function to print out contact information 
 def printContactInformation() {
   println("For more information, please contact Youth in Action at youthinaction@example.com or 773-000-0000.")
 }
 
 // 7. Defines a function to print out a closing statement 
 def printClosingStatement() {
   println("Now, let's get to work!")
 }
 
 // 8. Defines a function to print all statements 
 def printAllStatements() {
   printWelcomeMessage()
   printIntroduction()
   printEvents()
   printMissionStatement()
   printContactInformation()
   printClosingStatement()
   printGoodbyeMessage()
 }
 
 // 9. Main function to execute all statements
 def main(args: Array[String]) {
   printAllStatements()
 }
}