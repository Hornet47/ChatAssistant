'use client'
import { useState } from "react";
import SearchIcon from "./search.svg";
import "./globals.css"

export default function Home() {
  const [message, setMessage] = useState<string>("");
  const [messages, setMessages] = useState<string[]>([]);

  const sendMessage = async (message: string) => {
    const response: string = "Hello!";

    setMessages([...messages, message, response]);
  };

  return (
    <div className="app">
      <div>
        <h1>Chat</h1>
      </div>
      
      <div>
        {messages?.length > 0 ? (
          <div className="container">
            {messages.map((m) => (
              <div className="movie">{m}</div>
            ))}
          </div>
        ) : (
          <div className="empty">
            <h2>No messages</h2>
          </div>
        )}
      </div>

      <div className="search">
        <input
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Send a message: "
        />
        <img
          src={SearchIcon}
          alt="search"
          onClick={() => sendMessage(message)}
        />
      </div>
    </div>
  );
}
