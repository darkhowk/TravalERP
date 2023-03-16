function makeForm(actionUrl, fName){
    var f = document.createElement("form");
    f.name = fName;
    f.id = fName;
    f.action = actionUrl;
    f.method = "post";
    f.target = '';

    f.appendChild(addData('csrfmiddlewaretoken', '{{ csrf_token }}'));
    return f;
}

function addData(name, value){
    var elem = document.createElement("input");
    elem.setAttribute("type", "hidden");
    elem.setAttribute("name", name);
    elem.setAttribute("value", value);

    return elem;
}
function addMenu(){
    var perPage =  $('#perPage').val();
    var paging =$('#paging').val();
    var target =$('#target').val();
    var type =$('#type').val();
    movePage('setting/'+target+'/add?pageType=I'+'&perPage='+perPage+'&paging='+paging+'&type='+type)
}
$(document).on('change', '#perPage', function() {
    var perPage = $(this).val();
    location.href = location.origin + location.pathname + '?perPage='+ perPage
});

$(document).on('dblclick','tr', function(e){
    var id = e.currentTarget.id;
    var perPage =  $('#perPage').val();
    var paging =$('#paging').val();
    var target =$('#target').val();
    var type =$('#type').val();
    if (id != ''){
        movePage('setting/'+target+'/add?pageType=U&id='+id+'&perPage='+perPage+'&paging='+paging+'&type='+type)
    }
})

function goPage(page){
    var perPage =  $('#perPage').val();
    var target =$('#target').val();
       movePage('setting/'+target+'?perPage='+perPage+'&paging='+page)
}