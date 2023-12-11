// check authentication
auth.onAuthStateChanged(user => {
    if (!user) {
        location.replace('html1-1.html');
    }
});

// connect to login page
const createGuide = document.querySelector('#loginPage');
createGuide.addEventListener('click', (e) => {
    e.preventDefault();
    location.replace('contains.html');
});

// create new guide
const createForm = document.querySelector('#create-form');
createForm.addEventListener('submit', (e) => {
    e.preventDefault();

    db.collection('events').add({
        title: createForm['title'].value,
        detail: createForm['content'].value,
        date: Date.now()
    }).then(() => {
        console.log("added");
        location.replace('contains.html');
    }).catch(error => {
        console.log(error.message);
    })

})