// pages/index.tsx
import { useState } from 'react';
import ChatWindow from './components/ChatWindow';
import InputBox from './components/InputBox';

const Home = () => {
  const [messages, setMessages] = useState<string[]>([]);

  const sendMessage = async (text: string) => {
    try {
      // Replace the API endpoint with your backend API
      const response = await fetch('http://localhost:8000/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      });

      const data = await response.json();
      setMessages([...messages, text, data.message]);
    } catch (error) {
      console.error('Error sending message:', error);
    }
  };

  return (
    <div>
      <ChatWindow messages={messages} />
      <InputBox onSendMessage={sendMessage} />
    </div>
  );
};

export default Home;
