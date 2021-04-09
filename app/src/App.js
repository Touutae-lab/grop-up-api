import React, { useEffect, useState} from "react"
import './App.css'


function App(){
    useEffect(() => {
        fetch('/get').then(response => 
            response.json().then(data => {
                console.log(data.event.provider);
            })
        );
    }, [])
    return <div className="App" />;
}

export default App;