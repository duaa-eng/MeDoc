// webapp/static/webapp/script.js

    document.addEventListener('DOMContentLoaded', () => {
        const chatForm = document.getElementById('chat-form');
        const userInput = document.getElementById('user-input');
        const conversation = document.getElementById('conversation');

        // Scroll conversation to the bottom
        conversation.scrollTop = conversation.scrollHeight;

        // Submit the form when the user presses Enter key
        userInput.addEventListener('keypress', (event) => {
            if (event.key === 'Enter') {
                event.preventDefault();
                chatForm.submit();
            }
        });

        // Focus on the user input field
        userInput.focus();
    });
