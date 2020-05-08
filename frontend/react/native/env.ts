// @ts-ignore
import { ANDROID_CLIENT_ID, API_URL } from 'react-native-dotenv'
import Constants from 'expo-constants'

const variables = {
  ANDROID_CLIENT_ID,
  API_URL
}

interface Variables { 
  API_URL: string
  ANDROID_CLIENT_ID: string
}

interface ENV {
  dev: Variables
  staging: Variables
  prod: Variables
}

export const prodUrl: string = "https://someapp.herokuapp.com";

const ENV: ENV = {
  dev: {
    ...variables
  },
  staging: {
    ...variables
  },
  prod: {
    ...variables
  }
};

function getEnvVars(env: string = ""): Variables  {
  if (env.indexOf("dev") !== -1) return ENV.dev;
  if (env.indexOf("staging") !== -1) return ENV.staging;
  if (env.indexOf("prod") !== -1) return ENV.prod;
  return ENV.dev
}

export default getEnvVars(Constants.manifest.releaseChannel);
