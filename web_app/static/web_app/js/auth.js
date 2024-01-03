// listen for auth status changes
auth.onAuthStateChanged(user => {
    if (user) {
        if (!user.emailVerified) {
            console.log('user not verified');
            location.href = 'verification.html';
        } else {
            console.log('user authenticated');
            // redirect to page if logged in
            location.href = 'provider_main.html';
        }
    } else {
        console.log('user not authenticated');
    }
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
        document.getElementById('login_error').innerHTML = '';
        // redirect to page after login
        location.href = "verification.html";
    }).catch(err => {
        document.getElementById('login_error').innerHTML = err.message.substr(err.message.indexOf(":") + 1,
            err.message.indexOf("(") - err.message.indexOf(":") - 1);
    });
});

// sign up
const signupForm = document.querySelector('#signup-form');
signupForm.addEventListener('submit', (e) => {
    e.preventDefault();
    var confirmArea = document.getElementById('confirm_password');
    // get user info
    const email = signupForm['signup_email'].value;
    const pwdS = signupForm['signup_password'].value;
    const cPwd = signupForm['confirm_password'].value;
    if (pwdS !== cPwd) {
        document.getElementById('signup_error').innerHTML = "Passwords don't match";
    } else {
        // sign up the user
        auth.createUserWithEmailAndPassword(email, pwdS).then(cred => {
            console.log("signed up");
            document.getElementById('signup_error').innerHTML = '';

            // reset signupForm
            signupForm.reset();
            location.href = "verification.html";
        }).catch(err => {
            document.getElementById('signup_error').innerHTML = err.message.substr(err.message.indexOf(":") + 1,
                err.message.indexOf("(") - err.message.indexOf(":") - 1);
        });
    }
});

// show password
function showPwd(type) {
    if (type === 'signup') {
        var sign = document.getElementById("signup_password");
        var confirm = document.getElementById('confirm_password');
        if (sign.type === "password" && confirm.type === 'password') {
            sign.type = "text";
            confirm.type = "text";
        } else {
            sign.type = "password";
            confirm.type = "password";
        }
    } else if (type === 'login') {
        var log = document.getElementById("login-password");
        if (log.type === "password") {
            log.type = "text";
        } else {
            log.type = "password";
        }
    }
}