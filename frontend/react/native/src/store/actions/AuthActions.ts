import { ThunkDispatch } from "redux-thunk";
import { Platform, Alert } from 'react-native'
import { logInAsync } from 'expo-google-app-auth'

import env from '../../../env'
import { $dispatch } from "..";
import { ReducerState, ReducerAction, ActionTypes } from "../../interfaces/Auth";

const { IOS_CLIENT_ID, ANDROID_CLIENT_ID } = env

let credentials: { iosClientId?: string, androidClientId?: string } = {}

if (Platform.OS === 'ios') credentials = { iosClientId: IOS_CLIENT_ID }
if (Platform.OS === 'android') credentials = { androidClientId: ANDROID_CLIENT_ID }


export const signin = () => async (dispatch: ThunkDispatch<ReducerState, any, ReducerAction>) => {
  try {
    $dispatch(ActionTypes.SET_AUTH_LOADING, { isLoading: true }, dispatch)
    const result = await logInAsync({
      ...credentials,
      scopes: ["profile", "email"]
    })
    console.log(result)
  } catch ({ message }) {
    $dispatch(ActionTypes.SET_AUTH_RESPONSE_MSG, { responseMsg: message }, dispatch)
    Alert.alert('Error', message)
  } finally {
    $dispatch(ActionTypes.SET_AUTH_LOADING, { isLoading: false }, dispatch)
  }

}