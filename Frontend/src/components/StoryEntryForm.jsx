import React from "react";

const StoryEntryForm= ({story, storySetter, callBack, state}) =>{
        return (
            <form className="StoryEntryForm" onSubmit={callBack}>
                <input type ="text" className = 'query-input'
                value = {story}
                placeholder = 'Search a story here!' 
                onChange={(e) =>storySetter(e.target.value)}/>
                <button type ='submit' className = 'submit-btn'/>
            </form>
        )
    }
   

export default StoryEntryForm