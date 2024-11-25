import asyncio
import logging

# Configure logging for the module
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

async def handle_client(reader, writer):
    """Handle an individual client connection."""
    addr = writer.get_extra_info('peername')
    logging.info(f"New connection from {addr}")

    try:
        while True:
            logging.debug(f"Waiting to receive data from {addr}...")
            data = await reader.read(100)  # Read data from the client
            if not data:
                logging.warning(f"No data received from {addr}. Closing connection.")
                break  # Break if no data (client disconnected)

            message = data.decode("utf-8")
            logging.info(f"Message from {addr}: {message}")

            # Echo the message back to the client
            response = f"Server received: {message}"
            logging.debug(f"Sending response to {addr}: {response}")
            writer.write(response.encode("utf-8"))
            await writer.drain()
            logging.info(f"Echoed message back to {addr}: {response}")

            # Handle a client-initiated shutdown
            if message.lower() == "shutdown":
                logging.info(f"Closing connection with {addr} upon client request.")
                writer.write("Server is shutting down. Goodbye!".encode("utf-8"))
                await writer.drain()
                writer.close()
                await writer.wait_closed()
                return

    except ConnectionResetError:
        logging.error(f"Connection with {addr} lost unexpectedly.")
    except Exception as e:
        logging.error(f"Error occurred while handling {addr}: {e}")
    finally:
        logging.info(f"Closing connection with {addr}")
        writer.close()
        await writer.wait_closed()
