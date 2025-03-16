import { useState } from "react";
import StoryEntryForm from "./StoryEntryForm";
import { BiasGradientBar } from "./BiasGradientBar";
import { BackButton } from "./BackButton";


function Wrapper(){
    const [story, setStory] = useState("");
    const [getBias, setBias] = useState([]);
    const [submitted, setSubmitted] = useState(false);
    
    const inputChange = (value) => {
        setStory(value)
    };
    const backNav = (e) => {
        setSubmitted(false)
        setStory("")
    }
    const formSubmit = async (e) => {
        const srch = story.trim();
        e.preventDefault();
                fetch('http://127.0.0.1:8000/create/',
                {method: 'POST',
                 headers: {
                    'Accept': 'application/json',
                    "Content-type": "application/json"
                },
                body: JSON.stringify({
                    'query': srch,
                    'source_bias': "a"
                 }),
            })
        
        await fetch('http://127.0.0.1:8000/retrieve/')
            .then(response => response.json())
            .then((json) =>{setBias(JSON.parse(json.source_bias))})
            .then(setSubmitted(true))
            console.log(submitted)
        };
        console.log(getBias)

    
    return(
        <div>News Bias{submitted ? 
        <BiasGradientBar
            getBias={getBias}
            callback={backNav}
            />
        :
        
        <StoryEntryForm
        story = {story} 
        storySetter={inputChange}
        callBack={formSubmit}
        />
        }</div>
       
    )
}
export default Wrapper