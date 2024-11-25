import asyncio
import start_client

def display_client_menu():
    """Display the client menu and handle user input."""
    while True:
        print("=== Client Menu ===")
        print("1. Start Client")
        print("2. Help")
        print("3. Exit")

        choice = input("> ").strip().lower()
        if choice == "1" or choice == "start client":
            asyncio.run(start_client.start_client())
            break
        elif choice == "2" or choice == "help":
            print("Help: This is a simple client program.")
            print("Start Client: Connects to the server and sends messages.")
            print("Exit: Closes the client.")
        elif choice == "3" or choice == "exit":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
