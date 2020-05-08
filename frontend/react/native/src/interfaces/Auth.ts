export enum ActionTypes {
  SET_AUTH_GOOGLE_USER = 'SET_AUTH_GOOGLE_USER',
  SET_AUTH_TOKEN = 'SET_AUTH_TOKEN',
  SET_AUTH_LOADING = 'SET_AUTH_LOADING',
  SET_AUTH_RESPONSE_MSG = 'SET_AUTH_RESPONSE_MSG'
}

export interface ReducerState {
  googleUser: any
  token: string | null
  isLoading: boolean
  responseMsg: string | null
}

export interface ReducerAction {
  type: ActionTypes
  payload: any
}