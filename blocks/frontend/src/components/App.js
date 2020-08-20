import React from "react";
import { render } from "react-dom";
import SideBar from './SideBar';
import MxGraphGridAreaEditor from './MxGraphGridAreaEditor';

export default class App extends React.Component {
  render() {
    return (
        <div>
            <SideBar />
            <MxGraphGridAreaEditor />
        </div>
    );
  }
}

const container = document.getElementById("app");
render(<App />, container);
