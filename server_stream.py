import cv2
import zmq
import numpy as np


def display_stream():
    # Create a ZeroMQ context and socket
    context = zmq.Context()
    socket = context.socket(zmq.SUB)

    # Connect the socket to the RTSP server address
    socket.connect("tcp://192.168.103.228:5555") # Replace "rtsp_server_address" with the actual address

    # Set the subscription filter
    socket.setsockopt_string(zmq.SUBSCRIBE, "")

    while True:
        # Receive the encoded frame from the serverq
        encoded_frame = socket.recv()

        # Decode the frame
        frame = np.frombuffer(encoded_frame, dtype=np.uint8)
        frame = cv2.imdecode(frame, 1)

        # Display the frame
        cv2.imshow('RTSP Stream', frame)

        # Check for 'q' key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

print("now is running, However server off")
# Release the resources
cv2.destroyAllWindows()



if __name__ == '__main__':
    display_stream()
    print("camera show")

