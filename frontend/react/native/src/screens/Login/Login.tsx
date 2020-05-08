import React, { useEffect } from 'react'
import { View, Text } from 'react-native'
import { Button } from 'react-native-elements'
import { StoreState } from '../../interfaces'

interface Props {
  state: Partial<StoreState>,
  actions: {
    signin: Function
  }
}

function Login(props: Props) {

  const { actions: { signin }} = props

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text style={{ fontSize: 36, margin: 8 }}>Muxomor Taxi: Login</Text>
      <Button title='Google OAuth'  raised onPress={() => signin()} />
    </View>
  )
}

export default Login
