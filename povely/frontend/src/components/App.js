import React from 'react'
import ReactDom from 'react-dom';

class App extends React.Component {
    
    render() {
        console.log('running')
        return (
            <h1>Hey</h1>
        )
    }
}

ReactDom.render(<App/>, document.getElementById('app'))
