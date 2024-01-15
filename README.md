# Quiz Software Management System

This Python program is a quiz software management system that interacts with a MySQL database to input data for a quiz competition. The system provides a menu-driven interface to manage various aspects of the quiz, including entering questions, participants, updating scores, displaying data, and more.

## Database Connection
- The program uses the `mysql.connector` module to connect to a MySQL database named `quiz_comp` running on the local machine.
  
## Tables
The program interacts with the following tables in the database:
1. `questions1`: General questions for various subjects.
2. `maths`, `science_GK`, `astronomy`, `tourism`, `sports`, `entertain`: Specific subject-wise question tables.
3. `participants`: Table to store participant information.
4. `scores`: Table to store participant scores.
5. `questions2`: Table for HOTS(higher order thinking), Rapid Fire, and Multiple Correct questions.

## Program Execution Flow
1. The program starts with an introduction, displaying the available tables.
2. The user is prompted to enter the table number they want to interact with.
3. Based on the user's choice, the program performs various operations such as entering questions, participants, updating scores, displaying data, etc.

## Choices
- **Choice 1:** Entering Questions
  - The user can select the category of quiz questions and enter the details.
- **Choice 2:** Entering Participants
  - Allows the user to input participant details.
- **Choice 3:** Updating Scores
  - Enables the user to update scores for participants and displays the total marks with negative marking.
- **Choice 4:** Displaying Tables
  - Offers options to display different tables in the database.
- **Choice 5:** Entering Second Level Quiz Questions
  - Allows the user to input questions for HOTS, Rapid Fire, and Multiple Correct categories.

## Feedback
- After completing the interaction, the user has the option to provide feedback on the quiz software.
