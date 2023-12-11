async function addUser() {
    console.log("in add user");
    email = $("#signup_email").val();
    providerName = $("#signup_name").val();
    userName = $("#signup_UserName").val();
    pwd = $("#signup_Password").val();
    console.log("email=" + email);
    db.collection("users").doc(userName).get().then((doc) => {
        if(doc.exists){
            alert("account already exists.");
        } else {
            db.collection( "users").doc(userName).set({
                email: email,
                providerName: providerName,
                userName: userName,
                password: pwd
            }).then((docRef) => {
                alert("Good Add");
            }).catch((error) => {
                console.error("Error adding document: ", error);
            });
        }
    }).catch((error) => {
        console.log("check statement error: ", error);
    })
}

async function login() {
    console.log("in login");
    uName = $("#userName").val();
    pwd = $("#password").val();
    loginType = $("#loginType").val();
    console.log("userName = " + uName + "\r\npwd = " + pwd);
    var account = db.collection(loginType).doc(uName).get();
    console.log("account info: ", (await account).data());
    account.then((doc) => {
        if (doc.exists) {
            console.log("Doc data: ", account);
            if (loginType == "users")
                window.open("provider_main.html","_self");
            alert("Account Exists");
        } else {
            console.log("No such doc");
            alert("nonexisting account");
        }
    }).catch((error) => {
        console.log("Error getting document:", error)
    });
}


