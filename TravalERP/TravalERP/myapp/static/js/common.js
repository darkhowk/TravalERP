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

function searchREF(){
    var ref = $("#paramRef").val();
    var target = $("#target").val();
    $("#refFrm").remove();
    var frm = makeForm('', 'refFrm');
    frm.appendChild(addData('ref', ref));
    frm.appendChild(addData('use_yn', 'Y'));
    document.body.appendChild(frm);
    getREFAjax('refFrm', target, 'searchREFSucc');
}

function getREFAjax(fName, target, suF){

    var formArray = $("#"+fName).serializeArray();
    var formData = {};
    for (var i = 0; i < formArray.length; i++) {
        formData[formArray[i].name] = formArray[i].value;
    }

    var jsonData = JSON.stringify(formData);
    $.ajax({
        url: '/ajax/getREF/'+target,
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
                    eval(suF+"(data)");
                }
            }
        },
        error: function(xhr, status, error) {
            alert(' 실패')
        }
    });
}

var refData;
var masterData;
function searchREFSucc(data){


    var masterList = data.master_id;
    var refList = data.refList;
    refData = '';
    refData = refList
    masterData = '';
    masterData = masterList;

    // 상품명 / 몇박 몇일 / 담당자
    var result = $("#ref_result"); 
    result.empty();
    for (var i = 0; i < refList.length; i ++){
        result.append("<div class='col-4' style='overflow: hidden; text-overflow: ellipsis; white-space: nowrap; font-weight: bold;' data-row="+i+">"+refList[i].ref+"</div>")
        result.append("<div class='col-6 mt-1' style='overflow: hidden; text-overflow: ellipsis; white-space: nowrap;' data-row="+i+">"+refList[i].product_name+"</div>")
        result.append("<div class='col-2 mt-1' style='overflow: hidden; text-overflow: ellipsis; white-space: nowrap;' data-row="+i+">"+refList[i].kor_air_date+"</div>")     
    }
}

$(document).on('dblclick', '#ref_result > div', function() {
	var row = $(this).data('row');
	var id = masterData[row];
    var ref = refData[row].ref;

	$("#paramRef").val(ref);
	$('#master_id').val(id);

    $('#refModal').modal('hide');
});

$('#refModal').on('shown.bs.modal', function () {
    $('#ref_result').empty();

});