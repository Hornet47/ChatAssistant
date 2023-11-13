// components/InputBox.tsx
import React, { useState } from 'react';

interface InputBoxProps {
  onSendMessage: (text: string) => void;
}

const InputBox: React.FC<InputBoxProps> = ({ onSendMessage }) => {
  const [message, setMessage] = useState('');

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setMessage(event.target.value);
  };

  const handleSendMessage = () => {
    if (message.trim() !== '') {
      onSendMessage(message);
      setMessage('');
    }
  };

  return (
    <div className="mt-4">
      <input
        type="text"
        value={message}
        onChange={handleInputChange}
        placeholder="Type your message..."
        className="p-2 border rounded"
      />
      <button onClick={handleSendMessage} className="ml-2 bg-blue-500 text-white p-2 rounded">
        Send
      </button>
    </div>
  );
};

export default InputBox;
