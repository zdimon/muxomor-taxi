import React from 'react'
import { createStackNavigator } from '@react-navigation/stack';
import Login from '../screens/Login'

const Auth = createStackNavigator()

export default function AuthNavigator() {
  return (
    <Auth.Navigator>
      <Auth.Screen name="Login" component={Login}  />
    </Auth.Navigator>
  )
}