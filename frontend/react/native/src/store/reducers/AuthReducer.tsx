import { ReducerState, ReducerAction, ActionTypes } from "../../interfaces/Auth";

const initialState: ReducerState = {
 googleUser: null,
 token: null,
 isLoading: false,
 responseMsg: null
}

const reducer = (state: ReducerState = initialState, action: ReducerAction) => {
  if (ActionTypes[action.type]) {
    return {
      ...state,
      ...action
    }
  }
  return state
}

export default reducer