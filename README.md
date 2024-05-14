**AirBnB Clone Project**

This is a Python project aimed at creating a simplified version of the popular vacation rental online marketplace, AirBnB. The project includes a command-line interface (CLI) for managing and interacting with properties, users, and bookings.

**Command Interpreter Description:**

The command interpreter serves as the primary interface for interacting with the AirBnB clone. It allows users to perform various operations such as creating, updating, and deleting properties, managing user accounts, and making bookings. The command interpreter operates in a text-based environment, accepting commands from the user and executing corresponding actions.

**How to Start the Command Interpreter:**

1. Clone the repository:  
   ```
   git clone https://github.com/your_username/airbnb_clone.git
   ```
2. Navigate to the project directory:  
   ```
   cd airbnb_clone
   ```
3. Start the command interpreter:  
   ```
   python console.py
   ```

**How to Use the Command Interpreter:**

Once the command interpreter is running, you can interact with it using various commands. Here are some common commands and their descriptions:

- `help`: Displays a list of available commands and their descriptions.
- `create <class_name>`: Creates a new instance of the specified class (e.g., `create User`).
- `show <class_name> <id>`: Displays details of the instance with the specified ID (e.g., `show Place 1234`).
- `update <class_name> <id> <attribute_name> "<new_value>"`: Updates the specified attribute of the instance with the specified ID (e.g., `update Review 5678 text "Great experience!"`).
- `destroy <class_name> <id>`: Deletes the instance with the specified ID (e.g., `destroy Amenity 9876`).
- `quit`: Exits the command interpreter.

**Examples:**

- To create a new user:
  ```
  create User
  ```
- To display details of a property with ID 1234:
  ```
  show Place 1234
  ```
- To update the description of a property with ID 5678:
  ```
  update Place 5678 description "New description"
  ```
- To delete a review with ID 9876:
  ```
  destroy Review 9876
  ```

Feel free to explore and experiment with other commands to manage your AirBnB clone effectively!
