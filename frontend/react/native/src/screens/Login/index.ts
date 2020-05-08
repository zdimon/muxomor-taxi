import { connect } from "react-redux";
import { Dispatch, bindActionCreators } from "redux";

import Login from "./Login";
import { StoreState } from "../../interfaces";
import * as AuthActions from '../../store/actions/AuthActions'

const mapStateToProps = ({ Auth }: StoreState) => ({
  state: { 
    Auth 
  }
})

const mapDispatchToProps = (dispatch: Dispatch) => {
  return {
    actions: bindActionCreators(AuthActions, dispatch)
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(Login)