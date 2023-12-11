$("#infoForm").submit((e)=> {
    e.preventDefault();
    const email = firebase.auth().currentUser.email;
    const location = $("#location").val();
    const content = tinymce.get("texteditor").getContent();
    const companyName = $("#name").val();
    const phone = $("#phone").val();
    db.collection("users").doc(email).set({
        email: email,
        location: location,
        content: content,
        companyName: companyName,
        phone: phone
    }).then((docRef) => {
        window.location.href = "provider_main.html";
        console.log("Profile Added");
    }).catch((error) => {
        console.error("Error adding document: ", error);
    });
});

auth.onAuthStateChanged(user => {
    if (user) {
        if(user.emailVerified) {
            db.collection('users').doc(user.email).get().then((doc) => {
                if (doc.exists) {
                    $("#location").val(doc.data().location);
                    tinymce.activeEditor.setContent(doc.data().content);
                    $("#name").val(doc.data().companyName);
                    $("#phone").val(doc.data().phone);
                }
            }).catch((error) => {
                console.log("Error fetching user info: ", error);
            })
        } else {
            location.href='verification.html';
        }
    } else {
        console.log('user not authenticated');
        location.href='login.html';
    }
});