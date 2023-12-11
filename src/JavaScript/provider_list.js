function getDetail(index) {
    sessionStorage.setItem("resourceIndex", index);
    window.open("resource_detail.html")
}
$(document).ready(() => {
    let type = sessionStorage.getItem("type");
    let provider = sessionStorage.getItem("provider");
    if (type == null || provider == null)
        location.href="index.html";
    db.collection("resources").doc(type).get().then((doc) => {
        Object.keys(doc.data()).forEach((i) => {
            if (i === provider) {
                db.collection("users").doc(provider).get().then((userDoc) => {
                    $("#titleDiv").append(`<h3 id="title">${type}</h3>`)
                    const providerLocation = userDoc.data().location;
                    const searchPara = providerLocation.replace(" ","+");
                    const url = `<a href='https://www.google.com/maps/search/?api=1&query=${searchPara}' target="_blank">${providerLocation}</a>`
                    $("#location").append(url);
                    $("#mission").append(userDoc.data().content);
                    $("#companyName").append(userDoc.data().companyName);
                    $("#phone").append(userDoc.data().phone);
                    $("#email").append(userDoc.data().email);
                })
                doc.data()[i].forEach((j, index) => {
                    let content = j.content;
                    let img = "";
                    if (content.indexOf("img") != -1) {
                        let startIndex = content.indexOf("src=\"", content.indexOf("img")+3);
                        let endIndex = content.indexOf("\"", startIndex+5);
                        img = content.substring(startIndex+5, endIndex);
                        $("#resourceList").append(`<div class="resourceDiv text-center" onclick='getDetail(${index})'>
                                                <img src="${img}" alt="Resource Image" style="padding: 10px; width: 100%">
                                                <h4 class="resourceTitle">${j.title}</h4>
                                                </div>`)
                    } else {
                        db.collection("type").doc(type).get().then((typeDoc) => {
                            img = typeDoc.data().img;
                            if (img.indexOf("http") == -1)
                                img = "src/Image/"+img;
                            $("#resourceList").append(`<div class="resourceDiv text-center" onclick='getDetail(${index})'>
                                                <img src="${img}" alt="Resource Image" style="padding: 10px; width: 100%">
                                                <h4 class="resourceTitle">${j.title}</h4>
                                                </div>`)
                        })
                    }
                })
            }
        })
    })
})