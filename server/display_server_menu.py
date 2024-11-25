import asyncio
import start_server

def display_server_menu():
    """Display the server menu and handle user input."""
    while True:
        print("=== Server Menu ===")
        print("1. Start Server")
        print("2. Help")
        print("3. Exit")
        
        choice = input("> ").strip().lower()

        if choice == "1" or choice == "start server":
            asyncio.run(start_server.start_server())
            break  # Exit the menu once the server stops
        elif choice == "2" or choice == "help":
            print("\n=== Help Menu ===")
            print("Help: This is a simple server program.")
            print("Start Server: Starts the server and listens for clients.")
            print("Exit: Closes the server.\n")
        elif choice == "3" or choice == "exit":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
