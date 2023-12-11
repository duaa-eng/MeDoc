
// log out
const logout = document.querySelector('#logout');
logout.addEventListener('click', (e) => {
    e.preventDefault();

    auth.signOut().then(() => {
        console.log('User signed out');
        location.replace('html1-1.html');
    });
});
