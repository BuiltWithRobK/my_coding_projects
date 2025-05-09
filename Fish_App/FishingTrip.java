// Need to give user options on what they want to do in the app. This class should also collect all of the info for 
// the fishing trip to distribute throughout the app and store it in some database.

import java.util.Scanner;

class FishingTrip{
    
    public static void main (String[] args){
        
        // Display welcome and app menu
        System.out.println("Welcome to the Fishing Log App!");
        System.out.println("________________________________" + "\n");
        System.out.println("Enter a NUMBER" + "\n");
        System.out.println("1. Add new trip");
        System.out.println("2. View all trips");
        System.out.println("3. Search trips by location");
        System.out.println("4. Search trips by date");
        System.out.println("5. Save log");
        System.out.println("6. Load log");
        System.out.println("7. Quit");

        // Request what the user wants to do in the app
        Scanner scan1 = new Scanner(System.in);
        int choice = scan1.nextInt();

        // Determine which path user takes and what actions can be done.
        if (choice == 1){
            System.out.println("Enter trip location.");
            Scanner scan2 = new Scanner(System.in);
            String location = scan2.nextLine();

            System.out.println("Enter date of trip.");
            Scanner scan3 = new Scanner(System.in);
            String date = scan3.nextLine();

            System.out.println("Enter time of day.");
            Scanner scan4 = new Scanner(System.in);
            String time = scan4.nextLine();

            System.out.println("Enter fish Species caught.");
            Scanner scan5 = new Scanner(System.in);
            String species = scan5.nextLine();
            
            System.out.println("Enter number of fish caught");
            Scanner scan6 = new Scanner(System.in);
            int numberCaught= scan6.nextInt();

            System.out.println("Your trip info: \n" + location + "\n" + date + "\n" + time + "\n" + species + "\n" + numberCaught);
        }
        else if (choice == 2) {
            System.out.println("Now the user can view all trips!");
            //find source file and output all trips recorded
        }
        else if (choice == 3) {
            System.out.println("Now the user can view trips by location!");
            //request user input for specific location and set variable
            //then take input, make sure it is cleaned well enough to not output errors... all lower?
            //then open source file for data storage and search based on input
            //output all matching searches
        }
        else if (choice == 4) {
            System.out.println("Now the user can view trips by date!");
            //request user input for specific date and set variable... seperate entry for m d and y
            //then take input, make sure it is cleaned well enough to not output errors and combine into one date
            //then open source file for data storage and search based on input
            //output all matching searches for date
        }
        
    }
   
}