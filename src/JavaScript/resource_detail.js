$(document).ready(() => {
    let type = sessionStorage.getItem("type");
    let provider = sessionStorage.getItem("provider");
    let index = sessionStorage.getItem("resourceIndex");
    if (type == null || provider == null || index == null)
        location.href="index.html";

    // Use id to fetch corresponding content and title in the future
    // Add an id field in the resource document in the future
    db.collection("resources").doc(type).get().then((doc) => {
        $("#titleDiv").append(`<h3 id="title">Resource ${doc.data()[provider][index].title}</h3>`);
        let content = doc.data()[provider][index].content;
        let startIndex = 0;
        let endIndex = 0;
        while (startIndex != -1) {
            startIndex = content.indexOf("src=\"", content.indexOf("img",endIndex)+3);
            if (startIndex != -1)
                endIndex = content.indexOf("\"", startIndex+5);
            content = [content.slice(0,endIndex+1), "class='img-fluid'", content.slice(endIndex+1)].join('');
        }
        $("#resourceDiv").append(content);
    })
    db.collection("users").doc(provider).get().then((doc) => {
        $("#footerDiv").append(`<footer><p>Provider: ${doc.data().companyName}</p><p>Email: ${provider}</p></footer>`)
    })
})