// components/ChatWindow.tsx
import React from 'react';

interface ChatWindowProps {
  messages: string[];
}

const ChatWindow: React.FC<ChatWindowProps> = ({ messages }) => {
  return (
    <div className="bg-white p-4 h-64 overflow-y-auto border">
      {messages.map((message, index) => (
        <div key={index} className="mb-2">
          {message}
        </div>
      ))}
    </div>
  );
};

export default ChatWindow;
