// check authentication
auth.onAuthStateChanged(user => {
    if (user) {
        console.log(user.emailVerified);
        document.querySelector('#list').style.display = 'block';
    } else {
        location.replace('html1-1.html');
    }
});


// get data
db.collection('events').get().then(snapshot => {
    setupGuides(snapshot.docs);
});

// set up guide
const guideList = document.querySelector('#tableBody');
const setupGuides = (data) => {

    let html = '';
    data.forEach(doc => {
        const guide = doc.data();
        const li = `
            <tr>
                <td>
                    ${guide.title}
                </td>
                <td>
                    ${guide.detail}
                </td>
                <td>
                    ${guide.date}
                </td>
            </tr>
        `;
        html += li;
    });
    guideList.innerHTML = html;
}

// connect to create guide
const createGuide = document.querySelector('#createGuide');
createGuide.addEventListener('click', (e) => {
    e.preventDefault();
    location.replace('addDetail.html');
});