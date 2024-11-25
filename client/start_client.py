import asyncio
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

async def start_client():
    """Start the client and connect to the server."""
    host = '127.0.0.1'
    port = 12345
    try:
        logging.info(f"Attempting to connect to server at {host}:{port}...")
        reader, writer = await asyncio.open_connection(host, port)
        logging.info("Connected to server")

        # Send a test message to ensure connection
        test_message = "Hello, Server!"
        writer.write(test_message.encode("utf-8"))
        await writer.drain()
        logging.info(f"Sent test message to server: {test_message}")

        # Wait for server's response
        response = await reader.read(100)
        logging.info(f"Received response from server: {response.decode('utf-8')}")

        # Interactive loop
        while True:
            message = input("Enter a message to send (type 'exit' to quit): ").strip()
            if message.lower() == "exit":
                logging.info("Disconnecting from server...")
                writer.write("shutdown".encode("utf-8"))
                await writer.drain()
                break

           # Send the message to the server
            writer.write(message.encode("utf-8"))
            await writer.drain()

            # Wait for a response with a timeout
            try:
                response = await asyncio.wait_for(reader.read(100), timeout=5.0)
                print(f"Message from server: {response.decode('utf-8')}")
            except asyncio.TimeoutError:
                print("No response from server. Operation timed out.")

        writer.close()
        await writer.wait_closed()

    except ConnectionRefusedError:
        logging.error("No server found. Please ensure the server is running.")
    except asyncio.IncompleteReadError:
        logging.warning("Server closed the connection.")
    except Exception as e:
        logging.error(f"Unexpected error in client: {e}")
    finally:
        logging.info("Client exiting...")


if __name__ == "__main__":
    asyncio.run(start_client())
