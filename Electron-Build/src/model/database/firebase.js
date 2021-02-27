window.$ = window.jQuery = require("jquery");

document.addEventListener("DOMContentLoaded", event => {
    const app = firebase.app()
});
document.getElementById("gbutton").addEventListener("click", authentication_google);

function authentication_email(email, password) {


}

function authentication_google() {
    const provider = new firebase.auth.GoogleAuthProvider();

    firebase.auth().signInWithPopup(provider)
        .then(result => {

            const user = result.user;
            document.write(`Hello ${user.displayName}`);
            document.write(`ID: ${user.id_token}`);
            console.log();
        })
        .catch(console.log)
}




function authentication_phone(phone_num) {
    continue
}