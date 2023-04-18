function makeForm(actionUrl, fName){
    var f = document.createElement("form");
    f.name = fName;
    f.id = fName;
    f.action = actionUrl;
    f.method = "post";
    f.target = '';

    return f;
}

function addData(name, value){
    var elem = document.createElement("input");
    elem.setAttribute("type", "hidden");
    elem.setAttribute("name", name);
    elem.setAttribute("value", value);

    return elem;
}

function existFunction(func){
    var f = '';
    if(func.indexOf("(") > -1){
        f = func.substring(0, func.indexOf("("));
    }
    else{
        f = func;
    }

    return typeof window[f] === 'function';
}


function getAjax(fName, item, suF, suP){
    var formArray = $("#"+fName).serializeArray();
    var formData = {};
    for (var i = 0; i < formArray.length; i++) {
        formData[formArray[i].name] = formArray[i].value;
    }
   
    var jsonData = JSON.stringify(formData);

    $.ajax({
        url: '/ajax/get/'+item,
        method: 'POST',
        data: jsonData,
        headers: { "X-CSRFToken": $('[name="csrfmiddlewaretoken"]').val() }, // CSRF 토큰을 HTTP 헤더에 추가
        ContentType: 'application/json',
        dataType: 'json',
        success: function(data) {
            if (existFunction(suF)){
                var p = suF.indexOf("(");
                if (p > -1 ){
                    eval(suF);
                }
                else{
                    eval(suF+"(data, suP)");
                }
            }
        },
        error: function(xhr, status, error) {
            alert(' 실패')
        }
    });
}


function getLikeAjax(fName, item, suF, suP){
    alert("???")
    var formArray = $("#"+fName).serializeArray();
    var formData = {};
    for (var i = 0; i < formArray.length; i++) {
        formData[formArray[i].name] = formArray[i].value;
    }
   
    var jsonData = JSON.stringify(formData);

    $.ajax({
        url: '/ajax/getLike/'+item,
        method: 'POST',
        data: jsonData,
        headers: { "X-CSRFToken": $('[name="csrfmiddlewaretoken"]').val() }, // CSRF 토큰을 HTTP 헤더에 추가
        ContentType: 'application/json',
        dataType: 'json',
        success: function(data) {
            if (existFunction(suF)){
                var p = suF.indexOf("(");
                if (p > -1 ){
                    eval(suF);
                }
                else{
                    eval(suF+"(data, suP)");
                }
            }
        },
        error: function(xhr, status, error) {
            alert(' 실패')
        }
    });
}
