let dumpCard = "<div class=\"col-md-2 offset-2 card justify-content-center align-items-center\" style=\"visibility: hidden;\">\n" +
    "                                <img class=\"card-img-top\" src=\"src/Image/resource9.png\" alt=\"Resource Image\">\n" +
    "                                <div class=\"card-body\">\n" +
    "                                    <h5 class=\"card-title\">Case Management & Assistance for Immigrant Families</h5>\n" +
    "                                    <p class=\"card-text\">Resource Description</p>\n" +
    "                                </div>\n" +
    "                            </div>";
function addCard(data, divName) {
    let itemCount = 0;
    let temp = '';
    for (let i = 0; i < 9; i+=3) {
        temp += "<div class='row'>\n";
        do {
            if (i+itemCount >= data.length) {
                temp += dumpCard;
            } else {
                temp += "<div class='col-md-2 offset-2 card justify-content-center align-items-center' onclick='getDetail(\""+data[i+itemCount].name+"\")'>\n";
                if (data[i+itemCount].img.indexOf("http") != -1)
                    temp += "<img class='card-img-top' src='" + data[i+itemCount].img + "' alt='Resource Image'>\n<div class=\"card-body\">\n";
                else
                    temp += "<img class='card-img-top' src=src/Image/" + data[i+itemCount].img + " alt='Resource Image'>\n<div class=\"card-body\">\n";
                temp += "<h5 class='card-title'>"+data[i+itemCount].name+"</h5>"
                temp += "<p class='card-text'>"+data[i+itemCount].desc+"</p>";
                temp += "</div>\n</div>"
            }
            itemCount++;
        }while(itemCount < 3);
        temp += "</div>";
        itemCount = 0;
    }
    $("#"+divName).append(temp);
}
function addCarousel(data) {
    let size = data.length;
    let count = 1, page = Math.ceil(size/9), latestDiv = "itemDiv1";
    if (page > 1) {
        for (let i = 1; i < page; i++) {
            let temp = "<li data-target=\"#carouselPage\" data-slide-to=\""+i+"\"></li>";
            $("#carouselIndicator").append(temp);
        }
    }
    for (let i = 1; i <= page; i++) {
        let start = (i-1) * 9, end = start + 9;
        if(count == 1) {
            //For first active carousel item div
            addCard(data.slice(start, end), latestDiv);
        } else {
            //For rest carousel item div
            $("#carouselDisplay").append("<div class='carousel-item' id='itemDiv"+count+"'>");
            latestDiv = "itemDiv" + count;
            addCard(data.slice(start, end), latestDiv);
            $("#carouselDisplay").append("</div>");
        }
        count++;
    }
}
function getEvent(name, year, month, day, title) {
    let date = year + "-" + month + "-" + day;
    sessionStorage.setItem("provider", name);
    sessionStorage.setItem("date", date);
    sessionStorage.setItem("eventTitle", title);
    window.open("event_list.html","_blank");
}
function getProvider(name) {
    sessionStorage.setItem("provider", name);
    window.open("provider_list.html","_blank");
}
/*
* Get the resource and event of given type
* It will jump to the third div and display corresponding provider list and event list.
* */
function getDetail(name){
    location.href = "#thirdPage";
    setTimeout(()=> {
        history.replaceState('', document.title, window.location.origin + window.location.pathname + window.location.search);
    },2)
    $("#providerList").text("");
    $("#typeTitle").text(name);
    sessionStorage.setItem("type", name);
    db.collection("resources").doc(name).get().then((doc) => {
        Object.keys(doc.data()).forEach((i) => {
            db.collection("users").doc(i).get().then((userDoc) => {
                let content = userDoc.data().content;
                let img = "";
                if (content.indexOf("img") != -1) {
                    let startIndex = content.indexOf("src=\"", content.indexOf("img")+3);
                    let endIndex = content.indexOf("\"", startIndex+5);
                    img = content.substring(startIndex+5, endIndex);
                } else
                    img = "src/Image/resource5.jpg";
                $("#providerList").append(`<div class="provider container row justify-content-center" onclick="getProvider('${i}')">
                                                <div class="col-6"><img src="${img}" alt="Provider Image" style="padding: 10px 0; width: 100%"></div>
                                                <div class="col-6">
                                                    <h5 class="providerTitle">${userDoc.data().companyName}</h5>
                                                    <h5 class="providerInfo">Number: \n${userDoc.data().phone}</h5>
                                                </div>
                                        </div>`);
            });
        })
    }).catch((error) => {
        console.log("Error fetching user info: ", error);
    })
    db.collection("events").doc(name).get().then((doc) => {
        event_data["events"] = [];
        if (Object.keys(doc.data()).length !== 0)
            Object.keys(doc.data()).forEach((i) => {
                doc.data()[i].forEach((j) => {
                    let firstIndex = i.indexOf("-");
                    let secondIndex = i.indexOf("-", firstIndex+1);
                    let year = i.substring(0,firstIndex);
                    let month = i.substring(firstIndex+1,secondIndex);
                    let day = i.substring(secondIndex+1);
                    db.collection("users").doc(j.email).get().then((userDoc)=> {
                        new_event_json(j.title, j.email, parseInt(year), parseInt(month), parseInt(day), userDoc.data().companyName);
                    })
                });
            })
        else {
            event_data["events"] = [];
            init_calendar(new Date());
        }
    }).catch((error) => {
        console.log("Error fetching user info: ", error);
    })
}

function addNav(data) {
    for (let i = 0; i < data.length; i++) {
        $("#type").append("<li><a href=\"#thirdPage\" class=\"dropdown-item\" onclick='getDetail(\""+data[i].name+"\")'>"+data[i].name+"</a></li>")
    }
}
async function getType() {
    console.log("Getting type");
    let types = [], data = [];
    await db.collection("type").get().then((query) => {
        query.forEach((doc)=> {
            if (!doc.data()['isEmpty']) types.push(doc.data());
        });
    }).then(() => {
        addNav(types);
        addCarousel(types);
    }).catch((e) => {
        console.log("Error getting documents: ", e);
    });

}

$(document).ready(() => {
    sessionStorage.clear();
    getType();
})