import React from 'react';

export const BackButton = ({callback}) =>{
        return(
            <button onClick={() => {callback}}/>
        )
}