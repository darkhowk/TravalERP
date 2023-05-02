
function addMenu(){
    var perPage =  $('#perPage').val();
    var paging =$('#paging').val();
    var target =$('#target').val();
    var type =$('#type').val();
    movePage(target+'/add?pageType=I'+'&perPage='+perPage+'&paging='+paging+'&type='+type+'&target='+target)
}
$(document).on('change', '#perPage', function() {
    var perPage = $(this).val();
    var target =$('#target').val();
    var type =$('#type').val();
    location.href = location.origin + location.pathname +'?perPage='+ perPage +'&type='+type+'&target='+target
});

$(document).on('dblclick','tr', function(e){
    var id = e.currentTarget.id;
    var perPage =  $('#perPage').val();
    var paging =$('#paging').val();
    var target =$('#target').val();
    var type =$('#type').val();
    if (id != ''){
        movePage(target+'/add?pageType=U&id='+id+'&perPage='+perPage+'&paging='+paging+'&type='+type+"&target="+target)
    }
})
// 페이지 이동하는 함수
function goPage(page){
    var perPage =  $('#perPage').val();
    var target =$('#target').val();
    var type =$('#type').val();
    movePage(target+'?perPage='+perPage+'&paging='+page+"&target="+target +'&type='+type)
}

// 입력, 수정 화면에서 목록으로 나오는 함수
function goMenuList(){
    var perPage = $("#perPage").val();
    var page = $("#paging").val();
    var target =$('#target').val();
    var type =$('#type').val();
    movePage(target+'?paging='+page+"&perPage="+perPage+"&target="+target +'&type='+type)
}

function saveData(fName){
    $("#type").attr("disabled", true);
    var target = $("#target").val();
    if (target == 'rooming'){
        // master_id --> booking_id 로 변경하여 저장
		$("#booking_id").val($("#master_id").val());
		$("#master_id").attr("disabled", true)
		$("#tc_name").attr("disabled", true)
    }
    
    var jsonData = $("#"+fName).serializeArray();

	$.ajax({
		url: '/ajax/insertData/master/'+target, // 앞에 자동으로 setting/agent 붙음
		method: 'POST',
		data: jsonData,
		dataType: 'json',
		success: function(data) {
			id = data.id
			saveDetail(id);
		},
		error: function(xhr, status, error) {
			alert('등록 실패')
		}
	});
}

function saveDetail(id){
    var target = $("#target").val();
    var tableJson;
    if (target == 'booking'){
        $('input[name="booking_id"]').val(id);
        var sch = tableToJson(document.getElementById('schdule_table'));
        var hot = tableToJson(document.getElementById('hotel_table'));
        tableJson = mergeJson(sch, hot);
    }
    else if(target == 'rooming'){
        $('input[name="rooming_id"]').val(id);
		var room = tableToJson(document.getElementById('roomingList'));
        tableJson = room;
    }

	$.ajax({
		url: '/ajax/insertData/detail/'+target, // 앞에 자동으로 setting/agent 붙음
		method: 'POST',
		data: JSON.stringify(tableJson),
		headers: { "X-CSRFToken": $('[name="csrfmiddlewaretoken"]').val() }, // CSRF 토큰을 HTTP 헤더에 추가
		dataType: 'json',
		success: function(data) {
            $("#type").attr("disabled", false);
			alert('입력 완료 목록 화면으로 이동합니다.');
            goMenuList();
		},
		error: function(xhr, status, error) {
            $("#type").attr("disabled", false);
			alert('등록 실패')
		}
	});
}

function updateData(fName){
    $("#type").attr("disabled", true);
    var target = $("#target").val();
    if (target == 'rooming'){
        // master_id --> booking_id 로 변경하여 저장
		$("#booking_id").val($("#master_id").val());
		$("#master_id").attr("disabled", true)
		$("#tc_name").attr("disabled", true)
    }
    
    var jsonData = $("#"+fName).serializeArray();
   
    $.ajax({
        url: '/ajax/updateData/master/'+target, // 앞에 자동으로 setting/agent 붙음
        method: 'POST',
        data: jsonData,
        dataType: 'json',
        success: function(data) {
            id = data.id
            updateDetail(id);
        },
        error: function(xhr, status, error) {
            alert('등록 실패')
        }
    });
}

function updateDetail(id){
    var tableJson;
    var target = $("#target").val();
    if (target == 'booking'){
        $('input[name="booking_id"]').val(id);
        var sch = tableToJson(document.getElementById('schdule_table'));
        var hot = tableToJson(document.getElementById('hotel_table'));
        tableJson = mergeJson(sch, hot);
    }
    else if(target == 'rooming'){
        $('input[name="rooming_id"]').val(id);
		var room = tableToJson(document.getElementById('roomingList'));
        tableJson = room;
    }

    $.ajax({
        url: '/ajax/updateData/detail/'+target, // 앞에 자동으로 setting/agent 붙음
        method: 'POST',
        data: JSON.stringify(tableJson),
        headers: { "X-CSRFToken": $('[name="csrfmiddlewaretoken"]').val() }, // CSRF 토큰을 HTTP 헤더에 추가
        dataType: 'json',
        success: function(data) {
            $("#type").attr("disabled", false);
            alert('입력 완료 목록 화면으로 이동합니다.')
            goMenuList();
        },
        error: function(xhr, status, error) {
            $("#type").attr("disabled", false);
            alert('등록 실패')
        }
    });
}


function deleteData(fName){
    $("#type").attr("disabled", true);
    var target = $("#target").val();
    if (target == 'rooming'){
        // master_id --> booking_id 로 변경하여 저장
		$("#booking_id").val($("#master_id").val());
		$("#master_id").attr("disabled", true)
		$("#tc_name").attr("disabled", true)
    }
    
    var jsonData = $("#"+fName).serializeArray();
   
    $.ajax({
        url: '/ajax/deleteData/master/'+target, // 앞에 자동으로 setting/agent 붙음
        method: 'POST',
        data: jsonData,
        dataType: 'json',
        success: function(data) {
            id = data.id
            deleteDetail( id);
        },
        error: function(xhr, status, error) {
            alert('삭제 실패')
        }
    });
}

function deleteDetail(id){
    var tableJson ;
    var target = $("#target").val();
    if (target == 'booking'){
	$('input[name="booking_id"]').val(id);
        var sch = tableToJson(document.getElementById('schdule_table'));
        var hot = tableToJson(document.getElementById('hotel_table'));
    	tableJson = mergeJson(sch, hot);
    }
    else if(target == 'rooming'){
        $('input[name="rooming_id"]').val(id);
		var room = tableToJson(document.getElementById('roomingList'));
        tableJson = room;
    }

    $.ajax({
        url: '/ajax/deleteData/detail/'+target, // 앞에 자동으로 setting/agent 붙음
        method: 'POST',
        data: JSON.stringify(tableJson),
        headers: { "X-CSRFToken": $('[name="csrfmiddlewaretoken"]').val() }, // CSRF 토큰을 HTTP 헤더에 추가
        dataType: 'json',
        success: function(data) {
            $("#type").attr("disabled", false);
            alert('삭제 완료 목록 화면으로 이동합니다.')
            goMenuList();
        },
        error: function(xhr, status, error) {
            $("#type").attr("disabled", false);
            alert('삭제 실패')
        }
    });
}


