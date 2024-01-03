// listen for auth status changes
auth.onAuthStateChanged(user => {
    if (user) {
        db.collection("users").doc(user.email).get().then((doc) => {
            if (!doc.exists) {
                location.replace("profile.html")
            } else {
                const providerLocation = doc.data().location;
                const searchPara = providerLocation.replace(" ","+");
                const url = `<a href='https://www.google.com/maps/search/?api=1&query=${searchPara}'>${providerLocation}</a>`
                $("#location").append(url);
                $("#mission").append(doc.data().content);
                $("#companyName").append(doc.data().companyName);
                $("#phone").append(doc.data().phone);
                $("#email").append(doc.data().email);
            }
        }).catch((error) => {
            console.log("Error fetching user info: ", error);
        })
    } else {
        console.log('user not authenticated');
        location.href='login.html';
    }
});

