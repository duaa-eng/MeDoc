let email;
auth.onAuthStateChanged((user => {
    if (user) {
        email = user.email;
    }
}))
function getType() {
    console.log("Getting type");
    db.collection("type").get().then((query) => {
        query.forEach((doc) => {
            $("#type").append("<option value=\""+doc.data().name+"\">"+doc.data().name+"</option>");
        });
    }).catch((e) => {
       console.log("Error getting documents: " , e);
    });
}

function addResource(type, title, content, state) {
    const field = new firebase.firestore.FieldPath(email);
    db.collection("resources").doc(type).update(
        field , firebase.firestore.FieldValue.arrayUnion({title:title, content: content})
    ).then(() => {
        console.log("Resources Added Success");
    }).catch((error) => {
        console.error("Error adding document: ", error);
    })

    db.collection("type").doc(type).update({
        isEmpty: false
    }).then(() => {
        console.log("isEmpty status changed")
        if (state === 1)
            location.href = "provider_main.html";
        if (state === 0)
            location.href = "add.html";
    }).catch((error) => {
        console.error("Error setting isEmpty: ", error);
    })
}

function addEvents(type, title, content, startDate, startTime, endDate, endTime, state) {
    const value = {
                    title: title,
                    email: email,
                    content: content,
                    startTime: startTime,
                    endTime: endTime
                    };
    for (let i = new Date(startDate); i <= new Date(endDate); i.setDate(i.getDate()+1)) {
        let date = i.getFullYear()+"-"+(i.getMonth()+1)+"-"+(i.getDate()+1);
        db.collection("events").doc(type).update({
            [date] : firebase.firestore.FieldValue.arrayUnion(value)
        }).then(() => {
            console.log("Events Added Success");
        }).catch((error) => {
            console.error("Error adding document: ", error);
        })
        console.log();
    }

    db.collection("type").doc(type).update({
        isEmpty: false
    }).then(() => {
        console.log("isEmpty status changed")
        if (state === 1)
            location.href = "provider_main.html";
        if (state === 0)
            location.href = "add.html";
    }).catch((error) => {
        console.error("Error setting isEmpty: ", error);
    })

}

function submitForm(state) {
    const type = $("#type option:selected").val();
    const title = $("#title").val();
    const content = tinymce.get("texteditor").getContent();
    const startDate = $("#startDate").val();
    const startTime = $("#startTime").val();
    const endDate = $("#endDate").val();
    const endTime = $("#endTime").val();
    if (startDate == "")
        addResource(type, title, content, state);
    else
        if (startTime != "" && endDate != "" && endTime != "")
            addEvents(type, title, content, startDate, startTime, endDate, endTime, state);

}

$("#submit").click((e) => {
    e.preventDefault();
    submitForm(1);
})
$("#another").click((e) => {
    e.preventDefault();
    submitForm(0);
})
$(document).ready(async () => {
    await getType();
    $("#startDate").change(() => {
        if ($("#startDate").val() != "") {
            $("#startTime").prop("disabled", false);
            $("#endDate").prop("disabled", false);
            $("#endTime").prop("disabled", false);
        } else {
            $("#startTime").prop("disabled", true);
            $("#endDate").prop("disabled", true);
            $("#endTime").prop("disabled", true);
        }
    })
})