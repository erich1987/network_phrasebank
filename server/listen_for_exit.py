async def listen_for_exit(server):
    """Listen for server shutdown commands."""
    while True:
        command = input("> ").strip().lower()
        if command == "exit":
            print("Shutting down the server...")
            server.close()
            await server.wait_closed()
            break
        else:
            print("Invalid command. Type 'exit' to stop the server.")
