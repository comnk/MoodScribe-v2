"use client";
import React, { useEffect, useState } from "react";
import Link from 'next/link';

function Page() {
  const [message, setMessage] = useState("Loading");
  const [people, setPeople] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8080/api/test")
      .then((response) => response.json())
      .then((data) => {
        setMessage(data.message);
        setPeople(data.people);
      });
  }, []);

  return (
    <div>
      <h1>
        <Link href="/login/">Login</Link>
      </h1>
      <div>{message}</div>
      {people.map((person, index) => (
        <div key={index}>{person}</div>
      ))}
    </div>);
}

export default Page;
