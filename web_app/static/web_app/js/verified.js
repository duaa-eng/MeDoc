auth.onAuthStateChanged(user => {
    if (user) {
        console.log(user);
        if (!user.emailVerified){
            console.log('user not verified');
            user.sendEmailVerification();
        } else {
            console.log("user verified");
            // redirect to page if logged in
            location.href = "provider_main.html";
        }
    } else {
        location.href='login.html';
    }
});

// log out
$("#logout").click((e) => {
    e.preventDefault();
    auth.signOut().then(() => {
        console.log('User signed out');
        location.replace('login.html');
    });
});