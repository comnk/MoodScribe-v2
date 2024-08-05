"use client";
import React, { useEffect, useState } from "react";
import Link from 'next/link';

function Page() {
  const [message, setMessage] = useState("Loading");
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8080/api/test")
      .then((response) => response.json())
      .then((data) => {
        setMessage(data.message);
        setItems(data["items"]);
      });
  }, []);

  return (
    <div>
      <nav>
        <p>
          <Link href="/entry/">Edit Entry</Link>
        </p>
        <h3>
          <Link href="/login/">Login</Link>
        </h3>
      </nav>
      <div>{message}</div>
      {Object.keys(items).map((id) => {
          return <li key={id}>{items[Number(id)]["name"]}</li>;
        })}
    </div>);
}

export default Page;
