import firebase from 'firebase/app';
import 'firebase/auth';
import 'firebase/firestore';
import 'firebase/storage';

// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyASwpwU4gScouDb52SgtITzJGlhVlUaAeM",
    authDomain: "bindr-b1182.firebaseapp.com",
    projectId: "bindr-b1182",
    storageBucket: "bindr-b1182.appspot.com",
    messagingSenderId: "834172641970",
    appId: "1:834172641970:web:9ff63deccdc2ac41b7dfab",
    measurementId: "G-26JDS2433R"
};

firebase.initializeApp(firebaseConfig);

export const auth = firebase.auth();
export const googleProvider = new firebase.auth.GoogleAuthProvider();

export const db = firebase.firestore();
export const storage = firebase.storage();