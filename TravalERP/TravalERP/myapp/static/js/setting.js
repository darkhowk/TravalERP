
function addMenu(){
    var perPage =  $('#perPage').val();
    var paging =$('#paging').val();
    var target =$('#target').val();
    var type =$('#type').val();
    movePage('setting/'+target+'/add?pageType=I'+'&perPage='+perPage+'&paging='+paging+'&type='+type+'&target='+target)
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
        movePage('setting/'+target+'/add?pageType=U&id='+id+'&perPage='+perPage+'&paging='+paging+'&type='+type+"&target="+target)
    }
})
// 페이지 이동하는 함수
function goPage(page){
    var perPage =  $('#perPage').val();
    var target =$('#target').val();
    movePage('setting/commonSettingView?perPage='+perPage+'&paging='+page+"&target="+target)
}

// 입력, 수정 화면에서 목록으로 나오는 함수
function goMenuList(){
    var perPage = $("#perPage").val();
    var page = $("#paging").val();
    var target =$('#target').val();
    movePage('setting/commonSettingView?paging='+page+"&perPage="+perPage+"&target="+target)
}

function saveData(fName){
    var jsonData = $("#"+fName).serializeArray()
    $.ajax({
        url: 'addData', // 앞에 자동으로 setting/agent 붙음
        method: 'POST',
        data: jsonData,
        dataType: 'json',
        success: function(data) {
            alert('입력 완료 목록 화면으로 이동합니다.')
            goMenuList();
        },
        error: function(xhr, status, error) {
            alert('등록 실패')
        }
    });
}

function updateData(fName){
    var jsonData = $("#"+fName).serializeArray()
    $.ajax({
        url: 'updateData', // 앞에 자동으로 setting/agent 붙음
        method: 'POST',
        data: jsonData,
        dataType: 'json',
        success: function(data) {
            alert('수정성공 메뉴등록 화면으로 이동합니다.')
            goMenuList();
        },
        error: function(xhr, status, error) {
            alert('여행사 수정 실패')
        }
    });
}

function deleteData(fName){
    var jsonData = $("#"+fName).serializeArray()
    $.ajax({
        url: 'deleteData', // 앞에 자동으로 setting/agent 붙음
        method: 'POST',
        data: jsonData,
        dataType: 'json',
        success: function(data) {
            alert('삭제성공 메뉴등록 화면으로 이동합니다.')
            goMenuList();
        },
        error: function(xhr, status, error) {
            alert('메뉴 삭제 실패')
        }
    });
}