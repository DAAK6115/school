// Configure the WebSocket connection
const userId = JSON.parse(document.getElementById('user-id').textContent);
const chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/' + userId + '/'
);

// Handle incoming messages
chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const chatLog = document.querySelector('#chat-log');
    chatLog.value += `${data.message}\n`;
};

// Handle WebSocket connection closure
chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

// Send a message when the user clicks the send button
document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = ''; // Clear the input box
};

// Optionally, handle "Enter" key press for sending messages
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.key === 'Enter') { // Check if Enter key is pressed
        document.querySelector('#chat-message-submit').click();
    }
};
