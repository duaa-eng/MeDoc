// listen for auth status changes
auth.onAuthStateChanged(user => {
    if (user) {
        console.log('user authenticated');
        // location.replace('contains.html')
    } else {
        console.log('user not authenticated');
    }
});

// sign up
const signupForm = document.querySelector('#signup-form');
signupForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // get user info
    const email = signupForm['signup-email'].value;
    const pwdS = signupForm['signup-password'].value;

    // sign up the user
    auth.createUserWithEmailAndPassword(email, pwdS).then(cred => {
        console.log(cred.user);
        cred.user.sendEmailVerification();
        // reset signupForm
        signupForm.reset();

        db.collection("users").doc(email).set({
            email: email
        }).then((docRef) => {
            alert("Good Add");
        }).catch((error) => {
            console.error("Error adding document: ", error);
        });

        // location.replace('contains.html');
    }).catch(err => {
        document.getElementById('signup_error').innerHTML = err.message.substr(err.message.indexOf(":") + 1,
            err.message.indexOf("(") - err.message.indexOf(":") - 1);
    });

});

// log in
const loginForm = document.querySelector('#login-form');
loginForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // get user info
    const email = loginForm['login-email'].value;
    const pwdL = loginForm['login-password'].value;

    // log user in
    auth.signInWithEmailAndPassword(email, pwdL).then(cred => {
        // reset the page
        loginForm.reset();
        console.log(cred.user);
        location.replace('contains.html');
    }).catch(err => {
        document.getElementById('login_error').innerHTML = err.message.substr(err.message.indexOf(":") + 1,
            err.message.indexOf("(") - err.message.indexOf(":") - 1);
    });
});




