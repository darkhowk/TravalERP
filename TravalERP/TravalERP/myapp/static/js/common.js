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


function getDetailData(type, id, table){
    // 공통으로 디테일 가져와서 뿌리는것 만들어야함.
    // 1. 해당 타입, 아이디로 검색
    var jsonData = JSON.stringify({'type':type, 'id':id});
        $.ajax({
            url: '/ajax/searchDetail',
            method: 'POST',
            data: jsonData,
            headers: { "X-CSRFToken": $('[name="csrfmiddlewaretoken"]').val() }, // CSRF 토큰을 HTTP 헤더에 추가
            ContentType: 'application/json',
            dataType: 'json',
            success: function(data) {
                setDetailData(data, table, id);
            },
            error: function(xhr, status, error) {
                alert(' 실패')
            }
        }); 
}

function setDetailData(data, table, id) {
    var table = $("#" + table);
    var tbody = table.find("tbody");
    var thead = table.find("thead");
    var headers = [];
    var target = $("#target").val();

    // thead에 있는 th들의 id 값을 headers 배열에 저장
    thead.find("th").each(function() {
      headers.push($(this).attr("id"));
    });
  
    // 데이터 개수만큼 row 생성
    var tbody = document.getElementById("tbody");
    for (var i = 0; i < data.length; i++) {
        var row = tbody.insertRow(i)
  
      // headers 배열의 순서대로 데이터를 td에 추가
      for (var j = 0; j < headers.length; j++) {
        var header = headers[j];
        var value = data[i][header];

        // null 또는 undefined인 경우 빈 값으로 처리
        if (value == null || value == undefined) {
            value = '';
        }
        var cell = row.insertCell(j);
         var target = $("#target").val();
        if (j == 0){
            cell.innerHTML = "<td class='col'><input style='width:100%;' type='checkbox' id='delete'><input type='hidden' id='id' name='id' value='"+data[i]['id']+"' ><input type='hidden' id='use_yn' name='use_yn' value='Y'><input type='hidden' id='"+target+"_id' name='"+target+"_id' value='"+id+"'></td>";
        }
        else if (j == 1){
            cell.innerHTML = "<td class='col'>"+i+"</td>";
        }
        else{
            cell.innerHTML = "<td class='col'><input style='width:100%;' type='text' id='"+header+"' name='"+header+"' value='"+value+"'></td>";
        }
    }
  
    tbody.append(row);

    }
}