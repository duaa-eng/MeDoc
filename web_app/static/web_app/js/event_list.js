$(document).ready(() => {
    let type = sessionStorage.getItem("type");
    let date = sessionStorage.getItem("date");
    let provider = sessionStorage.getItem("provider");
    let title = sessionStorage.getItem("eventTitle");
    if (type == null || date == null || provider == null || title == null)
        location.href="index.html";
    $("#titleDiv").append(`<h3 id="title">${type} Event</h3>`);
    db.collection("events").doc(type).get().then((doc) => {
        Object.keys(doc.data()).forEach((i) => {
            if (i === date)
                doc.data()[i].forEach((j) => {
                    if (j.email === provider && j.title === title) {
                        let content = j.content;
                        let startIndex = 0;
                        let endIndex = 0;
                        while (startIndex != -1) {
                            startIndex = content.indexOf("src=\"", content.indexOf("img",endIndex)+3);
                            if (startIndex != -1)
                                endIndex = content.indexOf("\"", startIndex+5);
                            content = [content.slice(0,endIndex+1), "class='img-fluid'", content.slice(endIndex+1)].join('');
                        }
                        $("#eventDiv").append(content);
                    }
                })
        })
    })
    db.collection("users").doc(provider).get().then((doc) => {
        $("#footerDiv").append(`<footer><p>Date: ${date}</p> <p>Provider: ${doc.data().companyName}</p><p>Email: ${provider}</p></footer>`)
    })
})