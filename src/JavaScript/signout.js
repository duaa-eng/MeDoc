// listen for auth status changes
auth.onAuthStateChanged(user => {
    if (user) {
        // user not verified, redirect to verification page
        if (!user.emailVerified){
            console.log("user not verified");
            location.href='verification.html';
        } else {
            console.log('user verified');
            document.querySelector('#page').style.display = 'block';
        }
    } else {
        console.log('user not authenticated');
        location.href='login.html';
    }
});
// log out
$("#logout").click((e) => {
    e.preventDefault();
    auth.signOut().then(() => {
        console.log('User signed out');
        location.replace('index.html');
    });
});