'use client';

import Link from 'next/link';

import React, { useState, useEffect } from 'react'
import { EditorState } from 'draft-js';
import { Editor } from 'react-draft-wysiwyg';

import 'react-draft-wysiwyg/dist/react-draft-wysiwyg.css';
import './entry-page.css'

export default function edit_entry() {
    const [message, setMessage] = useState("");
    const [author, setAuthor] = useState("");
    const [editorState, setEditorState] = useState<EditorState>(EditorState.createEmpty());

    const onEditorStateChange = (newEditorState: EditorState): void => {
      setEditorState(newEditorState);
    };

    useEffect(() => {
        fetch("http://localhost:8080/api/generate_quote")
          .then((response) => response.json())
          .then((data) => {
            setMessage(data.message);
            setAuthor(data.author);
          });
    }, []);

    return (
      <>
        <h1>First Post</h1>
        <h2>
            <Link href="/">Back to home</Link>
        </h2>
        <p>{message} - {author}</p>
        <Editor
        editorState={editorState}
        onEditorStateChange={setEditorState}
        wrapperClassName="wrapper-class"
        editorClassName="editor-class"
        toolbarClassName="toolbar-class"
        />
      </>
  );
}