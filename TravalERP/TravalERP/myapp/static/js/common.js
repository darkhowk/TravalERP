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