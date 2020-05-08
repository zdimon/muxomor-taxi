import React, { useEffect } from 'react'
import { View, Text } from 'react-native'
import env from '../../../env'
import { StoreState } from '../../interfaces'

interface Props {}

function Login(props: Props & Partial<StoreState>) {

  useEffect(() => {
    console.log(props)
  }, [])

  return (
    <View>
      <Text>{env.API_URL}</Text>
    </View>
  )
}

export default Login
