import { ThunkDispatch } from "redux-thunk";
import { ReducerState, ReducerAction } from "../../interfaces/Auth";

export const signin = () => (
  dispatch: ThunkDispatch<ReducerState, any, ReducerAction>, 
  getState: () => ReducerState) => {
  
  const state = getState()
  
  console.log('Sign in fired...', state)
   
}