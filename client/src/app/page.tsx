"use client";
import React, { useEffect, useState } from "react";

function Page() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("http://localhost:8080/api/test")
      .then((response) => response.json())
      .then((data) => {
        setMessage(data.message);
      });
  }, []);

  return <div>{message}</div>;
}

export default Page;
