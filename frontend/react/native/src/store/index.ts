import Auth from './reducers/AuthReducer'
import { combineReducers, Dispatch } from 'redux'

import { ActionTypes as AuthTypes } from '../interfaces/Auth'

export const $dispatch = (type: AuthTypes, payload: any, dispatch: Dispatch) => {
  dispatch({ type, payload })
}

export default combineReducers({
  Auth
})