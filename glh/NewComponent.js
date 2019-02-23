import React, { Component } from 'react';

class NewComponent extends Component {
  render() {
    return (
        <h2> {this.props.text} </h2>
    );
  }
}

export default NewComponent;