import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
  import { Searchbar } from 'react-native-paper';


export default class MyComponent extends React.Component {
  state = {
    firstQuery: '',
  };


  sendQuery(query) {
    // window.location.href + query
    console.log(query)
  }


  render() {
    // const { firstQuery } = this.state;
    // return (
    //   <Searchbar
    //     placeholder="Search"
    //     onChangeText={query => { 
    //       this.setState({ firstQuery: query });
    //       this.sendQuery(query)
    //     }}
    //     value={firstQuery}
    //   />
    // );
  
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
