import React from 'react';
import { BackButton } from './BackButton';

export const BiasGradientBar = ({getBias, callback}) => {
        return(
            <div>
            <div className="Left-Gradient" style={{background:`linear-gradient(90deg, blue ${getBias[0]}%, green ${getBias[1]}%, yellow ${ 100 - getBias[2]}%, yellow ${getBias[2]}%, orange ${getBias[3]}%, red ${-getBias[4]}%)`}}></div><button onClick={callback}>Search Again</button>
            </div>
        )
}
