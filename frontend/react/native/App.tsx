import React from 'react';
import { StyleSheet } from 'react-native';
import 'react-native-gesture-handler'
import { NavigationContainer } from '@react-navigation/native'
import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk'

import appStore from './src/store'
import AuthNavigator from './src/navigators/AuthNavigator'

const store = createStore(appStore, applyMiddleware(
  thunk
))

export default function App(): JSX.Element {
  return (
    <Provider store={store}>
      <NavigationContainer>
        <AuthNavigator />
      </NavigationContainer>
    </Provider>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
