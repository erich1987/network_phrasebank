import asyncio
import logging
import handle_client
import listen_for_exit

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

async def start_server():
    """Start the server and manage connections."""
    logging.info("Initializing server...")
    try:
        server = await asyncio.start_server(handle_client.handle_client, '127.0.0.1', 12345)
        logging.info("Server started on ('127.0.0.1', 12345)")
        logging.info("Type 'exit' to shut down the server.")
        logging.debug(f"Listening on {server.sockets[0].getsockname()}")

        async with server:
            # Run the server and the command listener concurrently
            await asyncio.gather(
                server.serve_forever(),
                listen_for_exit.listen_for_exit(server)
            )
    except Exception as e:
        logging.error(f"Server encountered an error: {e}")
    except asyncio.CancelledError:
        logging.info("Server shutting down gracefully.")
    finally:
        logging.info("Server has stopped.")
