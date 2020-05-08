export enum ActionTypes {
  SET_AUTH_GOOGLE_USER = 'SET_AUTH_GOOGLE_USER',
  SET_AUTH_TOKEN = 'SET_AUTH_TOKEN'
}

export interface ReducerState {
  googleUser: any,
  token: string | null
}

export interface ReducerAction {
  type: ActionTypes,
  payload: any
}